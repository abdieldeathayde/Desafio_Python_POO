entrada = input().split()

mais_frequente = ""
maior_contagem = 0

for produto in entrada:
    contagem = entrada.count(produto)
    
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto

print(mais_frequente)