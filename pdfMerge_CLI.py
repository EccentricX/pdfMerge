import os
def oS():
	global S
	S=''
	s=input('Enter the directory of the file:');print()
	s+='\\'
	for os1 in s:
		if os1=='\\':
			S+='/'
		else:
			S+=os1
	os.chdir(S)
	global a
	a=os.listdir(S)
	global OS_dict
	global OS_dict_len
	OS_dict={}
	OS_Id=1
	for os2 in a:
		if len(os2)>4:
			if os2[-4]+os2[-3]+os2[-2]+os2[-1]=='.pdf':
				OS_dict[OS_Id]=os2
				OS_Id+=1
	for os3 in OS_dict:
		print(os3,'.',OS_dict[os3])
	OS_dict_len=len(OS_dict)
oS()

#

import datetime as dt
d=dt.datetime.today()
DaTe=d.today()
DaTeMoD=str(DaTe.day)+'-'+str(DaTe.month)+'-'+str(DaTe.year)+'   '+str(DaTe.hour)+' hr :'+str(DaTe.minute)+' min '+str(DaTe.second)+' sec'
def show3():
	file=open(' .txt','r')
	tyyt=file.read()
	if len(tyyt)!=0:
		print('This is a list of data about when and at what time you ran this program\n')
		print(tyyt)
	else:
		print('You Might Be the 1st user of this program or data may be lost or file may be deleted by mistake.')
	file.close()
code=input('\n\t\tWant to use, hit enter button:');print()
if code!='' and code=='6204961992':
	show3()
elif code=='':
	pass
else:
	exit()
def show():
                        f=open('HELPING GUIDE FOR USING PDF MERGER.html','w')
                        data=f.write('<HTML>\n')
                        data=f.write("<A HREF='https://drive.google.com/file/d/121Eu5OFVGEyhusmgPIGGnk3lo7ei7tGF/view?usp=drivesdk'><font size='200' face='ALGERIAN' color=''RED'><B><U>CLICK TO OPEN GUIDE SHEET</U></B></font></br></A>\n")
                        data=f.write("<A HREF='https://drive.google.com/file/d/12j7RbFWAjuj8HOcSXqvPP-qffmAWCqWx/view?usp=drivesdk'><font size='200' face='ALGERIAN' color=''RED'><B><U>CLICK TO GET PYTHON CODE OF THIS PROGRAM</U></B></font></A>\n")
                        data=f.write('</BODY>\n')
                        data=f.write('</HTML>\n')
                        f.close()
def show2():
	print('Welcome every one to another program.\nIn ths program you can merge your multiple PDF files into one single file.');print();print('\tHaving a tutorial guide? If yes press enter else\n Enter your name and then press enter.')
	o=input()
	if o!='':
		print('\n\t\t\tHi,'+o);print()
		show()
		print('A guide linked file is saved where this program is saved.\nClick on the link to open the guide file.')
		print()
		kkk=input('Read the Guide? If yes, press enter else 1st read the guide and then press enter')
		print(kkk)
	else:
		print('Hi,'+o)
		input('Want to Start press Enter')
		print()
def T():
        from time import time
        ti=time()
        while True:
                n=time()-ti
                if n<2:
                        pass
                else:
                        print(':'*67);print()
                        PDF()
                        qwerty=DaTeMoD+'\n'
                        file=open(' .txt','r')
                        for i in (file.readlines()):
                        	if i==qwerty:
                        		pass
                        		file.close()
                        	else:
		                        file=open(' .txt','a')
		                        data=file.write(qwerty+'\n')
		                        file.close()
