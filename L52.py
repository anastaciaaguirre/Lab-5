# Anastacia Aguirre & Abigail Lopez

def perfect(n):
    total=0
    for number in range(1,n):
        if n%number==0:
            total=total+number
    print(total==n)


def is_it_perfect():
    n=int(input("Give me a number."))
    perfect(n)

is_it_perfect()
