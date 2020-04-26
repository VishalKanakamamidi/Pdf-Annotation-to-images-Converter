from pdf2image import convert_from_path
import PIL
from PIL import Image 
import cv2, numpy
pages = convert_from_path('Dec.pdf',size=700)
key = 0
for page in pages:
	print(type(page))
	open_cv_image = numpy.array(page)
	open_cv_image = open_cv_image[:, :, ::-1].copy() 
	
	while(1):
		r = cv2.selectROI("page", open_cv_image, fromCenter=False,
			showCrosshair=True)
		print(r)
		if r == (0,0,0,0):
			break
		imCrop = open_cv_image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
		text = input("What is the annotation name ? ")
		cv2.imwrite("Annotations//"+text+".jpg",imCrop)
