from dataclasses import dataclass,asdict
from typing import List
from collections.abc import Sequence


@dataclass
class Cliente:
    nome: str
    email: str
    pedido: str

    def dicts(self):
        return {k: str(v) for k,v in asdict(self).items()}

@dataclass
class Pedidos(Sequence):
    pedidos: List[Cliente]
    index: int = 0
    nextindex: int = 0

    def append(self, *args) -> None:
        for value in args:
            self.pedidos[self.index] = value
            self.index +=1

    def __len__(self) -> int:
        return self.index

    def __getitem__(self, index) -> Cliente:
        return self.pedidos[index]

    def __next__(self) -> None:
        if self.nextindex >= self.index:
            self.nextindex= 0
            raise StopIteration
        value = self.pedidos[self.nextindex]
        self.nextindex +=1
  

def verify_orders(pedidos: Pedidos):
    match pedidos:
        case Pedidos(pedidos='Pending',):
            for num in pedidos.pedidos:
                print("pedido cadastrado", num)
        case Pedidos(pedidos='Approved'):
            for num in pedidos.pedidos:
                print("pedido aprovado", num)

        case Pedidos(pedidos='Reject'):
            for num in pedidos.pedidos:
                print("pedido cancelado", num)

        case _:
            print('nao encontrado')

    print('verificar')

if __name__=="__main__":
    new_order = Cliente('Teste1', 'teste1@live.com', '1234')
  
    lista_pedidos = Pedidos([verify_orders(new_order).__dict__])
    for listas in lista_pedidos:
        print(listas)

