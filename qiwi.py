from SimpleQIWI import *

token = input("ВАШ ТОКЕН ")
phone = input("ВАШ ТЕЛЕФОН ")

api = QApi(token=token, phone=phone)

print(api.balance)

account = input("Киви Получателя: ")
amount = input("Сумма Перевода: ")
comment = input("Коментарий К Переводу: ")
api.pay(account=account, amount=amount, comment=comment)

print(api.balance)