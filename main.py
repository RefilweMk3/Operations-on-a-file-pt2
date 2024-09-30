with open("ref.txt","w") as f:
    f.write("Hello there \n how are u doing today")
f.close
with open("ref.txt","r")as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)
f.close()

#file=open("kg.txt","x")
#file.write("sample file")
#file.close()

import os
#os.remove("kg")
os.rmdir("kg")