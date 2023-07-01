lista = []
def adicionar_lista():
    item = input("Digite o produto: ")
    lista.append(item)
    print("Item adicionado com Sucesso!!")
    print(lista)
    if item == 'sair':
        menu()
    else:
        return adicionar_lista()

def remover():
    item = input("Digite o item que deseja remover: ")
    if item in lista:
        lista.remove(item)
        print(lista)
    else:
        print("item não existe dentro da lista")
def mostrar_lista():
    if lista:
        print("Lista de compras:")
        for item in lista:
            print("- " + item)
    else:
        print("A lista de compras está vazia.")
def menu():

    while True:
        print("=========Lista de Compras=========")
        print("1- Adicionar na lista ")
        print("2- Excluir Item")
        print("3- Mostrar Lista")
        print("4- Sair")
        print("=========Lista de Compras=========")

        opc = input("Escolha uma opção:")

        if opc == "1":
            adicionar_lista()
        elif opc == "2":
            remover()
        elif opc == "3":
            mostrar_lista()
        elif opc == "4":
            print("Saindo...")
            break
        else:
            print("Opção invalida!")


menu()
