def total():
    arquivo = open("LocalStorege.txt", "r", encoding="utf8")
    frases = arquivo.readlines()
    for frases in arquivo:
        continue

    frasesTotal = len(frases)
    frasestotaReal = frasesTotal -1 
    return frasestotaReal

total()