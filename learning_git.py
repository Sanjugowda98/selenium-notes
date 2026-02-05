
class Evenodd:
def even_odd(start,end):
    for num in range(start,end):
        if num%2==0:
            print(f"{num}is even")
        else:
            print(f"{num}is odd")
obj=Evenodd()
obj.even_odd(10,20)
