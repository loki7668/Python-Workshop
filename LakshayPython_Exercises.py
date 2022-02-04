
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    
    # ** What is 7 to the power of 4?**
    
    return pow(a,b)
print(power(7,4))




def split_str(s):
    
    # ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

    return (s.split()) 
print(split_str("Hi there Sam!"))




def format(planet,diameter):
    
# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

    return "The diameter of {} is {} kilometers.".format(planet,diameter)
print(format("Earth",12742))




def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

    return list[3][1][2][0]
print(indexing([1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]))




def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


    return d['k1'][3]['tricky'][3]['target'][3]
print(dictionary({'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}))




def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is ________
print('Tuple is immutable')
    return None
subjective()




def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

    return email.split('@')[-1]
print(domainGet('user@domain.com'))


def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

    return 'dog' in st.lower().split()
print(findDog('That dog is grat'))




def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
 count = 0
 for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count
print(countDog('Dog is a  good animal dog is a very good pet'))




def lambdafunc(seq):
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

    return list(filter(lambda word: word[0]=='s',seq))
print(lambdafunc(['soup','dog','salad','cat','great']))



def caught_speeding(speed, is_birthday):
    
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **
 if is_birthday:
        speeding = speed - 5
 else:
        speeding = speed
    
 if speeding > 80:
  return 'Big Ticket'
 elif speeding > 60:
  return 'Small Ticket'
 else:
  return 'No Ticket'
print(caught_speeding(65,True))


## Numpy Exercises


import numpy as np
def create_arr_of_fives():
  #### Create an array of 10 fives
a1=np.ones(10)*5
  #### Convert your output into list 
  #### e.g return list(arr) 
  return list(a1)
print(create_arr_of_fives())




import numpy as np
def even_num():
  ### Create an array of all the even integers from 10 to 50
a1=np.arange(10,51,2)
  ### Convert your output into list 
  ### e.g return list(arr) 
  return return list(a1)
print(even_num())



import numpy as np
def create_matrix():
  ### Create a 3x3 matrix with values ranging from 0 to 8
a1=np.arange(0,9).reshape(3,3)
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  return list(a1)
print(create_matrix())



import numpy as np
def linear_space():
  ### Create an array of 20 linearly spaced points between 0 and 1
arr= np.linspace(0,1,20)
  ### Convert your output into list 
  ### e.g return list(arr) 
  return list(arr)
print(linear_space())



import numpy as np
def decimal_mat():
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
arr=np.linspace(0.01,1,100).reshape(10,10)
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  return list(arr)
print(decimal_mat())



import numpy as np
def slices_1():
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])
  return list(arr[2:5,1:5])
print(slices_1())



import numpy as np
def slices_2():
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[ 2],
  #      [ 7],
  #      [12]])
  return list(arr[0:3,1:2])
print(slices_2()) 



import numpy as np
def slices_3():
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  return list(arr[3:5,0:5])
print(slices_3()) 


# Great job!
