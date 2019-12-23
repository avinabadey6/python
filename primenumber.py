from time import perf_counter
n= int(input("Enter number to check for primality: "))
is_prime=True
t1_start = perf_counter()
for i in range(2, n//2): 
  if (n % i == 0): 
    is_prime=False

t1_stop = perf_counter()
print("Time taken:", t1_stop-t1_start)

if is_prime==True:
  print("it is prime")
else:
  print("not prime")

# 6700417 takes 1.3sec
# 2147483647 [not checked]
# 67280421310721 [not checked]


