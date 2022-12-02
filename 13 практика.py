ticket = int(input("Введите количество билетов: "))
ticket_price = 0
for i in range(ticket):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        ticket_price += 0
    elif 18 <= age < 25:
        ticket_price += 990
    else:
        ticket_price += 1390
if ticket > 3:
    ticket_price -= ((ticket_price/100)*10)
print("Итого:", round(ticket_price), "рублей.")