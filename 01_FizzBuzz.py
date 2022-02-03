# Question:
# Suppose we have a number n. We have to find a string that is representing all numbers from 1 to n, but we have to follow some rules.
# When the number is divisible by 3, put Fizz instead of the number
# When the number is divisible by 5, put Buzz instead of the number
# When the number is divisible by 3 and 5 both, put FizzBuzz instead of the number
# Answer:

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if((i%3 != 0) & (i%5 !=0)):
            print(i)
        elif((i%3==0) & (i%5==0)):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        else:
            print(i)    
        
           

if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)
