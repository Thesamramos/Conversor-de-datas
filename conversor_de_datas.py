import arrow

print("====== CONVERSOR DE DATAS ======")

day = int(input("Informe o dia (2 digitos): "))
month = int(input("Informe o mês (2 digitos): "))
year = int(input("informe o ano (4 digitos): "))

date = arrow.get(f"{year}-{month}-{day}")

print("\n[1] Formado Internacional\
      [2] Formato dos EUA\
      [3] Formato da Europa\
      [4] Formato da Ásia\
      [5] Formato Verbal")

choice = int(input("Escolha um formato de data (digite o número): "))

def return_date_format(choice):
    match choice:
        case 1:
            return "\nData formatada para o padrão internacional: " + date.format("YYYY-MM-DD")
        case 2:
            return "\nData formatada para o padrão dos EUA: " + date.format("MM/DD/YYYY")
        case 3:
            return "\nData formatada para o padrão europeu: " + date.format("DD/MM/YYYY")
        case 4:
            return "\nData formatada para o padrão asiatico: " + date.format("YYYY/MM/DD")
        case 5:
            return "\nData formatada para o padrão verbal: " + date.format("DD - MMMM - YYYY", locale="pt-br").replace("-", "de")
        case _:
            return "\nOpção Inválida"

print(return_date_format(choice))