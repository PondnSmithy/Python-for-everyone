salary = {'base':21000,'allowance':2000,'food':450}

print("-----Program calculate about salary-------")

try:
    month = int(input("How many month that your work in here :"))
    diligence = int(input("How many day that you didn't come:"))

except:
    print("Please enter only int")
    month = int(input("How many month that your work in here :"))
    diligence = int(input("How many day that you didn't come:"))

print('----Cal----')

if diligence > 0:
    salary['allowance'] = 1000
    print("Minus 1000 Baht")
    print(f"Your revenue have base:{salary['base']} \nallowance:{salary['allowance']} \nfood:{salary['food']}")
else:
    print(f"Your revenue have base:{salary['base']} \nallowance:{salary['allowance']} \nfood:{salary['food']}")

total_revenue = salary['base']*month+salary['allowance']*month+salary['food']
print(f"Total revenue: {total_revenue}")
