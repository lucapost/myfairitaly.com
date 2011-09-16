#!/bin/bash

outdir="`echo $1 |sed -e 's/input\///'`"
echo $outdir
rm -rf $outdir
mkdir $outdir tmp -p

for img in `ls $1`; do
		convert $1/$img tmp/tmp.png
		composite -gravity SouthEast input/wm.png tmp/tmp.png tmp/tmp.png
		convert tmp/tmp.png \
			\( +clone  -alpha extract \
			-draw 'fill black polygon 0,0 0,10 10,0 fill white circle 10,10 10,0' \
			\( +clone -flip \) -compose Multiply -composite \
			\( +clone -flop \) -compose Multiply -composite \
			\) -alpha off -compose CopyOpacity -composite tmp/tmp.png
		composite -background white -gravity center tmp/tmp.png input/background.png tmp/tmp.png
		convert tmp/tmp.png $outdir/$img
		echo $img
done
rm -rf tmp/
rm -rf $outdir/data.txt
