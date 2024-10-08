# 1 - IMPORTAR BIBLIOTECA PARA GERAR NUMEROS ALEATÓRIOS
import random


# 2 - CRIAR FUNÇÃO GERA UM NUMERO ALEATORIO ENTRE 1 E 100
def adivinhar_numero():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    acertou = False
 # 3 - CRIAR TITULO PARA O APP   
    print("Bem-vindo ao jogo de Adivinhação!")
    print("Existe um número escondido entre 1 e 100. Tente adivinhar!")

 # 4 - CRIAR LOOP ATÉ O JOGADOR ADVINHAR O NÚMERO
    while not acertou:
        palpite = int(input("Digite um número: "))
        tentativas += 1

        if palpite < numero_aleatorio:
            print("O número é maior do que isso.")
        elif palpite > numero_aleatorio:
            print("O número é menor do que isso.")
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número |{numero_aleatorio}| em {tentativas} tentativas.")

 # 5 - CHAMAR A FUNCAO PARA INICIO DO JOGO
adivinhar_numero()
           
