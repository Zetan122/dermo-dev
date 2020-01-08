from SimpleQIWI import *

token=input(‘Enter Token: ‘)

phone=input(‘Enter phone: ‘);

api = QApi(token=token, phone=phone)

print(api.balance)

api.pay(account=”ваш номер”, ammout=”количество выводимых средств”, comment=”любой комментарий”

print(api.balance)

input()