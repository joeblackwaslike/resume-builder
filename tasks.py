from invoke import task
from builder import ResumeDocument


@task
def build_docker(ctx):
    ctx.run("docker build -t joeblackwaslike/texlive:2016 docker-texlive")


@task
def render(ctx, data="blockchain", pty=True):
    data_path = f"data/{data}.yaml"

    # Generate latex
    doc = ResumeDocument.from_jsonresume(data_path)
    doc.export("latex/temp")
    ctx.run("scripts/xelatex temp")

    # Move and rename
    file_name = f"{doc.file_name}.pdf"
    ctx.run(f"mv latex/temp.pdf export/{file_name}")

    # clean up
    ctx.run("rm -f latex/temp*")

    # extract text to check machine parsers
    ctx.run(f"pdftotext -layout export/{file_name}")

    # open to preview pdf
    ctx.run(f"open export/{file_name}")

    print(f"Finished generating: {file_name}")
