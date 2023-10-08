import cv2 # pip install opencv-python

img = cv2.imread('captcha1.jpg', cv2.COLOR_BGR2RGB) # png error !

y_len = img.shape[0] #length in first dimension
x_len = img.shape[1] #length in second dimension

# print(x_len, y_len)
# print(img)

cv2.imshow("Img", img)

RTH = lambda x : '#%02x%02x%02x' % x # RTH - RgbToHex;

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
# rgb_to_hex((255, 255, 195))

print(img)

print(tuple(img[1][1]))

print(rgb_to_hex(tuple(img[1][1])))

'''
for i in range(0, int(x_len / 100)):
   for j in range(0, int(y_len / 4)):
        print(img[i][j])             #<---this is value of single pixel
'''
'''
imgH = [0] * x_len
for i in range(x_len):
   imgH[i] = [map(lambda pixel: RTH(tuple(pixel)), img[i])]
   )'''

print(imgH)


# https://stackoverflow.com/questions/39549545/split-image-into-pixelscolumns
