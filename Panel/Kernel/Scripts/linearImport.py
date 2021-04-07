
with open('/home/venom/links.txt','r') as reader:
    content = reader.read()
    if '\n' in content:
        Lines = content.split('\n')
        for line in Lines:
            print("FOUND "+line)