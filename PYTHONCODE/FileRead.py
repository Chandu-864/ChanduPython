from pathlib import Path
filename = Path('Filesread/Python_learn.txt')
content = filename.read_text()
lines = content.splitlines()
New_content = content.replace('python','Anaconda')
Mylist = ''
for line in lines:
    Mylist += line.strip()
    print(Mylist)
    print(len(Mylist))
print((New_content))
print(content)
