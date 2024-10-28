import json
from typing import Annotated

import typer
import yaml


def transform(data):
    data["meta"] = {}
    for item in data.get("awards", []):
        if "location" in item:
            del item["location"]

    skills = []
    for item in data.get("skills", []):
        for skill in item["keywords"]:
            skills.append(
                dict(name=skill)
            )
    data["skills"] = skills

    if "education" in data:
        del data["education"]

    for item in data.get("projects", []):
        if "summary" in item:
            item["description"] = item.pop("summary")
        for field in ("type", "language", "github", "docker", "entity", "roles", "keywords"):
            if field in item:
                del item[field]
    return data

def main(
    yaml_file: Annotated[typer.FileText, typer.Option()] = "data/bse-python.yaml", 
    json_file: Annotated[typer.FileTextWrite, typer.Option()] = "data/bse-python.json",
):
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    data = transform(data)
    json.dump(data, json_file, indent=2)
    print("Converted YAML to JSON")


if __name__ == "__main__":
    typer.run(main)
