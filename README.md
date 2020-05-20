# CV
Latex files for curriculum vitae.

CV.pdf is longw-winded
CV_short.pdf is a bit more compact.
 
You can still use TexShop to edits Latex and Bib files, but do not try to compile. Instead use:

./make_cv.sh
or
./make_cv_short.sh

It generates a lot of error messages, but it works.

To clean up and start over:

rm -f *.aux *.bbl *.blg *.log CV.out CV.pdf

To generate the file vita_2020.txt, I opened vita_2020.doc
in MS Word, did Save As, chose plain text and UTF-16 encoding.
But it's not worth redoing, because original Word doc is riddled with
errors and inconsistencies.

