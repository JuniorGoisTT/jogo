import random

def jogo_adivinhe_o_numero():
    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        tentativa = input("Digite sua tentativa (ou 'sair' para encerrar): ")
        
        if tentativa.lower() == 'sair':
            print(f"Você desistiu. O número secreto era {numero_secreto}.")
            break
        
        if not tentativa.isdigit():
            print("Por favor, digite um número válido.")
            continue
        
        tentativa = int(tentativa)
        tentativas += 1
        
        if tentativa < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhe_o_numero()
