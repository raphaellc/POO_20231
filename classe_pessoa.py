
class Pessoa:
    def __init(self,nome,idade):
        self.nm = nome
        self.idade = idade
    
    def __eq__(self, other):
       if isinstance(other, Pessoa):
            return self.nome == other.nome and self.idade == other.idade
       return False