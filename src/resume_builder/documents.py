from os.path import join
from os.path import relpath

import yaml
from pylatex import Command
from pylatex import Document
from pylatex import NoEscape

from .commands import Activity
from .commands import Award
from .commands import Education
from .commands import Experience
from .commands import Item
from .commands import MakeCVHeader
from .commands import OSProject
from .commands import Section
from .commands import Skill
from .environments import Awards
from .environments import Entries
from .environments import Items
from .environments import Paragraph
from .environments import Projects
from .environments import Skills


class ResumeDocument(Document):
    def __init__(self, data, *args, exclude=(), **kwargs):
        kwargs.setdefault("default_filepath", relpath(join(".", "export")))
        kwargs.setdefault("document_options", ["11pt", "letterpaper"])
        kwargs.setdefault("documentclass", "awesomecv")
        kwargs.setdefault("accent_color", "awesome-emerald")
        kwargs.setdefault("fontenc", None)
        kwargs.setdefault("inputenc", None)
        kwargs.setdefault("font_size", None)
        kwargs.setdefault("lmodern", None)
        kwargs.setdefault("textcomp", None)
        kwargs.setdefault("page_numbers", None)
        accent_color = kwargs.pop("accent_color")
        
        super().__init__(*args, **kwargs)
        
        self._exclude = set(exclude)
        self.file_name = self.get_file_name(data)
        
        self.preamble.append(
            Command("colorlet", ["awesome", NoEscape(accent_color)])
        )
        self.data.clear()

    @staticmethod
    def get_file_name(data):
        m = data['meta']
        elements = [
            e.replace(" ", "_")
            for e in [
                data['basics']["name"],
                m["name"],
                m["role"],
                m["focus"],
                m["company"],
                m["version"],
            ]
            if e
        ]
        return "_".join(elements)

    def export(self, file_):
        file_.write(self.dumps())

    def _add_masthead(self, data):
        basics = data["basics"]
        location = basics["location"]

        for command in [
            Command("name", basics["name"].split()),
            Command("position", basics["label"]),
            Command("address", f"{location['city']}, {location['region']}"),
            Command("mobile", basics["phone"]),
            Command("email", basics["email"]),
            Command("homepage", basics["website"]),
        ]:
            self.preamble.append(command)

        for profile in basics["profiles"]:
            self.preamble.append(
                Command(profile["network"].lower(), profile["username"])
            )

    def _add_cv_header(self):
        self.append(MakeCVHeader(options=["L"]))

    def add_section(self, title):
        self.append(Section(title))

    def _add_summary(self, data, title="Summary"):
        if "summary" in self._exclude or not data.get("basics", {}).get("summary"):
            return
        self.add_section(title)
        with self.create(Paragraph()) as block:
            block.append(data["basics"]["summary"])

    def _add_skills(self, data, title="Skills"):
        if "skills" in self._exclude or not data.get("skills"):
            return
        self.add_section(title)
        with self.create(Skills()) as block:
            for item in data["skills"]:
                block.append(Skill.from_jsonresume(item))

    def _add_work(self, data, title="Work Experience"):
        if "work" in self._exclude or not data.get("work"):
            return
        self.add_section(title)
        with self.create(Entries()) as block:
            for item in data["work"]:
                entry = Experience.from_jsonresume(item)
                with entry.create(Items()) as items:
                    summary = item.get("summary")
                    if summary:
                        items.append(Item(summary))
                    for bullet in item.get("highlights", []):
                        items.append(Item(bullet))
                block.append(entry)
                
    def _add_projects(self, data, title="Open Source Projects"):
        if "projects" in self._exclude or not data.get("projects"):
            return
        self.add_section(title)
        with self.create(Projects()) as block:
            for item in data["projects"]:
                project = OSProject.from_jsonresume(item)
                block.append(project)

    def _add_volunteer(self, data, title="Community Engagement"):
        if "volunteer" in self._exclude or not data.get("volunteer"):
            return
        self.add_section(title)
        with self.create(Entries()) as block:
            for item in data["volunteer"]:
                activity = Activity.from_jsonresume(item)
                with activity.create(Items()) as items:
                    summary = item.get("summary")
                    if summary:
                        items.append(Item(summary))
                block.append(activity)

    def _add_awards(self, data, title="Awards"):
        if "awards" in self._exclude or not data.get("awards"):
            return
        self.add_section(title)
        with self.create(Awards()) as block:
            for award in data["awards"]:
                block.append(Award.from_jsonresume(award))
                
    def _add_education(self, data, title="Education"):
        if "education" in self._exclude or not data.get("education"):
            return
        self.add_section(title)
        with self.create(Entries()) as block:
            for edu in data["education"]:
                entry = Education.from_jsonresume(edu)
                block.append(entry)

    @classmethod
    def from_jsonresume(cls, file_, **kwargs):
        data = yaml.load(file_, yaml.SafeLoader)
        exclude = data.get("meta", {}).get("exclude", [])
        
        doc = cls(data, exclude=exclude, **kwargs)

        doc._add_masthead(data)
        doc._add_cv_header()

        doc._add_summary(data)
        doc._add_skills(data)
        doc._add_work(data)
        doc._add_projects(data)
        doc._add_volunteer(data)
        doc._add_awards(data)
        doc._add_education(data)

        return doc
