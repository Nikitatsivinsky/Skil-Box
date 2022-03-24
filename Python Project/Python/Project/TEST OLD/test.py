from colorama import init
from colorama import Fore, Back, Style
init()

print( Fore.BLACK)
print( Back.GREEN)

what = input( "что деалем? (+, -):  ")

print( Fore.BLACK)
print( Back.CYAN)
a = float( input( "Первое число: ") )
b = float( input( "Второе число: ") )

if what == "+":
	c = a + b 
	print( Fore.BLACK)
	print( Back.GREEN)
	print("Результат " + str(c) ) 
elif what == "-":	
	c = a - b 
	print( Fore.BLACK)
	print( Back.GREEN)
	print("Результат " + str(c) ) 
else:
	print( Fore.BLACK)
	print( Back.RED)
	print("Выбрана не верная операция")
input()

