VERSION = 3.0.0
DATA = data/bse-python.yaml

filedir = export
filename = Joe_Black_resume_backend-software-engineer_python_v$(VERSION).pdf

.PHONY: build_docker generate_thumbnails dump_json build_package render build_pdf move_and_rename clean_up extract_txt preview

# install_deps:
# 	ifneq (,$(shell which apt))
# 	sudo apt install -y poppler-utils yq
# 	else ifneq (,$(shell which brew))
# 	brew install poppler yq
# 	endif

build_docker:
    docker buildx build --platform linux/amd64,linux/arm64 -t joeblackwaslike/texlive:2016 --push docker-texlive

generate_thumbnails:
	pdftoppm -png $(filedir)/$(filename) preview

dump_json:
	yq . data/bse-python.yaml

build_package:
	pip install -e .

build_pdf:
	scripts/xelatex temp

move_and_rename:
	mv latex/temp.pdf $(filedir)/$(filename)

clean_up:
	rm -f latex/temp*

extract_txt:
	pdftotext -layout $(filedir)/$(filename)

preview:
	open $(filedir)/$(filename)

render: build_pdf move_and_rename clean_up extract_txt preview
	@echo "Finished generating: $(filedir)/$(filename)"