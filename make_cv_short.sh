#!/bin/bash
export PATH=/Library/TeX/texbin:$PATH
export CVTARGET=CV_short.tex
pdflatex $CVTARGET
bibtex bu1.aux
bibtex bu2.aux
bibtex bu3.aux
bibtex bu4.aux
bibtex bu5.aux
bibtex bu6.aux
bibtex bu7.aux
bibtex bu8.aux
bibtex bu9.aux
pdflatex $CVTARGET
pdflatex $CVTARGET
