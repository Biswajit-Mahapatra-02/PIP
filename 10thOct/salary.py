import sys
salary = float(sys.argv[1])
da = 0.40 * salary
print(f'DA: {da}')
hra = 0.20 * salary
print(f'HRA: {hra}')
gsalary = salary + da + hra
print(f'The gross salary is {gsalary}')