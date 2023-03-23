class Pessoa:
    def __init__(self,nome,idade):
        self.nm = nome
        self.idade = idade
    
    def __eq__(self, other):
       if isinstance(other, Pessoa):
            return self.nm == other.nm and self.idade == other.idade
       return False
    
