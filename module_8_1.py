def add_everything_up(a, b):
    try:
        res_= a + b
    except TypeError:
        res_ = str(a) + str(b)
    else:
        res_ = a + b
        res_ = round(res_, 3)
    return res_

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))