## Add code below with answer clearly stated
num = 100 #Your factorial value
factorial = 1 #Variable for finding factorial
add = 0 #variable for summition of digit in number "num"

for i in range(1,num + 1): #this loop is for finding the factorial of number "num"
   factorial = factorial*i #factorial formula num! = num * (num + 1)
for integer in str(factorial): #this loop is to calculate the sum of the digit in number "num"
      add += int(integer) #adding all the digits in number "num"
        
print("Factorial of",num,"=",factorial)
print("Sum of the digit in number 100! =",add)

##Output of the above code
Factorial of 100 = 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208
27223758251185210916864000000000000000000000000
Sum of the digit in number 100! = 648
