#!/bin/sh

outdir=`echo $1 |sed -e 's/origin\///'`
rm -rf $outdir 
mkdir $outdir

mkdir tmp
cp $1/*.jpg tmp/

for i in `ls tmp/*.jpg` ; do
	convert $i tmp/tmp.png
	composite -gravity SouthEast origin/wm.png tmp/tmp.png tmp/tmp.png
	convert tmp/tmp.png \
		\( +clone  -alpha extract \
		-draw 'fill black polygon 0,0 0,10 10,0 fill white circle 10,10 10,0' \
		\( +clone -flip \) -compose Multiply -composite \
		\( +clone -flop \) -compose Multiply -composite \
		\) -alpha off -compose CopyOpacity -composite tmp/tmp.png
	composite -background white -gravity center tmp/tmp.png origin/background.png tmp/tmp.png
	outname=`echo $i |sed -e 's/tmp\///'`
	convert tmp/tmp.png $outdir/$outname
	echo $outdir/$outname
done

echo  " " 
sed '/^$/d' $1/data.txt > tmp/data.txt
exec 3<&0
exec 0<tmp/data.txt
while read line
do
	# use $line variable to process line
	name=`echo $line | cut -d: -f1`
	alt=`echo $line | cut -d: -f2`
	title=`echo $line | cut -d: -f3`
	echo "<img src=\"/images/gallery/$outdir/$name\" alt=\"$alt\" title=\"$title\" />"
done
exec 0<&3

rm -rf tmp/
