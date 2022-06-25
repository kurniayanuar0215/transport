import os
import zipfile
import datetime

now = datetime.datetime.now()
week = str(datetime.datetime.utcnow().isocalendar()[1]-1)
year = str(now.year)

fantasy_zip = zipfile.ZipFile('F:\\KY\\transport\\archive\\TRANSPORT_'+year+'_'+week+'.zip', 'w')

for folder, subfolders, files in os.walk('F:\\KY\\transport\\download'):

    for file in files:
        if file.endswith('.xlsb'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'F:\\KY\\transport\\download'), compress_type = zipfile.ZIP_DEFLATED)

fantasy_zip.close()

dir = 'F:/KY/transport/download'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

os.environ["https_proxy"] = "https://10.59.66.1:8080"
os.system("telegram-send --file F:/KY/transport/archive/TRANSPORT_"+year+"_"+week+".zip")

