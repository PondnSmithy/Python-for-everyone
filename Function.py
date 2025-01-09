def hello(friend):
    print("Hi, {}".format(friend))

def land(width,long):
    cal = width*long
    print("Width: {} Long: {}".format(width,long))
    print("Area: {}".format(cal))
    return cal

hello("Pond")
result = land(10,15)
print(result)