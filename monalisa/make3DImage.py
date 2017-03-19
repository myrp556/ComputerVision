import sys
import copy
from PIL import Image
import numpy as np
import os
import scipy.misc as smp

def setPixel2(pixels, r, g, b, width, height):
	for i in range(width):
		for j in range(height):
			vr = r if r >= 0 else pixels[i, j][0]
			vg = g if g >= 0 else pixels[i, j][1]
			vb = b if b >= 0 else pixels[i, j][2]
			pixels[i, j] = (vr, vg, vb)

def copy_pixel(src, width, height):
	res = np.zeros((width, height, 3), dtype=np.uint8)

	for i in range(width):
		for j in range(height):
			res[i, j] = src[i, j]
	return res

def get_pixel(src, x, y, width, height):
	if x < 0 or x >= width:
		return (0, 0, 0)
	if y < 0 or y >= height:
		return (0, 0, 0)
	return src[x, y]

def add_pixel(pix1, pix2):
	return (pix1[0] + pix2[0], pix1[1] + pix2[1], pix1[2] + pix2[2])

def make_image(red, cyan, l, width, height):
	res = np.zeros((height, width-l*2, 3), dtype=np.uint8)
	a = 0
	b = 0
	for i in range(width-l*2):
		for j in range(height):
			#res[i, j] = add_pixel(get_pixel(red, i, j-l, width, height), get_pixel(cyan, i, j+l, width, height))
			red_val = get_pixel(red, i+2*l, j, width, height)
			cyan_val = get_pixel(cyan, i, j, width, height)
			#cyan_val = (0, 0, 0)	
			res[j, i] = (red_val[0]+cyan_val[0], red_val[1]+cyan_val[1], red_val[2]+cyan_val[2])
			#print red_val, cyan_val, res[j, i]
	return smp.toimage(res)


def show_insc():
	print '''python make3DImage.py [instrctions]
-f [file name]:\t*NEEDED input image file name.
-o [file name]:\t*OPTIONAL output image file name. default is res.png
-l [length]:\t*OPTIONAL render length between red and cyan channels. default is 5.'''

if __name__ == '__main__':
	file_name = 0
	save_name = 'res.png'
	l = 5

	if len(sys.argv) < 1:
		show_insc()
	else:
		i = 1
		while i+1 < len(sys.argv):
			if sys.argv[i] == '-f':
				file_name = sys.argv[i+1]
				i += 2
				continue
			elif sys.argv[i] == '-o':
				save_name = sys.argv[i+1]
				i += 2
				continue
			elif sys.argv[i] == '-l':
				l = int(sys.argv[i+1])
				i += 2
				continue
			i += 1

		if file_name == 0:
			show_insc()
		else:
			#file_name = sys.argv[1]
			print 'input file %s' % file_name
			if not os.path.exists(file_name):
				print 'input [%s] file does not exist.' % file_name
			else:
				im = Image.open(file_name) #Can be many different formats.
				pix = im.load()
				
				(width, height) = im.size
				#print pix[0, 0] #Get the RGBA Value of the a pixel of an image
				#pix[x,y] = value # Set the RGBA Value of the image (tuple)
				#im.save("alive_parrot.png") # Save the modified pixels as png
				print 'width: %d height: %d' % (width, height)
				print 'pixel length: %d' % l
				red = []
				cyan = []
				print 'loading red channel...'
				red = copy_pixel(pix, width, height)
				setPixel2(red, -1, 0, 0, width, height)
				print 'loading cyan channel...'
				cyan = copy_pixel(pix, width, height)
				setPixel2(cyan, 0, -1, -1, width, height)
				
				#setPixel2(pix, -1, 0, 0, width, height)
				print 'making 3d image...'
				res = make_image(red, cyan, l, width, height)
				print 'saved to [%s]' % save_name
				res.save(save_name)
				res.show()
				#im.show()