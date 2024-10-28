from pathlib import Path

import sh
import typer
from resume_builder.documents import ResumeDocument


app = typer.Typer()

@app.command()
def render(data: str = "bse-python"):
    data_path = Path("data") / f"{data}.yaml"
    with data_path.open() as fd:
        doc = ResumeDocument.from_jsonresume(fd)
    
    export_path = Path("latex") / "temp"
    with export_path.open("w") as fd:
        doc.export(fd)
    
    sh.Command("scripts/xelatex")("temp")
    sh.mv("latex/temp.pdf", f"export/{doc.file_name}.pdf")
    sh.rm("-f", "latex/temp*")
    sh.Command("pdftotext")("-layout", f"export/{doc.file_name}.pdf")
    

@app.command()
def get_filename(data: str = "bse-python"):
    data_path = Path("data") / f"{data}.yaml"
    with data_path.open() as fd:
        doc = ResumeDocument.from_jsonresume(fd)
    print(doc.file_name)