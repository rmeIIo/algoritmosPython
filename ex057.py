sexo = str(input('Informe seu seu sexo: [M/F] ')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f"Sexo {sexo} registrado com sucesso!")

