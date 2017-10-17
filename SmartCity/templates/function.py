



def write_func():
	f = open('example.txt', 'w+')


	for i in range(10):
		f.write('EXAMPLE %d\n' %(i))
		
	f.close()

	
if __name__ == '__main__':
	write_func()