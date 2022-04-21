driving = input('Have you dirven a car?')
if driving != 'yes' and driving != 'no':
	print('Only enter yes or no.')
	raise SystemExit
		
age = input('What is your age?')
age = int(age)
if driving == 'yes':
    if age >= 18:
    	print('You pass the exam')
    else:
        print('Error!')
elif driving == 'no':
	if age >= 18:
		print('You could get the driving test.')
	else:
		print('Not bad, you could get the test in years.')	