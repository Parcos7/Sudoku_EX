import random

sudoku = [[random.randint(1, 9) if random.randint(0, 1) == 1 else 0 for _ in range(9)] for _ in range(9)]

def imagem():
    for i in sudoku:
        print()
        for j in i:
            print(f"{[j]}", end="")

def testeImg():
    for linha in range(len(sudoku)):
        for coluna in range(len(sudoku[linha])):
            valor = sudoku[linha][coluna]
            if valor == 0:
                return True
    return False

def preencher(escolha, escolha2):
    valor = sudoku[escolha][escolha2]
    if valor == 0:
        x = int(input(f"\nEscolha o numero de 1 a 9: "))
        sudoku[escolha][escolha2] = x
        imagem()

def testeValidar(sudoku):
    def validar(lista):
        return set(lista) == set(range(1,10))
    
    for linha in sudoku:
        if not validar(linha):
            return False
    
    for coluna in range(9):
        coluna = [sudoku[linha][coluna] for linha in range(9)]
        if not validar(coluna):
            return False

    for i in sudoku:
        for j in range(9):
            subclasse = [
            sudoku[x][y] 
            for x in range(i, i + 3)
            for y in range(j, j + 3) 
            ]
            if not validar(subclasse):
                return False
    return True

imagem()

while testeImg() == True:
    escolha, escolha2 = map(int, input("\n\nEscolha a Linha e Coluna: ").split())
    preencher(escolha, escolha2)
    testeImg()

#OBS sei que vai a maior parte das vezes invalido, estou no processo de corrigir
if testeValidar(sudoku) == True:
    print("Sudoku VALIDO!")
else:
    print("Sudoku INVALIDO!")
