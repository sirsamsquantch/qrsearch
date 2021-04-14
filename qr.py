import cv2
from os import walk

files = []

for (dirpath, dirnames, filenames) in walk('.'):
	files = filenames

for file in files:
	try:
		img = cv2.imread(file)
		detector = cv2.QRCodeDetector()
		data, bbox, straight_qrcode = detector.detectAndDecode(img)
		
		if len(data) > 0:
			print('Data found in '+file+': '+data)
	except:
		print('error: '+file)