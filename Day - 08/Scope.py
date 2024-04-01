#Scope

def outer_function():
    x=10
    def inner_function():
        y=5
        return x+y
    return inner_function()

print("Result :",outer_function())
