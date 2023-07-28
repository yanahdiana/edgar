from GPSPhoto import gpsphoto
import os
from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint

jpg = "edgar/foo_app/1.jpg"
image = Image.open(jpg)
exif = {}

for tag, value in image._getexif().items():
    if tag in TAGS:
        exif[TAGS[tag]]=value
pprint(exif)

data = gpsphoto.getGPSData('edgar/foo_app/1.jpg')
pprint(data)

myexifdata = {
    "DateTime": f"{exif['DateTimeOriginal']} {exif['OffsetTime']}",
    "Brand": exif['Make'],
    "Model": exif['Model'],
    "FocalLength": exif['FocalLength'],
    "ResolutionUnit": exif['ResolutionUnit'],
    "Width": exif['ExifImageWidth'],
    "Height": exif['ExifImageHeight'],
    "Location": f"{data['Latitude']},{data['Longitude']}",
    "Altitude": data['Altitude'],
    "Lens" : exif['LensModel'].removeprefix(exif['Model']).strip()
}

pprint(myexifdata)


