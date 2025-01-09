def calculate_ot(salary,normal,special = None):
 
    daily_wage = salary/(30*8)
    rate_normal = 1.5
    rate_special = 3
    sum_normal = daily_wage*rate_normal*normal
    sum_special = 0

    if special:
        sum_special = special*rate_special*daily_wage

    sum = sum_normal+sum_special+salary
    sum_ot = sum_normal+sum_special
    hours = normal+special
    return sum,sum_ot,hours

def receive(value):
    try:
        return int(input(value))
    except ValueError:
        return 0
    
salary = receive("Please enter your salary : ")
welfare = receive("Please enter your welfare : ")
ot_normal = receive("Please enter your OT(1.5) : ")
ot_special = receive("Please enter your OT(3) : ")


money,ot,hours = calculate_ot(salary+welfare,ot_normal,ot_special)
print("This month you get :",money,"baht")
print("This month you get OT :",ot,"baht")
print("This month you work in OT :",hours,"hrs")