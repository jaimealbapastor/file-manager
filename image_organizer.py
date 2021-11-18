# copié sur internet

# fx paths
import os
from pathlib import Path
import shutil
# fx imagen y exif
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
# fx hash
import hashlib


def get_exif(filename: str):
    try:
        exif = Image.open(filename)._getexif()

        if exif is not None:
            for key, value in exif.items():
                name = TAGS.get(key, key)  # to decode key into readable name
                exif[name] = exif.pop(key)  # replace key into name

            if 'GPSInfo' in exif:
                for key in exif['GPSInfo'].keys():
                    name = GPSTAGS.get(key, key)
                    exif['GPSInfo'][name] = exif['GPSInfo'].pop(key)

        return exif

    except Exception as e:
        print("Error: %s" % (e))
        return None
    except:
        print("Error desconocido")
        return None


def getmd5file(filename):
    try:
        hashmd5 = hashlib.md5()
        with open(filename, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashmd5.update(bloque)
        return hashmd5.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""


def _newfilename(md5, datetimeimg, ext):
    stmp = datetimeimg.replace(" ", "")
    stmp = stmp.replace(":", "")
    # la vble extension debe incluir el "."
    return stmp + "_" + md5 + ext


def _newsubdir(datetimeimg):
    stmp = datetimeimg.replace(" ", "")
    stmp = stmp.replace(":", "")
    stmp = stmp[0:6]
    return stmp


def _createdir(newdir):
    try:
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        return True
    except OSError as e:
        return False


def _copyfilerep(oldfile, newdir, newfile):
    snewpath = newdir + "/" + newfile
    if _createdir(newdir):
        print("_copyfilerep: " + oldfile + " --> " + snewpath)
        if not os.path.exists(snewpath):
            shutil.copy2(oldfile, snewpath)
    else:
        print("_copyfilerep ERROR: " + oldfile + " --> " + snewpath)


def _checkdir(spathdir, snewdir):
    nfiles = 0
    nfilesexifs = 0
    for root, dirs, files in os.walk(spathdir):
        for file in [f for f in files if f.lower().endswith(('.jpg', '.jpeg'))]:
            nfiles += 1
            sfilepath = os.path.join(root, file)
            print(sfilepath)
            datetimeimg = "19000101000000"
            md5 = getmd5file(sfilepath)
            print(md5)
            exif = get_exif(sfilepath)
            if exif is None:
                datetimeimg = "19020101000000"
            else:
                # si hay datos exif:
                nfilesexifs += 1
                if "DateTimeOriginal" in exif:
                    datetimeimg = exif["DateTimeOriginal"]
                    print(datetimeimg)

            snewfilename = _newfilename(md5, datetimeimg, ".jpg")
            snewsubdir = _newsubdir(datetimeimg)
            print(sfilepath + ">>" + snewdir + "/" +
                  snewsubdir + "/" + snewfilename)
            _copyfilerep(sfilepath, snewdir + "/" + snewsubdir, snewfilename)

        print("total archivos: %d / %d" % (nfilesexifs, nfiles))


# MAIN
spathrep = "/media/lubuntu/2106-0208/cmrep"
spathimgs = "/home/lubuntu/Pictures/Imagenes"
_checkdir(spathimgs, spathrep)

print("end!")
