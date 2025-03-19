def divide(a, b):
    return None if b == 0 else a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    return None if b == 0 else a % b

def summation(a, b):
    return None if a > b else sum(range(a, b + 1))

def main():
    while True:
        choice = input("Choose [D]ivide, [E]xponentiate, [R]emainder, [F] Summation, [Q]uit: ").strip().upper()
        if choice == 'Q':
            break
        
        try:
            a, b = map(float, input("Enter two numbers: ").split())
            operations = {'D': divide, 'E': exponentiate, 'R': remainder, 'F': summation}
            result = operations.get(choice, lambda x, y: None)(int(a), int(b))
            print("Result:", result if result is not None else "Invalid input")
        except ValueError:
            print("Invalid input. Enter numeric values.")

if __name__ == "__main__":
    main()
