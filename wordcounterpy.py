from os import path, getcwd, listdir, chdir
import natsort as nsrt

# file = path.join() # path sirve para agregar el separador correcto de cada SO

def where():
    w = getcwd()
    return print(w), nsrt.natsorted(listdir(w))

where()

chdir('../')
where()

with open('main.tex', 'r', encoding='utf8') as file:
    first = file.readline()
    print(first)

def get_numberline(phrase, file):
    with open(file, 'r', encoding='utf8') as f:
        for i, line in enumerate(f):
            if phrase in line:
                return i+1

get_numberline('capitulos', 'main.tex')
