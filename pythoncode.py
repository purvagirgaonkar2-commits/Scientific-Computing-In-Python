# ==========================
# Program 1: Student Mark Manager
# ==========================
def student_mark_manager():
    print("=== Student Mark Manager ===")
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    
    total = sum(marks)
    average = total / n
    highest = max(marks)
    lowest = min(marks)
    
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")
    print(f"Even marks count: {len([m for m in marks if m % 2 == 0])}")
    print(f"Odd marks count: {len([m for m in marks if m % 2 != 0])}")
    print("\n")

# ==========================
# Program 2: Number Analyzer
# ==========================
def number_analyzer():
    print("=== Number Analyzer ===")
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Even Numbers: {even}")
    print(f"Odd Numbers: {odd}")
    print(f"Maximum Number: {max(numbers)}")
    print(f"Minimum Number: {min(numbers)}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print("\n")

# ==========================
# Program 3: Simple Calculator
# ==========================
def simple_calculator():
    print("=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operation!")
        return
    
    print(f"Result: {result}")
    print("\n")

# ==========================
# Main Menu to choose programs
# ==========================
def main():
    while True:
        print("Choose a program to run:")
        print("1. Student Mark Manager")
        print("2. Number Analyzer")
        print("3. Simple Calculator")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            student_mark_manager()
        elif choice == '2':
            number_analyzer()
        elif choice == '3':
            simple_calculator()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the main menu
if __name__ == "__main__":
    main()



    
