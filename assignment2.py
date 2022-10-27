import docx2txt
my_text = docx2txt.process("demo.docx")
arr=my_text.split(" ")
eachArr=list(set(arr))
sentence=len(my_text.split("."))

def wordOccur(word):
    return my_text.count(word)

print("The number of sentence present in .docx file is:",sentence,"\n")


# print(eachArr)
for i in range(len(eachArr)):
    print(f"The word '{eachArr[i]}' is present in the .docx file is:",wordOccur(eachArr[i]))