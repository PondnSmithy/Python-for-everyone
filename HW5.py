product = {'3030' : {'price':500}, '3060': {'price':800} , '4040': {'price' : 900} , '4080':{'price' : 1000}}

while True:

    try:
        p = input("Please enter product:")
        q = int(input("Numbers: "))
        print('---------')

        if p in product:
            print(f'material: {p} price: {product[p]['price']}')
            print(f'Number is {q} So you have to pay {p} {product[p]['price']*q}')

    except ValueError:
        print("Value Error")
        break


    except:
        print("Please enter again")

    
