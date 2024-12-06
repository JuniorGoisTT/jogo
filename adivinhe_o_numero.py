import random

def selecionar_dificuldade():
    print("Selecione o nível de dificuldade:")
    print("1 - Fácil (número entre 1 e 50, tentativas ilimitadas)")
    print("2 - Médio (número entre 1 e 100, máximo de 10 tentativas)")
    print("3 - Difícil (número entre 1 e 200, máximo de 7 tentativas)")
    
    while True:
        escolha = input("Escolha o nível (1, 2 ou 3): ")
        if escolha in ["1", "2", "3"]:
            return int(escolha)
        print("Escolha inválida. Por favor, digite 1, 2 ou 3.")

def configurar_jogo(dificuldade):
    if dificuldade == 1:
        return 50, None  # Intervalo de 1 a 50, tentativas ilimitadas
    elif dificuldade == 2:
        return 100, 10  # Intervalo de 1 a 100, máximo de 10 tentativas
    elif dificuldade == 3:
        return 200, 7  # Intervalo de 1 a 200, máximo de 7 tentativas

def jogo_adivinhe_o_numero():
    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    
    dificuldade = selecionar_dificuldade()
    intervalo, max_tentativas = configurar_jogo(dificuldade)
    numero_secreto = random.randint(1, intervalo)
    
    print(f"Estou pensando em um número entre 1 e {intervalo}.")
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
        
        if max_tentativas and tentativas >= max_tentativas:
            print(f"Você excedeu o número máximo de {max_tentativas} tentativas. O número era {numero_secreto}.")
            break

if __name__ == "__main__":
    jogo_adivinhe_o_numero()
