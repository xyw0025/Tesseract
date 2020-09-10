The file `chi_tra_TRAIN.traineddata` should be put under path /usr/local/share/tessdata/ , etc.  
If it's installed succesfully, chi_tra_TRAIN can be seen using command "tesseract --list-langs".  


### to run:  

python testTesseract.py -i [input_files_folder_path] -f [output_format(xml, txt)]
	
```
ex: 
	python testTesseract.py -i input_data_example/ -f xml
```

It will iterate over files under specified folder.  
By default, language is chosen as chi_tra_TRAIN, the output files will be placed in ./output


