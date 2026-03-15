number  = int(input("Enter a number to see its divisors: "))
x = range(1, number+1)
div = []

for num in x:
    if number % num == 0:
        div.append(num) 
print(f"The divisors of {number} is {div}")

#    else:
#        print("Sorry, no divisors")
        

