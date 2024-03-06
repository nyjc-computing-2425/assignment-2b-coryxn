num = input('Enter a number (decimal only): ')
dot_pos = num.find('.') # find dot position
num1 = num[dot_pos+1:] # all numbers after dot
dp = len(num1) # length
print('The number', num, 'has', dp, 'decimal places.')