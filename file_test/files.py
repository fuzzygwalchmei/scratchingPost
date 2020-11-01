import os


def create_file(filename):
    if not filename in os.listdir():
        open(filename,'x')



def open_file():
    pass


def read_file(filename):
    with open(filename,'r') as f:
        file = f.read()
    file=file.split('\n')
    return(file)



def write_file(filename, new_text):
    with open(filename, 'a+') as f:
        f.write(new_text)

