from criptografia import encrypt, decrypt
import random
import string
import os
import filecmp
# Comparar linhas de arquivos
def arquivos_iguais(arquivo1, arquivo2):
    lista1, lista2 = [], []
    for line in arquivo1:
        lista1.append(line)
    for line in arquivo2:
        lista2.append(line)
    return lista1 == lista2
    

    






# Gera arquivos com strings aleatórias
arquivos = []
encriptografados = []
for i in range(0, 10):
    arquivo_atual = 'dados_teste' + str(i) + '.txt'
    arquivos.append(arquivo_atual)
    encriptografados.append(arquivo_atual + '.enc')
    with open(arquivo_atual, 'w') as f:
        for j in range(0, 10*(i+1)):
            f.write(''.join(random.choices(string.ascii_uppercase + string.digits, k=10*(i + 1))))
            f.write('\n')

# Criptografa todos os arquivos gerados
i = 0
for arq in arquivos:
    print('Encriptografando arquivo {0}'.format(arq))
    encrypt(arq, str(i))
    i += 1

i = 0
# Descriptografa os arquivos encriptografados
descriptografados = []
for arq in encriptografados:
    descriptografados.append('descripto_' + arquivos[i])
    print('Descriptografando arquivo {0}'.format(arq))
    decrypt(arq, 'descripto_', 'chave' + str(i) + '.bin')
    i += 1

# Compara os arquivos descriptogrados com os originais
for i in range(0, 10):
    arquivo_original = arquivos[i]
    arquivo_descriptografado = descriptografados[i]
    with open(arquivo_original, 'r') as orig, open(arquivo_descriptografado, 'r') as descr:
        if not arquivos_iguais(orig, descr):
            print('{0} difere de {1}'.format(arquivo_original, arquivo_descriptografado)) 
        
        





