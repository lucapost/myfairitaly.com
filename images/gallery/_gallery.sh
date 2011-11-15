#!/bin/bash

input=$1
outdir="`echo $1 |sed -e 's/_//'`"

if [ "${input+x}" = x ] && [ -z "$input" ]; then
	echo "please indicate folder, correct syntax is: ./generate.sh _pathoforiginalimages"
	exit 0
fi

rm tmp -rf
mkdir $outdir tmp -p
cp $input/*.jpg tmp/

for img in `ls tmp`; do
		convert tmp/$img tmp/tmp.png
		composite -gravity SouthEast _wm.png tmp/tmp.png tmp/tmp.png
		convert tmp/tmp.png \
			\( +clone  -alpha extract \
			-draw 'fill black polygon 0,0 0,10 10,0 fill white circle 10,10 10,0' \
			\( +clone -flip \) -compose Multiply -composite \
			\( +clone -flop \) -compose Multiply -composite \
			\) -alpha off -compose CopyOpacity -composite tmp/tmp.png
		composite -background white -gravity center tmp/tmp.png _background.png tmp/tmp.png
		convert tmp/tmp.png $outdir/$img
		echo $img
done
rm -rf tmp/
echo "./$outdir OK"
