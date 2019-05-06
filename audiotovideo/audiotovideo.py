import subprocess
import os, time, datetime
import re

# replace filenames with spaces
path = os.getcwd()
filenames = os.listdir(path + "/audios")
for filename in filenames:
    os.rename(os.path.join(path + "/audios", filename), os.path.join(path + "/audios", filename.replace(' ', '_')))

filenames = os.listdir(path + "/audios")
filenames = ['audios/' + x for x in filenames]


def getdatefromfilename(x):
    list_of_date = re.findall(r'Audio_recording_(\d*)-(\d*)-(\d*)_(\d)*-(\d*)-(\d*)', x)
    try:
        listofdate = [int(x) for x in list(list_of_date[0])]
    except:
        listofdate = []
    if len(listofdate) < 6:
        return datetime.datetime.now()
    else:
        return datetime.datetime(listofdate[0], listofdate[1], listofdate[2], listofdate[3], listofdate[4],
                                 listofdate[5])


for audioname in filenames:
    audioname=filenames[0]
    imagename = "dark.bmp"
    outputname = audioname.split('.')[0] + '.avi'
    outputname = outputname.replace("audios", "videos")

    file = audioname
    modified = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    created = datetime.datetime.fromtimestamp(os.path.getctime(file))
    fromfilename = getdatefromfilename(file)

    command = 'ffmpeg -loop 1 -r 0.1 -y -i ' + imagename + ' -i ' + audioname + ' -shortest -acodec copy -vcodec mjpeg ' + outputname
    subprocess.check_call(command.split())

    date = min(modified, created, fromfilename)
    modTime = time.mktime(date.timetuple())

    os.utime(outputname, (modTime, modTime))
