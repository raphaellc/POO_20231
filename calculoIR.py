import imposto

print("inicia programa calculo Imposto")
ir = imposto.Imposto()
ir.defineNomeContribuinte("Raphael")
ir.defineNumeroDependentes(0)
ir.defineProfissao("Professor")
ir.defineRendaMensal(1901)
print("valor IR =R$ ")
print(ir.calculaValorIR())
