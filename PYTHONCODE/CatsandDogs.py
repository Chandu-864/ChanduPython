from pathlib import Path
file1 = Path('Filesread/Dogs.txt')
file2 = Path('Filesread/Cats.txt')

try:
    content1 = file1.read_text()
    content2 = file2.read_text()
    message1 = content1.split('\n')
    message2 = content2.split('\n')
    
except FileNotFoundError:
    print("There is no such file in that directory. Make sure to give the correct file name and location")
else:
    print("The dog names are",message1,"and the Cat names are",message2)