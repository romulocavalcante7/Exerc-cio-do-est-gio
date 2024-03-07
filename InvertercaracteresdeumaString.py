def inverter_string(string):
    caracteres = list(string)
    inicio, fim = 0, len(caracteres) - 1
    while inicio < fim:
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        inicio += 1
        fim -= 1
    return "".join(caracteres)

minha_string = input("Informe uma string: ")
resultado = inverter_string(minha_string)
print(f"String invertida: {resultado}")
