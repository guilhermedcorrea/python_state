from __future__ import annotations
from abc import ABC, abstractmethod

class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()

    def approve(self)  -> None:
        self.state.approve()

    def reject(self)  -> None:
        self.state.reject()
    
class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        ...

    @abstractmethod
    def approve(self) -> None:
        ...
    @abstractmethod
    def reject(self) -> None:
        ...

class PaymentPending(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("Pagamento já pendente, não posso fazer nada!")
        
    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("Pagamento aprovado !")

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print("Pagamento recusado !")

class PaymentApproved(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("Pagamento recusado !")
      
    def approve(self) -> None:
        print("Pagamento já aprovado, não posso fazer nada.")

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print("Pagamento recusado !")


class PaymentReject(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("Pagamento recusado. Não vou recusa-lo novamente")
       
    def approve(self) -> None:
        print("Pagamento Recusado, não posso aprova-lo")

    def reject(self) -> None:
        print("Pagamento ja rejeitado")


if __name__=="__main__":
    order = Order()
    order.pending()
    order.approve()

