from modulo import multiplicar

#Crio a função
def saudacao(nomes_alunos):
    for nome in nomes_alunos:
        print(f"Olá,{nome}. Bem-vindo(a) a aula de Python no Senac.")

lista_alunos = ["Lucas","Marcelo","João","Carol","Enzo","Guilherme","Gabriel"]
saudacao(lista_alunos)


def somar(numero1,numero2):
    return numero1 + numero2

total = somar(2,2)
print("A soma é: ",total)
total2 = somar(5,5)
print("A soma de total2 é: ",total2)

resultado_modulo = multiplicar(5,5)
print(resultado_modulo)



