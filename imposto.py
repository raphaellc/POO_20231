"""Classe Imposto"""
class Imposto:
    """Construtor Imposto"""
    def __init__(self):
        self.nome_contribuinte = ""
        self.ano_nasc = 0
        self.profissao = ""
        self.escolaridade = ""
        self.renda_mensal = 0.0
        self.num_dependentes = 0
    
    def defineNomeContribuinte(self, nome):
        self.nome_contribuinte = nome

    def defineProfissao(self, profissao):
        self.profissao = profissao

    def defineRendaMensal(self, rm):
        self.renda_mensal = rm
        
    def defineNumeroDependentes(self, numdep):
        self.num_dependentes = numdep

    """Define a idade da pessoa"""
    def defineIdade(self, idade):
        self.idade = idade

    """Define a Renda anual"""    
    def defineRendaAnual(self, ra):
        self.renda_anual = ra

    def defineRendaPerCapta(self, rpc):
        self.renda_p_capta = rpc

    def defineAliquotaIRMaxima(self):
        if self.renda_mensal > 0.0:
            if self.renda_mensal <= 1900.00:
                self.al_IRM = 0
            elif self.renda_mensal >1900.00 and self.renda_mensal <= 2820.00:
                self.al_IRM = 7.5
            elif self.renda_mensal > 2820.00 and self.renda_mensal <= 3740.00:
                self.al_IRM = 15.00
            elif self.renda_mensal > 3740.00 and self.renda_mensal <= 4660.00:
                self.al_IRM = 22.5
            else:
                self.al_IRM = 27.5
        else:
            print("Renda Mensal Não informada")
    
    """Calcula o valor do Imposto de Renda"""
    def calculaValorIR(self):
        self.defineAliquotaIRMaxima()
        self.valor_devido = ((self.al_IRM/100) * self.renda_mensal) - self.num_dependentes * 190.0
        return self.valor_devido 
    
