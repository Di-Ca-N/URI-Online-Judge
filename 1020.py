n = int(input())
anos = n//365
meses = n%365//30
dias = n%365%30

print('''{} ano(s)
{} mes(es)
{} dia(s)'''.format(anos, meses, dias))
