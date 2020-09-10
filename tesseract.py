import pytesseract
from argparse import ArgumentParser 
import xml.etree.cElementTree as ET
import os

output_path = "./output/"
config="./config_set"
# What the file config_set does here is to remove all the spaces between every character in the output

def read_image_to_data(folder_path, filename, format="xml", lang="chi_tra_TRAIN"):
	output_name = filename.split('.')[0]
	if format == "xml":
		output_name += ".xml"
		output_file = pytesseract.image_to_alto_xml(folder_path, lang=lang, config=config)
		with open(output_path + output_name, 'w+b') as f:
			f.write(output_file)
	elif format == "txt":
		output_name += ".txt"
		output_file = pytesseract.image_to_string(folder_path, lang=lang, config=config)
		with open(output_path + output_name, 'w') as f:
			f.write(output_file)
	else:
		print("error: output format as .xml or .txt")
		return
	print("-" *5 + filename, "reading images to", format ) 



if __name__ == '__main__':
	
	parser = ArgumentParser()
	parser.add_argument("-i", "--input_file", dest="input_path")
	parser.add_argument("-f", "--format", dest="format")
	args = parser.parse_args()
	path = args.input_path
	format = "txt"
	if args.format != None:
		format = args.format

	for file in os.listdir(path):
		filename = os.fsdecode(file)
		if filename.endswith(".png") or filename.endswith(".jpg"):
			read_image_to_data(path+filename, filename, format)