#Ask the user for their date of birth
dob = input('Please enter date of birth in the \'YYYYMMDD\' format: ')

#Digit of Life
temp = 0
DOL = 0

#Calculate the Digit of Life
for ch in dob:
    temp += int(ch)

if temp > 9:
    while temp > 9:
        for digit in str(temp):
            DOL += int(digit)
        temp = DOL
            
if temp <= 9:
    DOL = temp
    print('Digit of Life: ', DOL)