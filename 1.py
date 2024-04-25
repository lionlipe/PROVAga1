def divisivelPor2():
    numero = int(input("Por favor, insira um número: "))
    if numero % 2 == 0:
        return True
    else:
        return False

# ver se a função é divisel por 2 ou não
checar = divisivelPor2()
print("O número inserido é divisível por 2?", checar, "!")