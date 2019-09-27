'''
When you're coding, you want to be doing your "actions" inside of functions.
You are usually using your "global" space to put in very specific values.
Here's an example.
'''

import random

def modifier_function (input1, input2):
    '''
    For simplicity, I've named the inputs to this function input1 and input2 to drive home the concept
    that each function has inputs. You can call them whatever you want.
    Think of it as, the function will take whatever object you give it, and the function will refer to it
    as input1 (or input2 or whatever you put the name there) and that reference will only exist INSIDE the function.
    '''
    for i in range(0, len(input1)): #iterate through each value input1
        input1[i] += 1 #modify that value by increasing it by 1

    while(input2): #shows you that input1 and input2 don't have to be the same type of object
        print("Infinite loop.") #here input2 is obviously a boolean value (True, False)

    return input1 #this function returns your input1. From the for loop, you should know that input1 is a list of sorts.

def generator_function (input):
    '''
    I think the idea of a generator makes sense. Take a look.
    '''
    output = [0]*input #input here is an integer value, output here is define IN the function.
    for i in range(0, len(output)): #iterate through the list output.
        output[i] = random.randint(1,10) #think about what this does
    return output

def observer_function (input):
    '''
    This would be an observer function. They still "return" a value, but these are generally boolean (T/F)
    '''
    if len(input) == 0: #can you explain what this function does?
        return True
    else:
        return False

def observer_function_2 (input):
    '''
    This is an example of an observer function that does not return anything.
    '''
    if len(input) == 0:
        print("I had a good day")
    else:
        pass

if __name__ == "__main__": #don't worry about what this means, just know that everything past this is "global"
    array1 = generator_function(10) #it's a generator because it takes an integer input, but your output is something new.
                                    #it "generated" (made something new) an array
    print("Generated array: ", array1)
    #you stored the array generated by the function as array1.
    array1 = modifier_function(array1, False) #here the modifier changes the values of the array you put in. You don't get something new as an output.
    #you can store this array under a new name, but I kept it the same to emphasize the idea of a "modifier."
    print("After modified: ", array1)

    obs = observer_function(array1)
    print(obs)
    observer_function_2 #do you understand why I don't save observer_function_2 to a variable name?