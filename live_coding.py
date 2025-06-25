class PaymentProcessor:
   def __init__(self, credit_card, amount, payment_acquirer):
       self.credit_card = credit_card
       self.amount = amount
       self.payment_acquirer = payment_acquirer

   def pay(self):
       if self.payment_acquirer == "zoop":
           # lógica para processar um pagamento com cartão na Zoop

       elif self.payment_acquirer == "adyen":
           # lógica para processar um pagamento com cartão na Adyen

	   elif self.payment_acquirer == "rede":
           # lógica para processar um pagamento com cartão na Rede

# A forma ideal é:
# 1. Criar uma classe abstrata com um método abstrato que processa 
# pagamentos em uma adquirente (independente de qual seja, ou seja, 
# independente de detalhes).

# 2. Criar uma classe concreta com um método que processa pagamentos 
# em uma adquirente específica.

# 3. Criar uma classe de alto nível que dependa somente da abstração.

# Abstração para operações de pagamento -> esse é o contrato da dependência (nossa "interface")

from abc import ABC, abstractmethod

class PaymentAcquirerInterface(ABC):
   @abstractmethod
   def process_payment(self, credit_card, amount):
       pass

# Implementação concreta para um pagamento na Zoop
class Zoop(PaymentAcquirerInterface):
   def process_payment(self, credit_card, amount):
       # lógica para processar um pagamento com cartão na Zoop

# Implementação concreta para um pagamento na Adyen
class Adyen(PaymentAcquirerInterface):
   def process_payment(self, credit_card, amount):
       # lógica para processar um pagamento com cartão na Adyen

# Classe de alto nível que faz a ação de pagar e depende da abstração 
# PaymentAcquirerInterface -> podemos trocar a implementação das 
# adquirentes sem afetar essa classe
class PaymentProcessor:
   def __init__(self, credit_card, amount, payment_acquirer: PaymentAcquirerInterface):
       self.credit_card = credit_card
       self.amount = credit_card
       self.payment_acquirer = payment_acquirer

   def pay(self):
       self.payment_acquirer.process_payment(self.credit_card, self.amount)

# Fazendo um pagamento com cartão na Zoop
credit_card = "1234567890123456"
amount = 100.0
payment_acquirer = Zoop()

payment_processor = PaymentProcessor(credit_card, amount, payment_acquirer)
payment_processor.pay()

# Fazendo um pagamento com cartão na Adyen
credit_card = "9876543210987654"
amount = 200.0
payment_acquirer = Adyen()

payment_processor = PaymentProcessor(credit_card, amount, payment_acquirer)
payment_processor.pay()

# Conclusão:
# A classe PaymentAcquirer é uma abstração (uma classe abstrata) que 
# define um contrato (método process_payment) para classes de adquirentes. 
# Isso cumpre o requisito de depender de abstrações em vez de detalhes concretos.

# As classes concretas Zoop e Adyen implementam a abstração definida na 
# classe PaymentAcquirer. 
# Elas fornecem a implementação específica do método process_payment. 
# Essas classes de adquirentes podem ser trocadas facilmente porque seguem 
# o contrato estabelecido pela classe abstrata.

# A classe de alto nível PaymentProcessor depende da abstração 
# PaymentAcquirer (injetada através do construtor) em vez de depender 
# das implementações concretas específicas das adquirentes. 
# Isso permite trocar facilmente a implementação da adquirente 
# sem modificar a classe PaymentProcessor, o que é consistente com o DIP.
