ename = input("Enter Employee Name: ")
empid = input("  Enter Employee ID: ")
empsalary = int(input(" Enter Employee Salary (Monthly): "))
leave = int(input( "Enter Leave (Days): "))
month = int(input("Enter Month: "))
tds = int(input("enter tds%: "))
year =int (input("enter year: "))


print('Employee Name =  ', ename)
print('Employee ID =  ', empid)
print('Employee Monthly Salary = ', empsalary)
ctc = empsalary*12
print('CTC(Monthly Salary) = ',ctc)
if month == 1 or month ==3 or month ==  5 or month == 7 or  month == 8 or month == 10 or month == 12:
           day_salary = empsalary / 31
else:
         day_salary = empsalary / 30

print('Day Salary = ', day_salary)
leave_amount = leave * day_salary
print('leave Amount = ',leave_amount)

tds = (empsalary - leave) * (tds/100)
print("tds % : ", tds)

final_pay_salary = (empsalary - leave_amount -  tds)
print("final_pay_salary: ",final_pay_salary)

