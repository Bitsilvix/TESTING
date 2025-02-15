n=input("number")
#попытаться
try:
    n=int(n)
    print(n/0)
#исключение 
except ValueError:
    print("number")
except ZeroDivisionError:
    print("zero")
except (ValueError+ZeroDivisionError):
    print("mistake")