class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Atributo protegido

    def _metodo_prot(self):  # Método protegido
        print("Método protegido da classe Pessoa.")

    def __metodo_priv(self):  # Método privado
        print("Método privado da classe Pessoa.")


class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, matricula: str):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self._salario = None  # Atributo protegido

    def _metodo_prot(self):  # Método protegido sobrescrito
        print("Método protegido da classe Funcionario.")

    def __metodo_priv(self):  # Método privado sobrescrito
        print("Método privado da classe Funcionario.")

    def calcular_salario(self):
        # Implementação do método para calcular o salário
        self._salario = 2000  # Atributo protegido


class Gerente(Funcionario):
    def __init__(self, nome: str, idade: int, cpf: str, matricula: str, setor: str):
        super().__init__(nome, idade, cpf, matricula)
        self.setor = setor

    def _metodo_prot(self):  # Método protegido sobrescrito novamente
        print("Método protegido da classe Gerente.")

    def __metodo_priv(self):  # Método privado sobrescrito novamente
        print("Método privado da classe Gerente.")

    def bonificar(self):
        # Implementação do método para bonificar o gerente
        self._salario += 1000  # Atributo protegido


# Testando o código
funcionario = Funcionario("João", 30, "123.456.789-00", "001")
gerente = Gerente("Maria", 35, "987.654.321-00", "002", "TI")

# Atributos públicos
print(funcionario.nome)  # João
print(gerente.nome)  # Maria
print(funcionario.matricula)  # 001
print(gerente.matricula)  # 002

# Atributos protegidos
print(funcionario._cpf)  # 123.456.789-00
print(gerente._salario)  # None
funcionario.calcular_salario()
gerente.calcular_salario()
print(funcionario._salario)  # 2000
print(gerente._salario)  # 2000

# Métodos protegidos e privados
funcionario._metodo_prot()
