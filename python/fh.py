#file=open("sample.txt","w")
#file.write("hello this my first file")
#file.close()



#file=open("sample.txt","r")
#content=file.read()
#print(content)
#file.close()




#with open("sample.txt","a")as file:
   #file.write("\n this an appended text")





#with open("sample.txt","r")as file:
   #for line in file:
     #print(line.strip())




 
#with open("sample.txt","r")as file:
    #text=file.read()
    #words=text.split()
    #print("numbers of words:",len(words))

   
    



#with open("sample.txt","r")as source:
    #content=source.read()
#with open("copy.txt","w")as target:
    #target.write(content)    




file=open("sample.txt","r+")
print("file.read()")
file.write("\n hai")
file.close()

   
