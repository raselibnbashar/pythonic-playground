#xargs
def add(*numbers):
    sum = 0

    for num in numbers:
        sum = sum + num
    print(sum)
    

add(1,2)
add(10,20,30)
add(10,20,30,40)