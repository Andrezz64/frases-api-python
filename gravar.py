def WriteData(frase):
    print(frase)
    arquivo = open("LocalStorege.txt", "a", encoding="utf8") 
    frase
    arquivo.write(f'\n {frase}')
    return print("arquivo cadastrado")



