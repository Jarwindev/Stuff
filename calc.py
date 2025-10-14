def main():
    import argparse
    parser = argparse.ArgumentParser(description="Perform basic arithmetic operations.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="The operation to perform.")
    parser.add_argument("num1", type=float, help="The first number.")
    parser.add_argument("num2", type=float, help="The second number.")
    
    args = parser.parse_args()
    
    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "subtract":
        result = args.num1 - args.num2
    elif args.operation == "multiply":
        result = args.num1 * args.num2
    elif args.operation == "divide":
        if args.num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = args.num1 / args.num2
    
    print(f"The result of {args.operation}ing {args.num1} and {args.num2} is: {result}")

if __name__ == "__main__":
    main()