try:  
    with open("students.txt", "r") as file:  
        print("Reading Student Information:\n")  
        print(file.read())  
except FileNotFoundError:  
    print("Error: 'students.txt' not found.")  