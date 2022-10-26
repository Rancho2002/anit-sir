import docx2txt
my_text = docx2txt.process("demo.docx")
sentence=len(my_text.split("."))
def wordOccur(word):
    return my_text.count(word)
print("The number of sentence present in .docx file is:",sentence)
target=input("Which word you want to find? ")
print(f"The number {target} is present in the .docx file is:",wordOccur(target))