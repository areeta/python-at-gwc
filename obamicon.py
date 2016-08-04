#You can get a similar effect if you look at each pixel’s RGB, or red green blue, values. RGB values work like light. 
#If a color has high values for all three colors, it is close to white. If there are low values, it’s close to black. 
#If you add all the values together, you get a number that correlates to how “light” the color is. Lighter colors get colorized yellow. 
#Medium/light colors get coded as light blue. Medium/dark colors are red and very dark colors get coded as dark blue.

#Get the intensity of each pixel by adding the red, green and blue values.
#If the pixel has low intensity (<182) color it  dark blue.
#If the pixel is medium/low intensity (between 182 and 364) color it red.
#If the pixel is medium/high intensity (between 364 and 546) color it light blue.
#If the pixel is high intensity (>546) color it yellow.
#The RGB codes for the colors are as follows:

#Note: you must run this program from the same directory (folder) as the image file OR call the file using an absolute path. 
#The output.jpg file will be stored in the same folder.

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)


from PIL import Image

im = Image.open("winning.jpg")

colorpixels = list(im.getdata())
list_length=len(colorpixels)


for i in range(list_length):
	#print(i)
	redapples = colorpixels[i][0]
	blueapples = colorpixels[i][1]
	greenapples = colorpixels[i][2]
	sum = redapples + blueapples + greenapples
	
	print(sum)
	if sum < 182:
		colorpixels[i] = darkBlue
	elif sum >= 182 and sum < 364:
		colorpixels[i] = red
	elif sum >= 364 and sum< 546:
		colorpixels[i] = lightBlue
	else:
		colorpixels[i]= yellow 
		
		
im.putdata(colorpixels)

im.show()


	
	