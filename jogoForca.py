import random

#aqui eu vou criar uma listas de palavras 
palavras = ['palavra', 'letra', 'programação', 'desenvolvimento', 'youtube', 'jogo']


#primeira def para escolher a palavra aleatória
def escolher_palavras():
    return random.choice(palavras)


#agora vou criar uma def para verificar, sempre o status do jogo
def exibir_status(palavra, letras_corretas):
    estado = ''

    for letra in palavra:
        if letra in letras_corretas:
            estado += letra
        else:
            estado += '_' #para as letras que ainda não foram encontradas vai aparece somente o _ 
    
    return estado


#agora vou fazer a principal def do jogo
def jogar():
    palavra = escolher_palavras()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6 #total de chances que o jogador tem para acerta a palavra


    #mensagem de boas vindas ao jogo
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra escolhida tem um total de", len(palavra), "letras.")
    print("Boa sorte")

    #crio o laço de repetição para as tentivas
    while tentativas > 0:
        print("\nPalavra:", exibir_status(palavra, letras_corretas))
        print("Letras erradas:", letras_erradas)
        if tentativas == 1:
            print("Você tem somente mais 1(uma) tentativa.")
        else:
            print(f"Você tem um total de {tentativas} tentativas restantes")
        
        #agora faço o input das tentativas
        tentativa = input("Digite apenas uma letra: ").lower()

        #verificar se o input foi somente 1 letra e se realmente foi uma letra
        if (len(tentativa) != 1) or not (tentativa.isalpha()):
            print("Por favor, digite somente 1 letra")
            continue
        

        #verificar se a letra já foi inserida antes
        if (tentativa in letras_corretas) or (tentativa in letras_erradas):
            print("Você já digitou essa letra, por favor digite uma letra nova")
            continue

        #agora irie verifica se a letra está na palavra
        if tentativa in palavra:
            letras_corretas.append(tentativa)
            print(f"Nice! A letra '{tentativa}' está na palavra")
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1
            print(f"Que pena! A letra '{tentativa}' não esta na palavra")
        

        #verificar se a palavra foi totalmente descoberta
        if all(letra in letras_corretas for letra in palavra):
            print("\nParabéns voce adivinhou a palavra do jogo, a palavra era:", palavra)
            break

        #por fim se o jogador gastou todas as tentativas
        if tentativas == 0:
            print("\nNão foi dessa vez! A palavra era:", palavra)
    


jogar()