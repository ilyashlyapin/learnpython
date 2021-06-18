def weather(temperature):
    if temperature < 0:
        return 'На улице холодно!'
    elif 0 <= temperature <= 15:
        return 'На улице прохладно'
    elif 15 <= temperature <= 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'


print(weather(30))
