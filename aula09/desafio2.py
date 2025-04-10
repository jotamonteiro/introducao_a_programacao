numero = int(input('Digite Seu Numero: '))

nome_arquivo = f"tabuada_{numero}"

with open(nome_arquivo , "w") as arquivo:
    for x in range(11):
        arquivo.write(f"{numero} x {x} = {numero * x}\n")

print("Tabuada Criada Com Sucesso")
