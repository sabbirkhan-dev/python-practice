"""   
# global_variable 

global_variable = 66

def fn1 ():
    # enclosing scope
    enclosed_variable = 10
    
    def fn2 ():
        # local_variable 
        local_variable = 5
        
        print("Accesss to global v local", global_variable)
        print("Accesss to enclosing v local", enclosed_variable)
        print("Accesss to local v", local_variable)
     
    fn2() # inner function call
    
    print("Accesss to global v enclosing", global_variable)
    print("Accesss to enclosing v enclosing", enclosed_variable)
    
fn1() # outer """


def get_total(a, b):
    total = a + b

    def double_it():
        double = total * 2
        return double

    doubled = double_it()
    print(doubled)

    return total

print(get_total(23, 2))

