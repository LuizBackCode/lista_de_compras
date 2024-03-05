class ListaDeCompras:
    def __init__(self):
        self.lista = []

    
    def adicionar_item(self, item):
        if item not in self.lista:
            self.lista.append(item)
            print(f'{item} adicionado a lista.')
            print('-' * 30)
        else:
            print(f'{item} já existe na lista.')
            print('-' * 30)

    def remover_item(self, item):
        if item not in self.lista:
            print(f'{item} não existe na lista.')
            print('-' * 30)
        else:
            self.lista.remove(item)
            print(f'{item} removido da lista.')
            print('-' * 30)
    
    def exibir_lista(self):
        if self.lista:
            print('Lista de compras: ')
            for item in self.lista:
                print(f'--> {item}')
        else:
            print('Lista vazia...')
    

def interação():
    
    lista = ListaDeCompras()

    while True:

        print('1. Adicionar item a lista')
        print('2. Remover item da lista')
        print('3. Exibir lista de compras')
        print('4. Sair')
        print('-' * 30)


        while True:
            try:
                res = int(input('Escolha uma das opções: '))
                print('-' * 30)
                break
            except ValueError:
                print('[ERRO!] Digite um valor inteiro válido!')
                print('-' * 30)

        if res == 1:
            item = input('Digite o item a ser adicionado: ').upper()
            print('-' * 30)
            lista.adicionar_item(item)
        elif res == 2:
            item = input('Digite o item a ser removido: ').upper()
            print('-' * 30)
            lista.remover_item(item)
        elif res == 3:
            lista.exibir_lista()
            print('-' * 30)
        elif res == 4:
            print('Saindo...')
            break


if __name__ == '__main__':
    interação()