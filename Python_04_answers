1.  


#!/usr/bin/env python3
#Python_04 question 1

number = 100
while number < 101 and number > 0:
        print("number:" , number)
        number-=1
print("All done!")



2. 

#!/usr/bin/env python3
#Python_04 question  2



number = 4   
factorial_product = 4   

while number < 1001 and number > 0: 
        print("number:" , number, "factorial_product:", factorial_product)
        number-= 1
        factorial_product *= number

print("All done!")

****** this outputs the progression of the loop, so 1: 1000, 2: 1000*999, 3: 1000*998, etc




#!/usr/bin/env python3
#Python_04 question 2 


number = 1000
factorial_product = 1000

while number < 1001 and number > 1:
        number-= 1
        factorial_product *= number

print("number:" , number, "factorial_product:", factorial_product)
print("All done!")



**********this outputs the final factorial 


3. 


myscript12.py


#!/usr/bin/env python3
#Python_04 question 3

junkset = [101,2,15,22,95,33,2,27,72,15,52]

for junk in junkset:
        if junk % 2 ==0:
                print(junk)






4.  Sort the elements of the above list, then Iterate through each element and:

Print each element.
Calculate two cumulative sums, one of all the even values and one of all the odd values.
Print the two sums.


#!/usr/bin/env python3

#Python_04 question

junkset = [101,2,15,22,95,33,2,27,72,15,52]
sum_even = 0
sum_odd = 0

sorted = sorted(junkset)

for junk in sorted:
        print(junk)

for junk in sorted:
        if junk % 2 ==0:
                sum_even += junk

print("sum_even:", sum_even)

for junk in sorted:
        if junk % 2 !=0:
                sum_odd += junk

print("sum_odd:", sum_odd)



5. 

Use pop() and remove() with the list of integers.

pop()

Print your list before you start.
Store the value returned by pop().
Print the value and the list.
What happened to the orginal list?
remove()

Print your list before you start.
Store the value returned by remove().
Print the value and the list.
What happened to the orginal list?



>>> junkset = [101,2,15,22,95,33,2,27,72,15,52]
>>> print(junkset)
[101,2,15,22,95,33,2,27,72,15,52]
>>> pop_value=junkset.pop()
>>> print(pop_value)
52
>>> print(junkset)
[101, 2, 15, 22, 95, 33, 2, 27, 72, 15]


****** the original list had the last item removed


>>> junkset = [101,2,15,22,95,33,2,27,72,15,52]
>>> print(sorted(junkset))
[2, 2, 15, 15, 22, 27, 33, 52, 72, 95, 101]
>>> pop_remove=junkset.remove(72)
>>> print(junkset)
[101, 2, 15, 22, 95, 33, 2, 27, 15, 52]
>>> print(pop_remove)
None

****** original list has had 72 removed, but you cannot store the remove() value. printing the stored value returns 0. 

