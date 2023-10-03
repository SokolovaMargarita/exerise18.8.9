tickets = int(input("Введите количество билетов: "))
total_cost = 0

for _ in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        ticket_cost = 0
    elif age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390

    total_cost += ticket_cost

if tickets > 3:
    total_cost *= 0.9

print("Сумма к оплате:", total_cost, "руб.")