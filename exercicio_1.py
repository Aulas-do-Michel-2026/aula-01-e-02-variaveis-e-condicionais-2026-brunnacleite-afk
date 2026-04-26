"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""
nota_1 = float(input("Digite a primeira nota:"))
nota_2 = float(input("Digite a segunda nota:"))
nota_3 = float(input("Digite a terceira nota:"))
print("Sua média é ", round((nota_1+nota_2+nota_3)/3,2))
