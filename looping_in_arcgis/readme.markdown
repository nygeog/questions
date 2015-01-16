#ArcGIS Scripting Question?
##Looping vs. Line by Line code

It's become apparent to me that there is some sort of memory leaks that show up in ArcPy when doing nested or even regular loops. 

Tasks take much longer the more a loop iterates.


When you're writing scripts in AML or whatever, do you write them as such with loops:

	listData = ('1','2','3','4','5')
	
	for i in listData:
		codeProcess('data'+i,'data'+i+'out')


Or do you do it line by line.

	codeProcess('data1','data1out1')
	codeProcess('data2','data1out2')
	codeProcess('data3','data1out3')
	codeProcess('data4','data1out4')
	codeProcess('data5','data1out5')	
	
I'm aware of tools like GarabageCollector but it just seems like an annoyance to do this when its almost just easier (and efficient) to write a loop to generate the code that would run line by line. 