import arrow

print("====== CONVERSOR DE DATAS ======")

print('[1] Usar uma data diferente\
      [2] Usar data atual')

date_type =  int(input("Informe o número da sua escolha: "))

if date_type == 1:
    day = int(input("\nInforme o dia (2 digitos): "))
    month = int(input("Informe o mês (2 digitos): "))
    year = int(input("informe o ano (4 digitos): "))

    date = arrow.get(year, month, day)
else:
    date = arrow.now()

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

    def formatted_date(choice_date_format):
       formats = {
           1:"YYYY-MM-DD",
           2:"MM/DD/YYYY",
           3:"DD/MM/YYYY",
           4:"YYYY/MM/DD",
           5:"DD [de] MMMM [de] YYYY"
       }
       try:
        if choice_date_format == 5:
            return "\nData formatada: " + date.format(formats[choice_date_format], locale='pt-br')
        else:
            return "\nData formatada: " + date.format(formats[choice_date_format])
       except KeyError:
           return "\nOpção Inválida"

    print(formatted_date(choice_date_format))