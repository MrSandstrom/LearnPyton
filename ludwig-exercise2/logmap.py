def logmap(r,x):    
    return (r*x*(1-x))

#print(logmap(float(3.9),float(0.20)))

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
#
# Implement the function same_ends which given a list returns True/False depending on whether the first and the last elements in the list are the same. 
# For example, same_ends(['A','B','C','D','A']) must be True. The function must return False if the list has no elements
#


def same_ends(array):
    length = len(array)
    
    if length == 0:
        return False
    
    startPos = 0
    endPos = length -1

    if array[startPos] == array[endPos]:        
        return True
    else:
        return False

    

# array = []
array = ['A','B','C','D','B','A']
#print(same_ends(array))


#--------------------------------------------------------------------

#
# All Internet pages are written in the language HTML, where plain text is intermixed with tags which encode formatting instructions. 
# For example <b>attention</b> indicates that the page should show the text 'attention' in bold font. 
# Similarly <i>attention</i> indicates italic style.
#
# Implement the function tag for adding tags to text, e.g. tag('b','hello') must return '<b>hello</b>'

def tag(b, hello):
    value = "<" + b + ">"
    return value+hello+value

#print(tag('b','hello'))


#--------------------------------------------------------------------
#
# Given a list with an even number of elements, generate a new list where the first and the second halves of the original are swapped.
# For example, swap([1,2,3,4]) must return [3,4,1,2].

def swap(array):
    half = int(len(array)/2)
    first_half = array[0:half] 
    second_half = array[half:len(array)]
    result = second_half + first_half
    return result

print(swap([1,2,3,4,5,6]))

















