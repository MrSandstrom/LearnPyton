def logmap(r,x):    
    return (r*x*(1-x))

print(logmap(float(3.9),float(0.20)))

#--------------------------------------------------------------------


def experiment(r,x,n):
    print (x)
    for i in range(n-1):
        value = r*x*(1-x)
        x = value
        print (x)
        
# logmap function = rx(1-x)
# experiment case add n
# experiment(float(3.9),float(0.20),10)

#--------------------------------------------------------------------



def table(r,x1,x2,n):
    print (x1, x2)
    for i in range(n-1):
        value1 = r*x1*(1-x1)
        value2 = r*x2*(1-x2)
        x1 = value1
        x2 = value2
        print (x1, x2)


#table(float(3.9),float(0.20),float(0.21),10)

#--------------------------------------------------------------------