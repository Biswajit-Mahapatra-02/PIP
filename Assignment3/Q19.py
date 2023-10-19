def compute_average():
    total = 0
    count = 0
    
    while True:
        value = float(input("Enter a value (or 0 to finish): "))
        
        if count == 0 and value == 0:
            print("Error: The first value cannot be 0.")
            continue
        
        if value == 0:
            break
        
        total += value
        count += 1
    
    if count > 0:
        average = total / count
        print(f"The average of the {count} values is: {average}")
    else:
        print("No values provided.")

compute_average()