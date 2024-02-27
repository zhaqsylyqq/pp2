import re
txt = open('row.txt')
#--------------------------------- 1
def a_or_ab(txt):
    patt = "^a(*b)$"
    res = re.findall(patt, txt)
    return res
#--------------------------------- 2
def a_or_ab(txt):
    patt = "ab{2, 3}"
    res = re.findall(patt, txt)
    return res
#--------------------------------- 3
def a_or_ab(txt):
    patt = "^[a-z]+_[a-z]+$"
    res = re.findall(patt, txt)
    return res
#--------------------------------- 4
def a_or_ab(txt):
    patt = "^[A-Z][a-z]+&"
    res = re.findall(patt, txt)
    return res
#--------------------------------- 5
def a_or_ab(txt):
    patt = "^a.*?b&"
    res = re.findall(patt, txt)
    return res
#--------------------------------- 6
def a_smth_b(txt):
    x = re.sub("[ .,]" ,":", txt)
    return x
#--------------------------------- 7
def snake_to_camel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
#--------------------------------- 8
def split_by_upper(txt):
    return re.findall("[A-Z][^A-Z]*", txt)
#--------------------------------- 9
def space_between_capital(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
#--------------------------------- 10
def camel_to_snake(txt):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',re.sub('([A-Z]+)', r' \1',txt.replace('-', ' '))).split()).lower()