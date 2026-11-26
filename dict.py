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