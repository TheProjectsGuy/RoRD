# Generate rtImagesRgb.csv
r"""
	python .\getRTImages.py "C:\Users\123av\Downloads\Datasets\DiverseView\preprocessed\data1\rgb"
"""

import os
import re
import glob
from sys import argv, exit
import csv
import numpy as np


def natural_sort(l): 
	convert = lambda text: int(text) if text.isdigit() else text.lower() 
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
	return sorted(l, key = alphanum_key)


def getPairs(imgs):
	queryIdxs = np.linspace(start=0, stop=len(imgs)-1, num=10).astype(int).tolist()
	databaseIdxs = np.linspace(start=10, stop=len(imgs)-10, num=100).astype(int).tolist()

	queryImgs = [imgs[idx] for idx in queryIdxs]
	databaseImgs = [imgs[idx] for idx in databaseIdxs]
	
	return queryImgs, databaseImgs


def writeCSV(qImgs, dImgs):
	with open('rtImagesRgb.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		
		title = []
		title.append('query')

		for i in range(len(dImgs)):
			title.append('data' + str(i+1))

		writer.writerow(title)

		for qImg in qImgs:
			row = []
			row.append(qImg)

			for dImg in dImgs:
				row.append(dImg)

			writer.writerow(row)


if __name__ == '__main__':
	rgbDir = argv[1]
	rgbDir = os.path.realpath(rgbDir)
	file_list = glob.glob(f"{rgbDir}/*.jpg")	# Only JPG images
	rgbImgs = natural_sort([file for file in file_list])
	rgbImgs = [os.path.join(rgbDir, img) for img in rgbImgs]
	# print(f"{rgbImgs}")
	# raise NotImplementedError("Hold")
	queryImgs, databaseImgs = getPairs(rgbImgs)
	# print(f"Query: {len(queryImgs)}")
	# print(f"\n\nDatabase: {len(databaseImgs)}")
	# raise NotImplementedError("Hold")
	writeCSV(queryImgs, databaseImgs)
