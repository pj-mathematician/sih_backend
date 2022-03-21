import pyimgur
import os
CLIENT_ID = "18249260aac26ae"
im = pyimgur.Imgur(CLIENT_ID)
# links = []
data = {}
l = ['Cars', 'Indian Food', 'Pets']
for i in l:
    data[i] = {}
    m = os.listdir(i)
    for j in m:
        data[i][j] = []
        for k in os.listdir(i+'/'+j):
            print(i + '/' + j + '/' + k)
            data[i][j].append(im.upload_image(i+'/'+j+'/'+k).link)
with open('data.txt', 'w') as f:
    f.write(str(data))

