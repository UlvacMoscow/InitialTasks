all_the_money = 1600 # euro
ruble_exchange_rate_euro = 70 #ruble = 1 euro
tourist_day_cost_1 = 3
tourist_day_cost_2 = 2
tourist_count = 2
trip_count = 2
trip_lengt_1 = 14
trip_lengt_2 = 13
flight_cost = 100
flight_per_trip = 2

tourist_table_cost_1 = [tourist_day_cost_1 * trip_lengt_1,tourist_day_cost_1 * trip_lengt_2, flight_cost * trip_count * flight_per_trip ]

tourist_table_cost_2 = [tourist_day_cost_2 * trip_lengt_1,tourist_day_cost_2 * trip_lengt_2, flight_cost * trip_count * flight_per_trip ]

print("денег потраченно первым туристом", sum(tourist_table_cost_1))
print("денег потраченно вторым туристом", sum(tourist_table_cost_2))
print("денег осталось" , all_the_money - sum(tourist_table_cost_1) -sum(tourist_table_cost_2))

day_cost = tourist_day_cost_1 + tourist_day_cost_2

trip_cost = (trip_lengt_1 + trip_lengt_2) * day_cost

trip_cost += ((flight_cost * flight_per_trip) * trip_count) * tourist_count

if trip_cost > all_the_money:
    print("Внимание, наш бюджет не потянет такие траты, надо где-то сэкономить, у нас всего", all_the_money , "евро")

print("курс 1 евро =", ruble_exchange_rate_euro, "рублей")
print("мы потратим на поездку в евро" , trip_cost)
print("мы потратим на поездку в рублях" , trip_cost*ruble_exchange_rate_euro)

trip_tourist_1 = (trip_cost - ((trip_lengt_1 + trip_lengt_2) * tourist_day_cost_2)) - (flight_cost * flight_per_trip) * trip_count

print("первый турист потратил в евро", trip_tourist_1)

trip_tourist_2 = trip_cost - trip_tourist_1

print("второй турист потратил в евро", trip_tourist_2)

total_budget = all_the_money - trip_cost

if trip_cost > all_the_money:
    print("Путешествие не обошлось без кредитов, ваш общий долг в евро", total_budget)
else:
    print("Общие траты на путешествие в евро составили", trip_cost, "у вас осталось", total_budget, "евро")
