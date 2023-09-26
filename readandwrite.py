o = open("Write_into.txt", "w",encoding='utf-8')
i = open("Read_from.txt", "r",encoding='utf-8')
o.write(i.read())
o.close()