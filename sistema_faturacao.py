def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Escreva um numero valido.")



fila_prioritaria = []
fila_normal = []

opcao = ""

while opcao != "0":
    print("\n===== LOJA DE PRODUTOS ALIMENTARES =====")
    print("1. Registar cliente")
    print("2. Ver fila de espera")
    print("3. Atender proximo cliente")
    print("0. Sair")
    opcao = input("Escolha uma opcao: ")

    # ---------- REGISTAR CLIENTE ----------
    if opcao == "1":
        nome = input("Nome do cliente: ")
        genero = input("Genero (M/F): ").upper()
        total = ler_numero("Valor total das compras: ")
        idade = int(ler_numero("Idade: "))


        gravida = "N"
        if genero == "F":
            gravida = input("Esta gravida? (S/N): ").upper()
        deficiente = input("Tem deficiencia? (S/N): ").upper()


        if total > 100000:
            bonus = total * 0.10
        else:
            bonus = 0
        a_pagar = total - bonus


        ficha = {"nome": nome, "genero": genero, "total": total,
                 "bonus": bonus, "a_pagar": a_pagar}


        if idade >= 60 or gravida == "S" or deficiente == "S":
            fila_prioritaria.append(ficha)
            print("Cliente colocado na fila prioritaria.")
        else:
            fila_normal.append(ficha)
            print("Cliente colocado na fila normal.")

    # ---------- VER FILA ----------
    elif opcao == "2":
        print("Fila prioritaria:")
        for c in fila_prioritaria:
            print("-", c["nome"])
        print("Fila normal:")
        for c in fila_normal:
            print("-", c["nome"])

    # ---------- ATENDER ----------
    elif opcao == "3":
        if len(fila_prioritaria) == 0 and len(fila_normal) == 0:
            print("Nao ha clientes em espera.")
        else:

            if len(fila_prioritaria) > 0:
                cliente = fila_prioritaria.pop(0)
            else:
                cliente = fila_normal.pop(0)

            print("--- Fatura ---")
            print("Cliente:", cliente["nome"])
            print("Genero:", cliente["genero"])
            print("Total:", cliente["total"])
            print("Bonus:", cliente["bonus"])
            print("A pagar:", cliente["a_pagar"])

    # ---------- SAIR ----------
    elif opcao == "0":
        print("Programa terminado.")

    else:
        print("Opcao invalida.")
