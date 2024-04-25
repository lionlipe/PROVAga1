def divisivelPorN():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite outro número inteiro, que não seja zero: "))

    # Verificar se o numero2 é 0
    if numero2 == 0:
        print("Não é possível, coloque um número maior que zero.")
        return False

    # Verificar se é divisivel ou nao
    if numero1 % numero2 == 0:
        print("O primeiro número é divisível pelo segundo!")
        return True
    else:
        print("O primeiro número não é divisível pelo segundo.")
        return False

# Mostrar se é true ou false
resultado = divisivelPorN()
print("True ou false?", resultado)