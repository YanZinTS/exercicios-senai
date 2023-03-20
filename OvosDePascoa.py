precos = {
    "pequeno": 7.80,
    "medio": 12.90,
    "grande": 23.95,
    "preto": 9.67,
    "branco": 4.50,
    "leite": 9.32,
    "kitkat": 4.67,
    "mms": 5.43,
    "presente": 2.50,
    "entrega": 5.00,
}

tamanho = input("Qual tamanho do ovo você deseja (pequeno, medio, grande)? ")
sabor1 = input("Qual sabor de recheio você deseja (preto, branco, leite)? ")
sabor2 = input("Deseja adicionar um segundo sabor (preto, branco, leite)? (Deixe em branco se não quiser) ")

#preço baseado no tamanho e sabor selecionados
preco_base = precos[tamanho] + (precos[sabor1] + precos[sabor2])/2 if sabor2 else precos[tamanho] + precos[sabor1]

#adicionais
adicionais = []
while True:
    adicional = input("Deseja adicionar um adicional (kitkat, mms)? (Deixe em branco se não quiser) ")
    if not adicional:
        break
    adicionais.append(adicional)

#preço baseado nos adicionais selecionados
preco_adicionais = sum(precos[adicional] for adicional in adicionais)

#tipo de serviço
servico = input("Deseja presente (s/n)? ")
if servico.lower() == "s":
    preco_servico = precos["presente"]
else:
    preco_servico = 0
    
servico = input("Deseja entrega (s/n)? ")
if servico.lower() == "s":
    preco_servico += precos["entrega"]

# Cálculo do preço final
preco_total = preco_base + preco_adicionais + preco_servico
pagamento = input("Qual o método de pagamento (dinheiro, cartão, pix)? ")
if pagamento.lower() == "cartao":
    preco_total += precos["cartao"]
elif pagamento.lower() == "dinheiro" or pagamento.lower() == "pix":
    preco_total *= 0.9

#quantidade de ovos
quantidade = int(input("Qual a quantidade de ovos? "))
preco_total *= quantidade

#preço total
print("O preço total é R$", preco_total)