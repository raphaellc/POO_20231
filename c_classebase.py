class ClasseBase:
    atr_pub = 0
    __atr_priv = 0
    _atr_prote = 0
    _nome_classe = ""

    def __init__(self):
        self.__atr_priv = 10
        self._nome_classe = "Base"
        print ("sou a classe"+self._nome_classe)
    
    def __metPriv(self):
        self.__atr_priv +=1
        print ("sou um método privado base"+ str(self.__atr_priv))
        
        

    def _metProt(self):
        self._atr_prote += 1
        print("sou um metodo protegido base e meu atributo é "+ str(self._atr_prote))
        

    
    def metPubl(self):
        print("sou um metodo public base")


class SubClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print("rodando na subclasse")
        self._atr_prote = 0
        #self._atr_priv = 0
    def metSubClasse(self):
        self._atr_prote +=1
        print("metodo privado sendo chamado em metodo da subclasse")
        print("O atributo Protegido herdado da superclasse é "+str(self._atr_prote))

    def metPubl(self):
        super().metPubl()
        super()._metProt()
        print("sobrescrevendo o metodo da classe base")
    
    
base = ClasseBase()
base._metProt()

base._atr_prote = 10
sc = SubClasse()
sc.metSubClasse()
sc.metPubl()


    