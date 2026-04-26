"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""

peso_kg = int(input("Digite o peso do paciente em kg:"))
dose_remedio = peso_kg * 2
print("A dose recomendada é de ",  dose_remedio , "mg.")

