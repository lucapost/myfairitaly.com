#!/bin/bash

input=$1
outdir="source/images/gallery/`echo $1 |sed -e 's/gallerysource\///'`"

if [ "${input+x}" = x ] && [ -z "$input" ]; then
	echo "please indicate folder, correct syntax is: ./generate.sh gallerysource/pathoforiginalimages"
	exit 0
fi

rm tmp -rf
mkdir $outdir tmp -p
cp $input/*.jpg tmp/

for img in `ls tmp`; do
		convert tmp/$img tmp/tmp.png
		composite -gravity SouthEast gallerysource/wm.png tmp/tmp.png tmp/tmp.png
		convert tmp/tmp.png \
			\( +clone  -alpha extract \
			-draw 'fill black polygon 0,0 0,10 10,0 fill white circle 10,10 10,0' \
			\( +clone -flip \) -compose Multiply -composite \
			\( +clone -flop \) -compose Multiply -composite \
			\) -alpha off -compose CopyOpacity -composite tmp/tmp.png
		composite -background white -gravity center tmp/tmp.png gallerysource/background.png tmp/tmp.png
		convert tmp/tmp.png $outdir/$img
		echo $img
done
rm -rf tmp/
echo "./$outdir OK"
