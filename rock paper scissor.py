import random
def choice():
	print('Press 1 for rock')
	print('Press 2 for paper')
	print('Press 3 for scissor')
	i=int(input('enter your choice : '))
	if(i==1):
		print( name , 'chose rock')
	elif(i==2):
		print(name, 'chose paper')
	elif(i==3):
		print(name, 'chose scissor')
	else:
		print('plea enter correct plea ')
		choice()
	return i
	
def botchoice():
	j=random.randint(1,3)
	if(j==1):
		print('Computer chose Rock')
	elif(j==2):
		print('Computer chose Paper')
	elif(j==3):
		print('Computer chose Scissor')
	return j
	
def play():
	n=int(input('enter total points : '))
	ms=cs=0
	r=1
	c=5
	while(ms<n and cs<n and c== 5):
		print()
		print('Round -', r)
		a=choice()
		b=botchoice()
		if (a==1 and b==3 or a==2 and b==1 or a==3 and b==2):
			print(name, 'won !')
			ms+=1
		elif(a==b):
			print ('Draw !')
		else:
			print('computer won')
			cs+=1
		print(name,"'s score :", ms)
		print("computer's score :",cs)
		r+=1
		c=int(input('Enter 5 to continue :'))
	print('Result')
	if ms > cs :
		print('Congratulations', name ,'won !!!')
	else:
		print(name,'lost , computer won')
		
#global 
print('Welcome to Rock-Paper-Scissor')
name=input('enter your name : ')
play()
