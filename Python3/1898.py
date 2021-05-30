first = input().encode("utf-8").strip()
second = input().encode("utf-8").strip()

first_digits = [x for x in first if x.isnumeric() or x == "."]
second_digits = [x for x in second if x.isnumeric() or x == "."]

cpf = "".join(first_digits[:11])
first_value = "".join(first_digits[11:])
second_value = "".join(second_digits)

first_dot = first_value.find(".")
if first_dot != -1:
    first_value = first_value[:min(len(first_value), first_dot + 3)]

second_dot = second_value.find(".")
if second_dot != -1:
    second_value = second_value[:min(len(second_value), second_dot + 3)]

print(f"cpf {cpf}")
print(f"{float(first_value) + float(second_value):.2f}")


#aceitos = {'0','1','2','3','4','5','6','7','8','9','.'}
#
#entrada1 = input()
#entrada2 = input()
#
#entrada1_decodificada = "".join(char for char in entrada1 if char in aceitos)
#entrada2_decodificada = "".join(char for char in entrada2 if char in aceitos)
#
#ponto1 = entrada1_decodificada.find('.')
#ponto2 = entrada2_decodificada.find('.')
#
#if ponto1 != -1:
#    final_pos = min(ponto1 + 3, len(entrada1_decodificada))
#    entrada1_decodificada = entrada1_decodificada[:final_pos]
#
#
#if ponto2 != -1:
#    final_pos = min(ponto2 + 3, len(entrada2_decodificada))
#    entrada2_decodificada = entrada2_decodificada[:final_pos]
#
#cpf = entrada1_decodificada[:11]
#valor = float(entrada2_decodificada)+float(entrada1_decodificada[11:])
#
#print('cpf {}'.format(cpf))
#print('{:.2f}'.format(valor))