def PDF():
        try:
        	file=open(' .txt','r')
        	file.close()
        	file=open(' .txt','a')
        	data=file.write(DaTeMoD)
        	data=file.write('\n')
        	file.close()
        except:
        	file=open(' .txt','a')
        	data=file.write(DaTeMoD)
        	data=file.write('\n')
        	file.close()
        	show2()
        try:
                import PyPDF3 as P
                B=[]
                os5=[]
                os7={}
                os9=[]
                global N
                N=[]
                y=int(input('Enter the number of PDF file want to merge:-'))
                if y<OS_dict_len:
                        for os6 in range(y):
                                os5.append(int(input('Enter corressponding code : -')))
                        for os8 in range(y):
                                os7[os5[os8]]=OS_dict[os5[os8]]
                                os9.append(S+OS_dict[os5[os8]])
                elif y==OS_dict_len:
                	os7=OS_dict
                	for os10 in OS_dict:
                		os5.append(os10)
                else:
                        print('\n\tEntered no. of Elements doesn\'t exists!!!')
                        input()
                        exit()
                print()
                for i in range(y):
                        x=os7[os5[i]]
                        B.append(P.PdfFileReader(x))
                        N.append(x)
                pdfWriter=P.PdfFileWriter()
                print()
                print('1.)  For attaching pdf document end-to-end.')
                print('2.)  For attaching the random pages of pdf document.')
                print('3.)  For attaching pages serially from 1st page of pdf document.')
                print('4.)  For attaching pages randomlly and end-to-end mixed.')
                print('5.)  For attaching range of pages.')
                print()
                m=int(input('Select Option:-'))
                print()
                if m==1:
                        for j in range(y):
                                for a in range(B[j].numPages):
                                        pageObj=B[j].getPage(a)
                                        pdfWriter.addPage(pageObj)
                if m==2:
                        A=[]
                        for j in range(y):
                                k=input('No. of random pages want to attach from  '+str(N[j])+' :-')
                                for h in range(int(k)):
                                        A.append(int(input('\tEnter the page no.:-')))
                                for a in A:
                                        pageObj=B[j].getPage(a-1)
                                        pdfWriter.addPage(pageObj)
                if m==3:
                        for j in range(y):
                                for a in range(int(input('No. of pages want to attach serially for '+str(N[j])+' :-'))):
                                        pageObj=B[j].getPage(a)
                                        pdfWriter.addPage(pageObj)
                if m==4:
                        for j in range(y):
                                k=input('No. of random pages want to attach from  '+str(N[j])+' :-')
                                if k=='':
                                        print('Attaching Done for  '+str(N[j]))
                                        for j in range(y):
                                                for a in range(B[j].numPages):
                                                        pageObj=B[j].getPage(a)
                                                        pdfWriter.addPage(pageObj)
                                else:
                                        A=[]
                                        for h in range(int(k)):
                                                A.append(int(input('\tEnter the page no.:-')))
                                        print('Attaching Done for  '+str(N[j]))
                                        for a in A:
                                                pageObj=B[j].getPage(a-1)
                                                pdfWriter.addPage(pageObj)
                if m==5:
                	for j in range(y):
                		print('\nWorking on PDF File named '+'"'+str(N[j])+'"'+' :-')
                		tk=input('\nStarting page no.:')
                		kt=input('Ending page no.:')
                		if tk.isdigit() and kt.isdigit():
	                		if int(tk)!=0 and int(kt)!=0:
	                			for nm in range(int(tk)-1,int(kt)):
	                				pageObj=B[j].getPage(nm)
	                				pdfWriter.addPage(pageObj)
	                		print('\nDone for PDF File named '+'"'+str(N[j])+'"')
	                	else:
	                		print('\nWorking on PDF File named '+'"'+str(N[j])+'"'+' :-')
	                		for dbdb in range(B[j].numPages):
	                			pageObj=B[j].getPage(dbdb)
	                			pdfWriter.addPage(pageObj)
	                		print('\nDone for PDF File named '+'"'+str(N[j])+'"')
                print()
                pOF=open(input('Enter the name of merged file:-')+'.pdf','wb')
                pdfWriter.write(pOF)
                pOF.close()
                print('\nFiles are Ready to be viewed as Merged Successfully!!!👍')
        except:
                print('\n\t\tProgram Terminated')
                print('\t\t Restarting..... in 2 sec,please wait!')
                T()
PDF()
print()
print('Your Merged File contains the following files : -')
print()
for i in N:
        print('\t☛',i)
