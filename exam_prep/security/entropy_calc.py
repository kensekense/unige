import math
def entropy_ (X, y):
 sum = 0.0
 for i in range(0,len(X)):
  pi = X[i]*y
  sum += pi*math.log(pi,2)
 return -1*sum

if __name__ == "__main__":
 b = 34/120
 a = [1/4,3/20,6/10]
 print(entropy_(a,b))

 b = 1/4
 print(entropy_(a,b))
