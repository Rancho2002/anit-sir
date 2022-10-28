import docx2txt
my_text = docx2txt.process("demo.docx")
my_text= my_text.lower()

sentence=(my_text.split("."))
# print(sentence)
print("The number of sentence present in .docx file is:",len(sentence)-1,"\n")


# Ommiting the full stops and others punction marks, the new lines and creating a fresh paragraph
l=[]
for i in range(len(my_text)):
    if((ord(my_text[i])>=65 and ord(my_text[i])<=90) or (ord(my_text[i])>=97 and ord(my_text[i])<=122) or my_text[i]==' '):
        l.append(my_text[i])
s="".join(l)



# creating the word array separated by spaces
arr=s.split(" ")

#taking the unique words
eachArr=list(set(arr))

#just return ocurrence of any word inside a string
def wordOccur(word):
    return s.count(word)

# print(eachArr)
for i in range(len(eachArr)):
    print(f"The word '{eachArr[i]}' is present in the .docx file is:",wordOccur(eachArr[i]))