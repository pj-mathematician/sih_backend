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
    links = []
    for j in m:
        data[i][j] = []
        links = []
        for k in os.listdir(i+'/'+j):
            print(i + '/' + j + '/' + k)
            links.append(im.upload_image(i+'/'+j+'/'+k).link)
            data[i][j].extend(links)
print(data)
with open('data.txt', 'w') as f:
    f.write(str(data))

