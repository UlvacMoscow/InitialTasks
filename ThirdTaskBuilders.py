#3) Напишите программу на python, которая "выполняет" вот этот анекдот:
#Идет по улице прохожий, смотрит - на газоне двое рабочих. Первый выкапывает яму,
#ждут, второй закапывает. Перекур. Потом все повторяется.
#Прохожий не выдерживает: "Мужики, а что вы делаете-то?"
#Ну понимаешь, вообще мы деревья сажаем. Я выкапываю яму, Петрович кладет туда саженец,
#Серега закапывает. А сегодня Петрович заболел...
#3.1) Написать "правильный" цикл, как сажают деревья.
#Выход из цикла - по окончании рабочего дня. Сколько у рабочих было саженцев - мы не знаем.
#3.2) Сделать так, что Петрович заболел: добавить условие по вводу с клавиатуры. Совет: используйте цикл while.

working_hours = 0
long_work_day = 8
worker_dig_pit_time = 0.6
serega_bury_pit_time = 0.4
petrovich_working_time = 0.3
timeout = 0.1
seedling_amount = 0

while True:
    petrovich_status = input ("Как вы думаете болен петрович сегодня? введите \"да\" или \"нет\", а если не хотите смотреть на то как другие работают напишите \"стоп\"")
    if petrovich_status.lower() == "стоп":
        print("работа остановлена")
        break

    if petrovich_status.lower() == "да":
        while working_hours < long_work_day:
            working_hours = working_hours + worker_dig_pit_time + serega_bury_pit_time
            print("Мужики перекопали ям", working_hours, "часа, а Петрович тем временем валялся с температурой")
            working_hours += timeout
            print("Мужики перекурили, времени с начала рабочего дня прошло", working_hours,"часа")
        if working_hours > long_work_day:
            print("мужики сегодня переработала на",  working_hours - long_work_day, "часов, правда они ничего не посадили, но это уже детали, на работу пришел значит работаешь.")
            print("рабочий день закончен")
        break

    if petrovich_status.lower() == "нет":
        while working_hours < long_work_day:
            working_hours = working_hours + worker_dig_pit_time + serega_bury_pit_time + petrovich_working_time
            seedling_amount = seedling_amount + 1
            print("Мужики посадили саженцев", seedling_amount,"за", working_hours, "часа")
            working_hours += timeout
            print("Мужики перекурили, времени с начала рабочего дня прошло", working_hours,"часа")
        if working_hours > long_work_day:
            print("мужики сегодня переработала на",  working_hours - long_work_day, "часов и посадили", seedling_amount, "саженцев")
            print("рабочий день закончен")
        break