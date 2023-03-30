"""Um exemplo de código utilizando herança e polimorfismo em um jogo de RPG pode ser a criação de classes de personagens que herdam atributos e métodos de uma classe base "Personagem". Por exemplo, podemos criar as classes "Guerreiro", "Mago" e "Arqueiro" que herdam os atributos básicos de "Personagem", como nome, vida e mana.

Além disso, podemos utilizar o polimorfismo para criar habilidades únicas para cada classe de personagem. Por exemplo, a classe "Guerreiro" pode ter uma habilidade de ataque corpo a corpo, enquanto o "Mago" pode ter uma habilidade de lançar feitiços mágicos e o "Arqueiro" pode ter uma habilidade de ataque à distância. Essas habilidades podem ser implementadas como métodos nas classes de personagem, cada um com uma implementação lógica diferente, mas todos com a mesma assinatura para permitir o polimorfismo.

Podemos ainda criar subclasses específicas de cada classe de personagem, como "Paladino" e "Bárbaro" que herdam atributos e métodos da classe "Guerreiro", mas possuem habilidades únicas implementadas por meio de polimorfismo"""

class Personagem:
    def __init__(self, nome, vida, mana):
        self.nome = nome
        self.vida = vida
        self.mana = mana

class Guerreiro(Personagem):
    
    def ataque_corpo_a_corpo(self):
        # Implementação do ataque corpo a corpo do guerreiro
        print("Guerreiro Atacando corpo a corpo")
    
class Mago(Personagem):
    def __init__(self):
        self.mana = 10

    def lancarFeitico(self):
        # Implementação do lançamento de feitiço do mago
        self.mana =- 1
        print("Mago Lança feitiço")

class Arqueiro(Personagem):

    def ataque_a_distancia(self):
        # Implementação do ataque à distância do arqueiro
        print("Arqueiro Atacando")

class Paladino(Guerreiro):

    def cura(self):
        # Implementação da habilidade de cura do paladino
        self.mana -=2
        print("Paladino Curando")

class Barbaro(Guerreiro):

    def furia(self):
        # Implementação da habilidade de furia do bárbaro
        print("Barbaro Furioso")
