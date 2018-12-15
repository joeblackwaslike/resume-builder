from invoke import task
from builder import ResumeDocument


@task
def build_docker(ctx):
    ctx.run("docker build -t joeblackwaslike/texlive:2016 docker-texlive")


def _build_pdf(ctx):
    ctx.run("scripts/xelatex temp")


def _move_and_rename(ctx, file_name):
    ctx.run(f"mv latex/temp.pdf export/{file_name}")


def _clean_up(ctx):
    ctx.run("rm -f latex/temp*")


def _extract_txt(ctx, file_name):
    ctx.run(f"pdftotext -layout export/{file_name}")


def _preview(ctx, file_name):
    ctx.run(f"open export/{file_name}")


@task
def render(ctx, data="blockchain", pty=True):
    data_path = f"data/{data}.yaml"

    # Generate latex
    doc = ResumeDocument.from_jsonresume(data_path)
    doc.export("latex/temp")
    file_name = f"{doc.file_name}.pdf"

    _build_pdf(ctx)
    _move_and_rename(ctx, file_name)
    _clean_up(ctx)
    _extract_txt(ctx, file_name)
    _preview(ctx, file_name)

    print(f"Finished generating: {file_name}")
