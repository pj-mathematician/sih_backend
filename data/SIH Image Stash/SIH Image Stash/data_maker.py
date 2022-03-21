import pyimgur
import os
CLIENT_ID = "00f3771c2e933ea"
im = pyimgur.Imgur(CLIENT_ID)
# links = []
data = {}
l = ['Cars', 'Indian Food', 'Pets']
iter = 0
for i in l:
    data[i] = {}
    m = os.listdir(i)
    for j in m:
        data[i][j] = {}
        for k in os.listdir(i+'/'+j):
            print(i + '/' + j + '/' + k)
            data[i][j]["image_{}".format(iter)] = im.upload_image(i + '/' + j + '/' + k).link
with open('data.txt', 'w') as f:
    f.write(str(data))

