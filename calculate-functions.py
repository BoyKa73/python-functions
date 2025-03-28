#defintions
def add_numbers(number1, number2)
    return number1 + number2
#return sum
#test

a = 10
b = 20


add_numbers(number1=a, number2=b)
#add_numbers(a,b)

c = add_numbers (a, b)
   print(f"Die Summe von a={a} und b={b} ist {c}.")






def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"