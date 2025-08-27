all: pdf

PDF=pdflatex

pdf: paper.pdf

paper.pdf: paper.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

clean:
	latexmk -C

.PHONY: all pdf clean
