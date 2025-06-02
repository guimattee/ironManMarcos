


telefones = {
    'joao': '1234',
    'maria': '5678'
}

telefones['lucas'] = '90123' #adiciona itens na lista


busca = input("digite o nome: ").lower()

print(telefones.get(busca, 'nome não encontrado')) #mensagem de erro

