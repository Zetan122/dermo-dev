from SimpleQIWI import *

token = input("ВАШ ТОКЕН")
phone = input("ВАШ ТЕЛЕФОН")

api = QApi(token=token, phone=phone)

print(api.balance)

api.pay(account="ТЕЛЕФОН ПОЛУЧАТЕЛЯ", amount=1, comment='комментарий')

print(api.balance)