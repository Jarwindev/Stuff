def main():
    number = float(input("Enter a number: "))
    if number < 0:
        print("Error: Cannot compute the cube root of a negative number.")
    else:
        print(f"The cube root of {number} is approximately {cube_root(number):.2f}")

def cube_root(number):   
    return number ** (1/3)
    
if __name__ == "__main__":
    main()