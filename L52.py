# Anastacia Aguirre & Abigail Lopez

def perfect(n):
    total=0
    for number in range(1,n):
        if n%number==0:
            total=total+number
    if total==n:
        return True


def is_it_perfect():
    n=int(input("Give me a number."))
    for numbers in range(1, n):
        if perfect(numbers) == True:
            print(numbers)

is_it_perfect()

