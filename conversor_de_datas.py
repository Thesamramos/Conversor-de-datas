import arrow

print("====== CONVERSOR DE DATAS ======")

print('[1] Usar uma data diferente\
      [2] Usar data atual')

date_type =  int(input("Informe o número da sua escolha: "))

if date_type == 1:
    day = int(input("\nInforme o dia (2 digitos): "))
    month = int(input("Informe o mês (2 digitos): "))
    year = int(input("informe o ano (4 digitos): "))

    date = arrow.get(f"{year}-{month}-{day}")
else:
    date = arrow.utcnow()

while True:

    print("\n[1] Formato Internacional\
        [2] Formato dos EUA\
        [3] Formato da Europa\
        [4] Formato da Ásia\
        [5] Formato Verbal\
        [6] Sair")

    choice_date_format = int(input("Escolha um formato de data (digite o número): "))

    if choice_date_format == 6:
        print("\nPrograma encerrado.")
        break

    def return_date_format(choice_date_format):
        match choice_date_format:
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

    print(return_date_format(choice_date_format))