with open("vegetables.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.write("\n"+content)
    myfile.write("\n"+content)
