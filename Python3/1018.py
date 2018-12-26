reais = int(input())

cem = reais//100
cinq = (reais%100)//50
vinte = ((reais%100)%50)//20
dez = (((reais%100)%50)%20)//10
cinc = ((((reais%100)%50)%20)%10)//5
dois = (((((reais%100)%50)%20)%10)%5)//2
um_real = (((((reais%100)%50)%20)%10)%5)%2


print('''{}
{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00
{} nota(s) de R$ 1,00'''.format(reais, cem, cinq, vinte, dez, cinc,dois,um_real))
