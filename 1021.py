valor = input().split('.')
reais = int(valor[0])
cents = int(valor[1])

cem = reais // 100
cinq = (reais % 100) // 50
vinte = ((reais % 100) % 50) // 20
dez = (((reais % 100) % 50) % 20) // 10
cinc = ((((reais % 100) % 50) % 20) % 10) // 5
dois = (((((reais % 100) % 50) % 20) % 10) % 5) // 2

um_real = (((((reais % 100) % 50) % 20) % 10) % 5) % 2
cinq_cent = cents // 50
vin_cin_cent = (cents % 50) // 25
dez_cent = ((cents % 50) % 25) // 10
cinc_cent = (((cents % 50) % 25) % 10) // 5
um_cent = (((cents % 50) % 25) % 10) % 5

print('''NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01'''.format(cem, cinq, vinte, dez, cinc, dois, um_real, cinq_cent,
                                 vin_cin_cent, dez_cent, cinc_cent, um_cent))
