####  1

philosophy = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


better_count = philosophy.count('better')
never_count = philosophy.count('never')
is_count = philosophy.count('is')
print(is_count)


philosophy_upper = philosophy.upper()
print(philosophy_upper)


philosophy_change = philosophy.replace("i", '&')
print(philosophy_change)


#  2 

number = 5483

product = 1 
for i in str(number):
    product = product * int(i) 

print(product)


reversed_number = ''

for i in str(number)[::-1]:
    reversed_number += i
reversed_number = int(reversed_number)
print(reversed_number)

# 3

str_number = list(map(int, str(number)))

str_number.sort()
print(str_number)



ready_number = ''

for i in str_number:
    ready_number += str(i)
ready_number = int(ready_number)
print(ready_number)

