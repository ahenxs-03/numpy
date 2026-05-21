import numpy as np
# a=np.array([1,2,3])
# print(a+5)
from PIL import Image
import matplotlib.pyplot as plt

img=Image.open("images/cat.jpg")
print(type(img))
print(np.shape(img))
print(type(img))

im=np.array(img)
print(type(im))
print(im.shape)
# im2=im.reshape(256,)
# plt.imshow(im)
# plt.show()
#print(im)
# for i in range(256):
#     if i%2==0:
#         im[i]=i
#     else:
#         im[i]=i
#print(im)
im[0][0]=[100,0,0]
print(im[0][0])
for i in range(100):
    for j in range(70):
        im[i][j]=(i,j,i+j)
im[440][415]=(67,89,52)
im[440][416]=(67,89,52)
im[440][417]=(67,89,52)
im[440][418]=(67,89,52)
im[440][415]=(67,89,52)
im[441][416]=(67,89,52)
im[442][417]=(67,89,52)
im[443][418]=(67,89,52)

plt.imshow(im)
plt.show()
