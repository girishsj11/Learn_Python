# chunk_of_data_writing_to_file

 Program takes input text file & buffersize which defines the how many bytes of program will writtens to the output text file.
 
 ### Method 1
 
The program will only writes the 'buffersize' bytes of data from 'infile' to 'outfile',
    to cross verify you can check the size of both 'infile' and 'outfile' files.
    
 > Example : 
 
     infile size =  2.06 MB (2167737 bytes)
     outfile size = 10 KB (10028 bytes)
        
    
 ### Method 2 
 
 The program will writes the whole content of 'infile' to 'outfile' by passing chunks of data of sizes 'buffersize',
    to cross verify once program runs , check the size of both 'infile' & 'outfile' files will be almost similar.
    
 > Example : 
 
     infile size =  2.06 MB (2167737 bytes)
     outfile size = 2.07 MB (2173433 bytes)
     counter calculation will be like = (infile size/buffersize) = (2167737/10000) = 216.7737 ~= 217
