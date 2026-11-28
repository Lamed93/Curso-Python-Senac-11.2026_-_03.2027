# Crie um programa em Python que funcione como um jogo simples de adivinhação de palavra.
# Regras do jogo:
# O programa deve definir uma palavra secreta (você pode escolher qualquer uma).
# O usuário poderá digitar apenas uma letra por vez.
# A cada tentativa, o programa deve:
#  - Verificar se a letra digitada existe na palavra secreta.
#  - Se a letra existir, exiba a palavra parcialmente revelada (mostrando as letras corretas nas posições certas e * nas demais).
#  - Se a letra não existir, exiba a palavra secreta apenas com * (sem revelar novas letras).
# O programa deve contar o número de tentativas do usuário.
# O jogo termina quando o usuário acertar todas as letras da palavra secreta.


import os 
palavra_secreta = 'casa' 
letras_acertadas = '' 
numero_tentativas = 0 
 
while True: 
    letra_digitada = input('Digite uma letra: ') 
    numero_tentativas += 1 
 
    if len(letra_digitada) > 1: 
        print('Digite apenas uma letra.') 
        continue 
 
    if letra_digitada in palavra_secreta: 
        print(palavra_secreta)
        letras_acertadas += letra_digitada 
 
    palavra_formada = '' 
    for letra_secreta in palavra_secreta: 
        if letra_secreta in letras_acertadas: 
            print('Letra encontrada:', letra_secreta)
            palavra_formada += letra_secreta 
        else: 
            palavra_formada += '*'
            print('Palavra formada:', palavra_formada) 
    if palavra_formada == palavra_secreta: 
        os.system('clear') 
        print('VOCÊ GANHOU!! PARABÉNS!') 
        print('A palavra era', palavra_secreta) 
        print('Tentativas:', numero_tentativas) 
        letras_acertadas = '' 
        numero_tentativas = 0 