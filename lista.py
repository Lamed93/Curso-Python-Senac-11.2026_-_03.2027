programadores = [
    'Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'
]
print(programadores)
# ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'] 
programadores.pop(0)
print(programadores)
# ['Juliana', 'Samuel', 'Caio', 'Luana'] ​
programadores = [
    'Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'
]
programadores.pop(5)
#obtemos o erro IndexError: pop index out of range​
programadores = [
    'Victor', 'Juliana', 'Samuel', 'Caio', 'Luana'
]
programadores.remove('Samuel')
# #Obtemos o erro ValueError: list.remove(x): x not in list, pois não existe na lista programadores um item com a string “Igor” que queremos excluir. ​
