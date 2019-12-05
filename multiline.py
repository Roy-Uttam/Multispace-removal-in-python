import re
with open('multiline.txt',"r") as f:
    data = f.read()
    data = re.sub('\s{2,}', ' ',data)
    data = re.sub('\n', ' ',data)
with open('multiline-out.txt', "w") as f:
    f.write(data)