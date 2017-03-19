# report from monna lisa 3d image
2017.3.19
well... this is a (sub)project form Computer Vision Course
and from now Im justing trying to use python fliter the [red] and [cyan] channel.
i check [Photoshop 3d image tutorial] on youtube, and seems THIS would be a solution for this project.

just, use python read pixels values from image file,
and form that pick out [RED] and [GREEN & BLUE] channels' value,
after that just make some shift in width (horizonal) position, like 3, 5 pixels.
and so, that we would get the (so called) 3D image we want... tabunn

and there is still some promble or keng, that i have met on ths program.
first, check how to manipulate pixels from image in python, like..emm....Image from PIL, 

	img = Image.open(file)
	img.load(pixels)
	pixels[x, y] = (r, g, b)

**NOTATION:**
the 'pixels' value is PixelsAccess format, and if want to access the value should use [x, y]
not [x][y]!
and, the value is Tuple format, cant not be changed its single value, must change all if want

mean while, the processing is really, slow....

so here still have some problem... can we use Depth-map to manipulate these image?
well, we ll c if more work can be carred on...
