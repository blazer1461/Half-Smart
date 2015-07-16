__author__ = 'blazer1461'
def read_file (fname):
    f= open(fname)
    s= f.read()
    f.close()
    return s

def get_csv_dict(fname):
    c = {}
    lines = read_file(fname).split("\n")
    for row in lines:
        r= row.split(",")
        c[r[0]]= r[1:]
    return c
def get_csv_list(fname):
    z= []
    lines = read_file(fname).split("\n")
    for object in lines:
        s= object.split(",")
        z.append(s)
    return z
if __name__ == "__main__":
    text = read_file('CSTUY_words.csv')
    lines = get_csv_list('CSTUY_words.csv')
    dict= get_csv_dict('CSTUY_words.csv')
    print text
    print lines
    print dict
    print ("\n")
