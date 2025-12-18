try:
    num1 = int(input("eneter first number:"))
    num2 = int(input("eneter second number:"))
    result=num1/num2

except ValueError:
    print("please enter valid integers.")
except ZeroDivisionError:
    print("cannot divide by zero.")
finally:
    print("execution completed.")

    