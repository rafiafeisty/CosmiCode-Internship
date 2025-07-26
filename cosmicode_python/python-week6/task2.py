import math

def calculations(a,b):
    try:
        a = float(a)
        b = float(b)

        sqrt_res_a=math.sqrt(a)
        sqrt_res_b=math.sqrt(b)
        print("Sqaure Root of first number: ", sqrt_res_a)
        print("Sqaure Root of second number: ", sqrt_res_b)
        print("\n")

        div_res=a/b
        print("Division of first number by second number: ", div_res)
        print("\n")

        log_a=math.log(a)
        log_b=math.log(b)
        print("Logarithm of first number: ", log_a)
        print("Logarithm of second number: ", log_b)
        print("\n")

        power=math.pow(a,b)
        print("Power of first number by second number: ", power)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError:
        print("Error: Invalid input. Please enter a number")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number")
    except Exception as e:
        print("An error occurred: ", str(e))
    finally:
        print("Program execution completed")


calculations(25, 5)
print("\n--- Test with zero division ---")
calculations(10, 0)
print("\n--- Test with negative input for sqrt/log ---")
calculations(-16, 2)
print("\n--- Test with invalid type ---")
calculations("abc", 2)