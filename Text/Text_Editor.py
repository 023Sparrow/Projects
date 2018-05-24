
def open():
    pass

def edit():
    pass

def save():
    with open("test.txt","rt") as f:
        data = f.read()
    print('文件名：',data)
    
save()
