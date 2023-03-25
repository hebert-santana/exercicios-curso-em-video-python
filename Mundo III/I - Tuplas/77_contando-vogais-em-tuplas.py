# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

times = ('arsenal', 'aston villa', 'brentford', 'brighton', 'burnley', 'chelsea', 'crystal palace', 'everton', 'leeds', 'leicester', 'liverpool', 'manchester city', 'manchester united', 'newcastle', 'norwich', 'southampton', 'tottenham', 'watford', 'west ham', 'wolverhampton')

for time in times:
    vogais = ''
    for letra in time:
        if letra in 'aeiou' and letra.upper() not in vogais:
            vogais += letra.upper() + ' '
    print(f'As vogais presentes no nome do time {time.upper()} são: {vogais}')
