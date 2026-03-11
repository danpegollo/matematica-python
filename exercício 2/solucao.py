nota1 = float(input("Coloque sua nota de português: "))
peso1 = int(input("Coloque o peso da sua nota de português: "))
nota2 = float(input("Coloque sua nota de matemática: "))
peso2 = int(input("Coloque o peso da sua nota de matemática: "))
nota3 = float(input("Coloque sua nota de inglês: "))
pesso3 = int(input("Coloque o peso da sua nota de inglês: "))

pesoTotal = peso1 + peso2 + pesso3
media = (nota1 * peso1 + nota2 * peso2 + nota3 * pesso3)/ pesoTotal
print(f"Sua nota final é de: {media:.2f} e peso total de", pesoTotal)