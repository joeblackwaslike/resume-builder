from pathlib import Path

import jsonpatch
import sh
import typer
import yaml

from resume_builder.documents import ResumeDocument

app = typer.Typer()


@app.command()
def render(base: str = "base", patch: str = "", accent_color: str = "00a388"):
    data_path = Path("data") / f"{base}.yaml"
    with data_path.open() as fd:
        data = yaml.load(fd, yaml.SafeLoader)
        if patch:
            patch_path = Path("data") / "patches" / f"{patch}.yaml"
            with patch_path.open() as fd:
                patch = jsonpatch.JsonPatch(yaml.load(fd, yaml.SafeLoader))
                data = patch.apply(data)

        doc = ResumeDocument.from_jsonresume(data, accent_color=accent_color)

    export_path = Path("latex") / "temp"
    with export_path.open("w") as fd:
        doc.export(fd)

    sh.Command("scripts/xelatex")("temp")
    sh.mv("latex/temp.pdf", f"export/{doc.file_name}.pdf")
    sh.rm("-f", "latex/temp*")
    sh.Command("pdftotext")("-layout", f"export/{doc.file_name}.pdf")


# @app.command()
# def get_filename(base: str = "base"):
#     data_path = Path("data") / f"{base}.yaml"
#     with data_path.open() as fd:
#         doc = ResumeDocument.from_jsonresume(fd)
#     print(doc.file_name)
