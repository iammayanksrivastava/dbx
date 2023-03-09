file = 'testfile.txt'
newfile = 'newtestfile.txt'

def readfile(): 
    with open(file, mode='r') as f: 
        lines = f.read()
        print(lines)
        f.close()


def appendfile(): 
    with open(file, mode='a') as f: 
        f.writelines('\nThis is the fifth line')
        f.close()



def appendfile(): 
    with open(newfile, mode='w') as f: 
        f.write('\nThis is the new line')
        f.close()



appendfile()
readfile()
appendfile()