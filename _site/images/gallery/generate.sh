#!/bin/bash

if [ -e $1/data.txt ]; then
	echo "$1/data.txt"
else 
	echo "$1/data.txt non è presente nella directory specificata"
	exit 0
fi

outdir=`echo $1 |sed -e 's/origin\///'`
rm -rf $outdir 
mkdir $outdir tmp

sed '/^$/d' $1/data.txt > tmp/data.txt

exec 3<&0
exec 0<tmp/data.txt

while read line; do
	
	name=`echo $line | cut -d: -f1`
	altit=`echo $line | cut -d: -f2`
	titleit=`echo $line | cut -d: -f3`
	alten=`echo $line | cut -d: -f4`
	titleen=`echo $line | cut -d: -f5`

	if [ -e $1/$name ]; then
		echo "$1/$name"
	else 
		echo "$1/$name non è presente, controlla la presenza del file o lo struttura di data.txt"
		exit 0
	fi

	convert $1/$name tmp/tmp.png
	composite -gravity SouthEast origin/wm.png tmp/tmp.png tmp/tmp.png
	convert tmp/tmp.png \
		\( +clone  -alpha extract \
		-draw 'fill black polygon 0,0 0,10 10,0 fill white circle 10,10 10,0' \
		\( +clone -flip \) -compose Multiply -composite \
		\( +clone -flop \) -compose Multiply -composite \
		\) -alpha off -compose CopyOpacity -composite tmp/tmp.png
	composite -background white -gravity center tmp/tmp.png origin/background.png tmp/tmp.png
	convert tmp/tmp.png $outdir/$name

	echo "<img src=\"/images/gallery/$outdir/$name\" alt=\"$altit\" title=\"$titleit\" />"  >> tmp/it.txt
	echo "<img src=\"/images/gallery/$outdir/$name\" alt=\"$alten\" title=\"$titleen\" />"  >> tmp/en.txt
done

exec 0<&3

cat tmp/it.txt
echo ""
cat tmp/en.txt

rm -rf tmp/
