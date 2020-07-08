#Excerise 5.2
#Attempting to get the max and min number in random sequence
largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done' : break
    try:
        number = float(num)
    except:
        print('Invalid input')
        continue
    if smallest is None or smallest > number:
        smallest = number
    elif largest is None or largest < number:
        largest = number
print("Maximum is", largest)
print("Minimum is", smallest)



