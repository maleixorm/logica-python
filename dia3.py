# Operadores Aritméticos

a = 5
b = 2

print(a + b) # soma
print(a - b) # divisão
print(a * b) # multiplicação
print(a / b) # divisao
print(a // b) # divisão inteira
print(a % b) # resto da divisao
print(a ** b) # exponenciação


# Operadores de Comparação

x = 10
y = 5

print(x > 5)
print(x >= 5)
print(y < 5)
print(y <= 5)
print(x != y)


# Operadores Lógicos

idade = 20
possui_carteira = True
pode_dirigir = (idade >= 18) and possui_carteira
print(pode_dirigir)

eh_estudante = False
sua_idade = 60
meia_entrada = eh_estudante == True or idade >= 60
print(meia_entrada)

chovendo = True
nao_chovendo = not chovendo
print("Chovendo: ", chovendo)
print("Não Chovendo: ", nao_chovendo)

# Revisão

#nota > 7 e frequência = 80%
nota = 8
frequencia = 60
passou_de_ano = (nota > 7) and (frequencia > 80)
print("Passou de ano: ", passou_de_ano)

# senhas iguais
# criando um registro de usuario
senha = "teste123"
confirmacao_senha = "teste1234"
aviso_senha_errada = senha != confirmacao_senha
print("A senha está errada? ", aviso_senha_errada)

# mesa de bar
# 123.85
# quanto cada pessoa vai pagar? 3
conta = 123.85
pessoas = 3
parte_de_cada_um = conta / pessoas
print("Cada um tem que pagar: ", parte_de_cada_um)