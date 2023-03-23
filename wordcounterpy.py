from os import path, getcwd, listdir, chdir
import natsort as nsrt

# file = path.join() # path sirve para agregar el separador correcto de cada SO

def where():
    w = getcwd()
    return print(w), nsrt.natsorted(listdir(w))

where()

chdir('../')
where()


def get_lines(phrase, file):
    var = list()
    with open(file, 'r', encoding='utf8') as f:
        for word in f.readlines():
            if phrase in word:
                var.append(word)

    return var



lines = get_lines('capitulos', 'main.tex')

lines


paths = [ele.strip().replace('% ','').replace('\\include{','').replace('}','') for ele in lines]
pathswext = [i+'.tex' for i in paths]
pathswext
