print('Доброе утро, укажите возраст:')
age = input()

def age_direction(age):
    age = int(age)
    if age <= 6:
        print("Если ваш возраст " + format(age) + ", то Вам пора в садик")
    if 7 <= age <= 17:
        print("Если ваш возраст " + format(age) + ", то Вам пора в школу")
    if 18 <= age <= 23:
        print("Если ваш возраст " + format(age) + ", то Вам пора в ВУЗ")
    else:
        print("Если ваш возраст " + format(age) + ", то Вам пора на работу")


age_direction(age)
