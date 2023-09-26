# Taking "gfg input file.txt" as input file
# in reading mode
with open("Read_from.txt", "r") as input:
      
    # Creating "gfg output file.txt" as output
    # file in write mode
    with open("Write_into.txt", "w") as output:
          
        # Writing each line from input file to
        # output file using loop
        for line in input:
            output.write(line)