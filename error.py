try:
    a,b= eval(input("Enter two numbers seperated by commas"))
    result= a=b
    print(result)
except ZeroDivisionError:
    print("division by 0 is error")
except SyntaxError:
    print(",is missing")
except:
    print("wrong inpute")
finally:
    print("THIS WILL EXCUTE NO MATTER ")