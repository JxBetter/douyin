import numpy
from sys import argv
from PIL import Image

def covert_pic():
    picpath = argv[1]
    pic_data = Image.open(picpath)
    array_data = numpy.array(pic_data)
    array_red = numpy.copy(array_data)
    array_red[:,:,1:3] = 0
    array_gb = numpy.copy(array_data)
    array_gb[:,:,0] = 0
    img_red = Image.fromarray(array_red)
    img_gb = Image.fromarray(array_gb)
    bk1 = Image.new("RGB", pic_data.size, color=(0, 0, 0))
    bk1.paste(img_red, (11, 11), mask=img_red.split()[0])
    bk2 = Image.new("RGB", pic_data.size, color=(0, 0, 0))
    bk2.paste(img_gb, (0, 0), mask=img_gb.split()[1])
    res_array = numpy.array(bk1) + numpy.array(bk2)
    res = Image.fromarray(res_array)
    res.show()
    res.save(r'F:\dy.jpg')

if __name__ == '__main__':
    covert_pic()