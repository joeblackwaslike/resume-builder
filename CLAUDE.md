# resume-builder

Python tool that renders a PDF resume from jsonresume-conforming YAML via XeLaTeX (awesome-cv).

## Layout

```
src/resume_builder/   # Python package
  cli.py              # typer CLI — `builder render`
  documents.py        # ResumeDocument → LaTeX
  commands.py         # pylatex command wrappers
  jsonresume.py       # jsonresume parsing helpers
  environments.py     # pylatex environment wrappers
data/                 # git submodule → github.com/joeblackwaslike/resume-data
  base.yaml           # canonical resume (jsonresume YAML)
  base-cs.yaml        # CS-focused variant
  patches/            # JSON Patch files applied on top of base
latex/                # LaTeX class + fonts; temp build artifacts land here
export/               # Output PDFs and extracted text
scripts/xelatex       # Shell wrapper that invokes xelatex with correct paths
```

## Commands

```sh
# install / sync deps
uv sync

# render base resume (outputs to export/)
builder render

# render with a patch
builder render --patch python
builder render --patch anthropic-research-tools

# render a different base
builder render --base base-cs --patch cs

# lint / format
ruff check src/
ruff format src/

# type check
mypy
```

Available patches: `python`, `cs`, `ct`, `fullstack`, `mercor`, `web3`, `anthropic-research-tools`, `anthropic-sandboxing`

## Data submodule

`data/` is a git submodule. After cloning:

```sh
git submodule update --init --recursive
```

If you modify resume data, commit in `data/` first, then stage the updated pointer in the parent repo and commit both.

## Output naming

The export filename is derived from the YAML `meta` fields: `Joe_Black_v{version}[_{patch}].pdf`

## Stack

- Python 3.8+, managed with `uv`
- Typer CLI, PyYAML, jsonpatch, PyLaTeX, sh
- XeLaTeX for PDF rendering (requires a TeX Live install or the Docker image in `docker-texlive/`)
- Ruff for lint/format, mypy for type checking
