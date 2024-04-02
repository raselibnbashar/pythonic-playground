try:
    list = [36,0,3]
    result = list[0] / list[2]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Get Zero Division Error!")
except IndexError:
    print("Get Index Error!")
finally:
    print("Successfully")