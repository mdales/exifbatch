Small script to late me take a csv file of EXIF settings and apply them to a folder full of images.

The first column should be the shot number, and the second column should be the file name. The first row (excluding the first two columns) should be the EXIF field name.

For example:

```
shot,filename,fnumber,exposuretime,iso,make,model,lensmake,lensmodel,lensinfo,caption,focallength
0,000001910036.tif,5.6,1/350,400,Canon,EOS 300,Canon,EF50mm f/1.8 II,50 mm f/1.8,Illford HP5+,50 mm
1,000001910035.tif,1.8,1/1500,400,Canon,EOS 300,Canon,EF50mm f/1.8 II,50 mm f/1.8,Illford HP5+,50 mm
2,000001910034.tif,5.6,1/500,400,Canon,EOS 300,Canon,EF50mm f/1.8 II,50 mm f/1.8,Illford HP5+,50 mm
```
