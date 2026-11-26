print("-------Lista-------")

frutas = ['maçã', 'banana', 'laranja']
frutas.append('uva')
print(frutas)


print("\n--------------------")
a = [1, 2, 3, 4]

print(a[0])

print(a[-1])

print(a[1:3]) 

a[0] = 42

print(a)

print("\n-------------------------")
a = [1, 2, 3, 4, 5]
a.append(6) #Adicionando o 6 ao final da lista
print(a)
a.insert(0, 0.0) #adicionando 0.0 na posicao 0​
print(a)
print(len(a)) # mostrar o num. de elementos da lista 7 ​
a[2:4] = [5.0, 5.0] #Modificar trecho da lista ​
print(a)

print("\n----------------------")
a = [1, 2, 3]

b = a

print(b)
b[0] = 42
print(a) 

c = a[:]
print(c)

c[0] = 0
print(c)

print(a)

print("\n----------------------")
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio','Luana']
print(type(programadores)) # type ‘list’ 
print(len(programadores)) # 5 ​
print(type(programadores)) # type ‘list’ ​

print(len(programadores)) # 5 ​

print(programadores[4]) # Luana ​

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

print(programadores)
# ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'] ​

programadores[1] = 'Carolina'

print(programadores)
# ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana'] ​
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

print(programadores)
# ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana 
programadores.append('Renato') 
print(programadores)
# ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato'] programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'] ​

programadores.insert(1, 'Rafael') 
print(programadores)
# ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']​
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

print(programadores)
# ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'] programadores.pop(0) ​

print(programadores)
# ['Juliana', 'Samuel', 'Caio', 'Luana'] ​

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
#programadores.pop(5)
#obtemos o erro IndexError: pop index out of range​

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

programadores.remove('Igor')
#Obtemos o erro ValueError: list.remove(x): x not in list, pois não existe na lista programadores um item com a string “Igor” que queremos excluir. ​

aluno = ['Murilo', 19, 1.79]
# Nome, idade e altura ​

print(type(aluno)) # type 'list' ​

print(aluno) # ['Murilo', 19, 1.79]​

dados_cliente = { 'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645' } 
print(dados_cliente) 
# {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645'} 
dados_cliente.pop('Telefone', None) 
print(dados_cliente) 
# {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul'}
dados_cliente = { 'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645' }
print(dados_cliente) 
# {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645'} 
del dados_cliente['Telefone']
print(dados_cliente)