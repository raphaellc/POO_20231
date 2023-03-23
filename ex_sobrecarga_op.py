import classe_pessoa
# Criando o array
pessoas = []

# Adicionando as instâncias
pessoas.append(classe_pessoa.Pessoa("João", 25))
pessoas.append(classe_pessoa.Pessoa("Maria", 30))
pessoas.append(classe_pessoa.Pessoa("Pedro", 20))
pessoas.append(classe_pessoa.Pessoa("Lucas", 27))
pessoas.append(classe_pessoa.Pessoa("Ana", 22))
pessoas.append(classe_pessoa.Pessoa("José", 40))
pessoas.append(classe_pessoa.Pessoa("Mariana", 35))
pessoas.append(classe_pessoa.Pessoa("Paulo", 18))
pessoas.append(classe_pessoa.Pessoa("Carla", 28))
pessoas.append(classe_pessoa.Pessoa("Felipe", 32))

pessoa = classe_pessoa.Pessoa("Raphael",40)
pessoa1 = classe_pessoa.Pessoa("Paulo",18)

for p in pessoas:
    if(pessoa == p):
        print("encontrou"+pessoa.nm)
    else:
        print("Não encontrou"+pessoa.nm)
    
