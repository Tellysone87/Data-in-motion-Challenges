# 
# Write a Python function that takes a number as input and checks if it is prime. 
# A prime number is a natural number greater than 1 that is divisible only by 1 and itself.
# 

def prime(num):
   i = 2 #set the counter to 2 becasue all number are divisable by 1 without question
   j = 0

   if num < 0: # catches case where the number provided is less than 0 
       return "Not prime"
   
   while i < num: # loop through numbers between 1 and the actual number
       if num % i == 0: # check if it is divisible by the current loop number
           j+=1
           print(i)
       i+=1

   if j > 0:
       return "Not prime"
   else:
       return "Prime"
       
def main():
    print(prime(36))
    print(prime(7))
    print(prime(11))

main()