marks = int(input("Enter marks: "))
if marks < 40:
    grade = 'F'
elif marks < 50:
    grade = 'D'
elif marks < 70:
    grade = 'C'
elif marks < 90:
    grade = 'B'
else:
    grade = 'A'

print(grade)
    
