with open('myfile2.txt','r') as f,open('myfile.txt','r') as f2:
	
	'''for line in f:
		print(line,end='')

	f_contents=f.readline()
	print(f_contents, end='')

	f_contents=f.readline()
	print(f_contents,end='')'''

	f_contents=f.read(15)
	print(f_contents)

	f_contents2=f2.readline(15)
	print(f_contents2)



