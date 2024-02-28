#1. Crie uma função que conte o número de vogais em uma string.
def contar_vogais(string):
    contador = 0
    vogais = "aeiouAEIOU"
    

    for caractere in string:
        if caractere in vogais:
            contador += 1

    return contador
texto = "Olá"
print("Número de vogais:", contar_vogais(texto))

#2. Escreva um programa que substitua todas as ocorrências de uma letra em uma string por outra letra.
def substituir_letra(string, letra_antiga, letra_nova):
    resultado = ""
    for caractere in string:
        if caractere == letra_antiga:
            resultado += letra_nova
        else:
            resultado += caractere
    return resultado

texto = "Olá, como você está hoje?"
letra_antiga = "o"
letra_nova = "x"

texto_modificado = substituir_letra(texto, letra_antiga, letra_nova)
print("Texto original:", texto)
print("Texto modificado:", texto_modificado)

#3. Crie uma função que retorne o número de palavras em uma string.
def contar_palavras(string):
    return len(string.split())

#4. Crie uma função que conte o número de ocorrências de uma determinada palavra em uma frase.
def contar_ocorrencias_palavra(frase, palavra):
    palavras_na_frase = frase.split()
    return palavras_na_frase.count(palavra)

#5. Crie uma função que encontre os k maiores elementos em uma lista, mantendo a ordem original.
def k_maiores(lista, k):
    return sorted(lista, reverse=True)[:k]

#6. Escreva um programa que implemente a soma de matrizes usando listas aninhadas.
def soma_matrizes(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

#7. Crie uma função que encontre a interseção de duas listas sem usar conjuntos.
def intersecao_listas(lista1, lista2):
    return [item for item in lista1 if item in lista2]

#8. Crie uma função que embaralhe os elementos de uma lista de forma aleatória.
import random
def embaralhar_lista(lista):
    lista_embaralhada = lista[:]
    random.shuffle(lista_embaralhada)
    return lista_embaralhada

#9. Escreva um programa que encontre o par de elementos em uma lista cuja soma seja igual a um determinado valor.
def encontrar_par_soma(lista, soma_desejada):
    pares = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == soma_desejada:
                pares.append((lista[i], lista[j]))
    return pares

#10.Criar um algoritmo para calcular a frequência que uma palavra aparece em um texto.
def calcular_frequencia_palavra(texto, palavra):
    palavras_na_frase = texto.split()
    return palavras_na_frase.count(palavra)

#11. Escreva um programa que identifique todos os números primos em uma lista de números inteiros.
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(lista):
    return [numero for numero in lista if eh_primo(numero)]

#12.Implemente um algoritmo para encontrar a menor string em uma lista de strings.
def menor_string(lista_strings):
    return min(lista_strings, key=len)

#13.Crie um algoritmo para ler um arquivo texto.
def ler_arquivo_texto(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

#14.Crie um algoritmo para ler um arquivo CSV.
import csv
def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, newline='') as csvfile:
        leitor_csv = csv.reader(csvfile)
        return [linha for linha in leitor_csv]

#15.Crie um algoritmo para ler um arquivo JSON.
import json
def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo) as json_file:
        return json.load(json_file)

#16.Crie um algoritmo para consolidar um ou mais arquivos de texto de um diretório.
import os
def consolidar_arquivos_texto(diretorio):
    texto_consolidado = ''
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.txt'):
            with open(os.path.join(diretorio, nome_arquivo), 'r') as arquivo:
                texto_consolidado += arquivo.read() + '\n'
    return texto_consolidado

#17.Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve mais vendas.
def mes_maior_vendas(dados_csv):
    mes_vendas = {}
    for linha in dados_csv[1:]:
        mes = linha[0]
        vendas = int(linha[1])
        if mes in mes_vendas:
            mes_vendas[mes] += vendas
        else:
            mes_vendas[mes] = vendas
    return max(mes_vendas, key=mes_vendas.get)

#18.Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve menos vendas.
def mes_menor_vendas(dados_csv):
    mes_vendas = {}
    for linha in dados_csv[1:]:
        mes = linha[0]
        vendas = int(linha[1])
        if mes in mes_vendas:
            mes_vendas[mes] += vendas
        else:
            mes_vendas[mes] = vendas
    return min(mes_vendas, key=mes_vendas.get)

#19.Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e o valor de cada venda realizada), retornando qual a soma de vendas que teve cada vendedor.
def soma_vendas_vendedor(dados_csv):
    vendas_vendedor = {}
    for linha in dados_csv[1:]:
        vendedor = linha[0]
        venda = float(linha[1])
        if vendedor in vendas_vendedor:
            vendas_vendedor[vendedor] += venda
        else:
            vendas_vendedor[vendedor] = venda
    return vendas_vendedor

#20. Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e o valor de cada venda realizada), retornando qual o vendedor que mais vendeu e o que menos vendeu.
def vendedor_mais_menos_vendas(dados_csv):
    vendas_vendedor = soma_vendas_vendedor(dados_csv)
    vendedor_mais_vendas = max(vendas_vendedor, key=vendas_vendedor.get)
    vendedor_menos_vendas = min(vendas_vendedor, key=vendas_vendedor.get)
    return vendedor_mais_vendas, vendedor_menos_vendas