from SimpleQIWI import *

token = input("ВАШ ТОКЕН")
phone = input("ВАШ ТЕЛЕФОН")

api = QApi(token=token, phone=phone)

print(api.balance)

api.pay(account="+79197211395", amount=240, comment='+тест ')

print(api.balance)