# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками

def card_show(num_1:str):
    print(num_1)
    print ('*' * len(num_1[:-4]) + num_1[-4:])

def palindrome(data):
    data = data.replace(' ','').lower()
    if data == data[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")




def main ():

    card_show("1111444477778888")
    print(palindrome(data="Шабаш"))



main ()








