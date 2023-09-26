
# Creating an output file in writing mode
output_file = open("Write_into.txt", "w",encoding='utf-8')
  
# Opening input file and scanning each line
# from input file and writing in output file
with open("Read_from.txt", "r",encoding='utf-8') as scan:
    output_file.write(scan.read())
  
# Closing the output file
output_file.close()