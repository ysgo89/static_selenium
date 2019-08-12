import os
import sys

FILE_PATH = "C:\\Program Files\\Suresofttech\\STATIC Launcher LITE\\resources\\services.json"
FILE_PATH1 = "C:\\Program Files\\Suresofttech\\STATIC Launcher LITE\\resources\\services2.json"
FILE_PATH2 = "C:\\Program Files\\Suresofttech\\STATIC Launcher LITE\\resources\\services3.json"

oldline = '"javaOptions": [\n'
newline = '"javaOptions": [\n "-javaagent:D:\\Automation_Data\\STATIC\\tm-javalib-lower-runtime.jar",\n'

oldline2 = '"javaOptions": []'
newline2 = '"javaOptions": ["-javaagent:D:\\Automation_Data\\STATIC\\bin\\tm-javalib-lower-runtime.jar"]'

with open(FILE_PATH, "rt") as fin:
    with open(FILE_PATH1, "wt") as fout:
        for line in fin:
            fout.write(line.replace(oldline, newline))


with open(FILE_PATH1, "rt") as fin2:
    with open(FILE_PATH2, "wt") as fout2:
        for line in fin2:
            fout2.write(line.replace(oldline2, newline2))

os.remove(FILE_PATH)
os.remove(FILE_PATH1)
os.rename(FILE_PATH2, FILE_PATH)
