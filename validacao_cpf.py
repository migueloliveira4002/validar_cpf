#cpf = ''
cpf = input("Digite seu CPF, apenas numeros: ")

# VAMOS CALCULAR O PRIMEIRO DIGITO
nove_digitos = cpf[:9]
contador = 10
mult_1 = 0
for i in nove_digitos:
    mult_1 += int(i) * contador
    contador -= 1

mult_2 = (mult_1 * 10) % 11
mult_2 = mult_2 if mult_2 <= 9 else 0

# AQUI VAMOS CALCULAR O SEGUNDO DIGITO
dez_digitos = nove_digitos + str(mult_2)
contador_dez = 11
mult_3 = 0
for i in dez_digitos:
    mult_3 += int(i) * contador_dez
    contador_dez -= 1

mult_4 = (mult_3 * 10) % 11
mult_4 = mult_4 if mult_4 <= 9 else 0

# GERA O CPF COM OS DOIS DIGITOS CALCULADOS
cpf_gerado = f'{nove_digitos}{mult_2}{mult_4}'
print(f'CPF Gerado: {cpf_gerado}')

# VALIDA SE O CPF ESTA CORRETO
if cpf_gerado == cpf:
    print("O CALCULO ESTA CORRETO!")
else:
    print("O CALCULO ESTA INCORRETO!")
