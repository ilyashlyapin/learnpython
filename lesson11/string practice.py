def lines_sum(line1, line2):
    if type(line1) != str:
        return 0
    elif type(line2) != str:
        return 0
    elif line1 == line2:
        return 1
    elif line1 != line2 and len(line2) > len(line1):
        return 2
    elif line1 != line2 and line2 == 'learn':
        return 3
    else:
        print("hi")


not_str = lines_sum(1, 2)
print(not_str)
equal = lines_sum('hello', 'hello')
print(equal)
secondmore = lines_sum('hell', 'hello')
print(secondmore)
notequals_secondlearn = lines_sum('leard', 'learn')
print(notequals_secondlearn)

