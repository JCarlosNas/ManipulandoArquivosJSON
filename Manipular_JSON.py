# import json
# inventario = {}
# opcao = int(input("Digite: "
#                   "<1> para registrar ativo "
#                   "<2> paraa exibir ativos armazenados: "))
# while opcao >0 and opcao<3:
#     if opcao == 1:
#         resp = "S"
#         while resp == "S":
#             inventario [input("Digite o número patrimonial: ")] = [
#                 input("Digite a data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = input("Digite <S> para continuar. ").upper()
#         with open("inventario_json.json", "w") as arq_json:
#             json.dump(inventario, arq_json)
#         print("JSON gerado!!!! ")
#     elif opcao == 2:
#         with open("inventario_json.json", "r") as arq_json:
#             resultado = json.load(arq_json)
#             for chave, dado in resultado.items():
#                 print("Data................: ", dado[0])
#                 print("Descrição...........: ", dado[1])
#                 print("Departamento........: ", dado[2])
#     opcao = int(input("Digite: "
#                       "<1> para registrar ativo "
#                       "<2>para exibir ativos armazenados:"))
#

# import json
# with open("inventario_json.json", "r") as arq_json:
#     inventario = json.load(arq_json)
# opcao = int(input("Digite :"
#                   "<1> para registrar ativo: "
#                   "<2> para exibir ativos armazenados: "))
# with opcao >0 and opcao <3:
#     if opcao == 1:
#         resp = "S"
#         while resp == "S":
#             inventario[input("Digite o número patrimonial: ")] = [
#                 input("Digite a  data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = input("Digite <S> para continuar: ").upper()
#         with open("inventario_json.json", "w") as arq_json:
#             json.dump(inventario, arq_json)
#         print("JSON gerado!!!!")
#     elif opcao == 2:
#         for chave, dado in inventario.items():
#             print("Data..............: ", dado[0])
#             print("Descrição.........: ", dado[1])
#             print("Departamento......: ", dado[2])
#     opcao = int (input("Digite: "
#                        "<1> para regitstrar ativo: "
#                        "<2> para exibir ativos armazenados: "))

import  json
import os
if os.path.exists("inventario_json.json"):
    with open("inventario_json.json", "r") as arq_json:
        inventario = json.load(arq_json)

else:
    inventario = {}
opcao = int(input("Digite :"
                  "<1> para registra ativo: "
                  "<2> para exibir ativos armazenados: "))

from Funcoes_JSON import *

inventario = ler_arquivo("inventario_json.json")
opcao = chamarMenu()
while opcao >0 and opcao <3:
    if opcao == 1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao == 2:
        exibir("inventario_json.json")
    opcao = chamarMenu()


