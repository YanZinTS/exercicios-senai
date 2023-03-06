import random

dnvo = "s"

while dnvo == "s":
    
    print( "Escolha um nível:\n 3- Fácil\n 2- Médio\n 1- Difícil: ")
    niveis = int(input("Digite qual o número do nivel: "))

    chances = niveis * 5

    arvores = random.randrange (0,50)
    while chances > 0:
        print("Você possui " + str(chances) + " tentativas")
        tentativas= int(input("Digite um número: "))
        
        if tentativas > arvores:
            print("Está em uma árvore de número menor")
            chances -= 1
        elif tentativas < arvores:
            print("Está em uma árvore de número maior")
            chances -= 1
        else:
            print("Acertou")
            chances = 0
            break
        
    dnvo = input("\nDeseja jogar novamente? (s/n): ")