# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:03:38 2020
@author: giri
"""

#method 1
'''
The below program will only writes the 'buffersize' bytes of data from 'infile' to 'outfile'.
to cross verify you can check the size of both 'infile' and 'outfile' files.
Ex: 
	infile size =  2.06 MB (2167737 bytes)
	outfile size = 10 KB (10028 bytes)
	buffersize = 10000
'''
infile = "large_text.txt"
outfile = "large_text_with_chunk_data.txt"
buffersize = 10000 

with open(infile,"r") as file_i:
    with open(outfile,"w") as file_o:
        data_buffer = file_i.read(buffersize) #reading chunk of data from input file & storing in variable
		file_o.write(data_buffer) #writing a chunks of data to the output file
        print("Writing to a file is done !....")
	
	

	
	
#method 2
'''
The below program will writes the whole content of 'infile' to 'outfile' by passing chunks of data of sizes 'buffersize'
to cross verify once program runs , check the size of both 'infile' & 'outfile' files will be same.
Ex: 
	infile size =  2.06 MB (2167737 bytes)
	outfile size = 2.07 MB (2173433 bytes)
	buffersize = 10000
	counter calculation will be like = (infile size/buffersize) = 216.7737 ~= 217
'''
infile = "large_text.txt"
outfile = "large_text_copy.txt"
buffersize = 10000

with open(infile,"r") as file_i:
    with open(outfile,"w") as file_o:
        data_buffer = file_i.read(buffersize)
        counter = 0
        while len(data_buffer):
            file_o.write(data_buffer)
            data_buffer = file_i.read(buffersize) #to showcase when databuffer hits the last data of input file , then it becomes empty, so loop exits.
            counter+=1 #to have count to reach the last item/data of inputfile
        print("{} times the chunk of data is written to new file ".format(counter))
        print("Writing to a file is done !....")
