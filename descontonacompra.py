#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
print("$$$$ --Para saber quanto será seu desconto e o preço final do produto, informe os dados abaixo.-- $$$$")
preco = float(input("Qual preço do produto?  "))
desconto = int(input("De quanto será o desconto (%)?  ")) / 100
economia = round(preco * desconto, 2)
preco_final = preco - economia
print("Você economizou: R$", economia)
print("O preço comm desconto é: R$", preco_final)

