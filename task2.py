def salam():

    name = input("Adınızı daxil edin: ")
    
    print(f"Salam, {name}! Uğurlar.")

salam()

def sum_numbers(a, b):
    return a + b

nəticə = sum_numbers(15, 5)
print("Cəmi:", nəticə)

def account_average(value):

    return sum(value) / len(value)

qiymətlər = [83, 22, 74, 97]

ortalama = account_average(qiymətlər)
print("Ortalama bal:", ortalama)
