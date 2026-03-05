VERSION = 3.4
DATA = data/base.yaml

filedir = export
filename = Joe_Black_v$(VERSION).pdf


.PHONY: build_docker generate_thumbnails extract_txt preview render all

all: render extract_txt generate_thumbnails preview
	echo "ran pipeline"

render:
	resume-builder render

build_docker:
    docker buildx build --platform linux/amd64,linux/arm64 -t joeblackwaslike/texlive:2016 --push docker-texlive

generate_thumbnails:
	pdftoppm -png $(filedir)/$(filename) preview

extract_txt:
	pdftotext -layout $(filedir)/$(filename)

preview:
	open $(filedir)/$(filename)
