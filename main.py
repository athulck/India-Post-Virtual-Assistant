#Imports
from tkinter import *
import pyttsx3
import time
import string
import os


class Process:


    #Constructor
	def __init__(self, master):
	     
	    #Variables
		self.answer="Good Morning, How may I help you ?"
		self.cmp_no=2001
	    
	    #Background Image
		self.background_image = PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"/bg.gif")
		self.background_label = Label(master, image=self.background_image)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
       
		#Heading
		self.label1=Label(text="INDIA POST",bg="red",fg="yellow")
		self.label1.place(x=350,y=30,width=100,height=25)
		master.columnconfigure(0, weight=1)
		master.rowconfigure(0, weight=1)
		
		self.label_q=Label(master,text="QUERY : ",bg="black",fg="blue")
		self.label_q.place(x=280,y=175,width=100,height=25)
	
		#Input Box
		self.query_box=Entry(master)
		self.query_box.place(x=420,y=175,width=300,height=25)

		self.label_ans=Label(master,text="COMPUTER : ",bg="black",fg="blue")
		self.label_ans.place(x=280,y=225,width=100,height=25)
	
		#Output Box
		self.ans=Label(master,text="%s"%self.answer,bg="black",fg="green")
		self.ans.place(x=420,y=225,width=300,height=25)

		#Button
		self.submit=Button(master,text="Submit")
		self.submit.place(x=350,y=275,width=100,height=25)
		self.submit.bind("<Button-1>",self.ifsubmitclicked)
	
		#Welcome Speech
		self.talk_back(self.answer[:-1])

	#Complaint Register Button
	def ifregisterclicked(self, event):
		
		name = os.path.dirname(os.path.realpath(__file__))+"/Complaints/Complaint"+str(self.cmp_no)+".txt"
		print(name)
		
		file = open(name, "w+")
		file.write(self.complaint_box.get("1.0", 'end-1c'))
		file.close()
		
		answer="Your complaint has been successfully registered"
		self.talk_back(answer)

		self.ans = Label(mainActivity,text="%s"%answer,bg="black",fg="green")
		self.ans.place(x=420,y=225,width=300,height=25)
		# os.system("service apache2 start")

		self.notification="Complaint Registered! Complaint No : "+str(self.cmp_no)
		os.system("""zenity --info --text=" """+self.notification+""" " --title  "Complaint Registered" """)
		self.cmp_no+=1
		self.complaint_box.place_forget()
		self.query_box=Entry(mainActivity)
		self.query_box.place(x=420,y=175,width=300,height=25)
		self.submit.place_forget()
		self.submit=Button(mainActivity,text="Submit")
		self.submit.place(x=350,y=275,width=100,height=25)
		self.submit.bind("<Button-1>",self.ifsubmitclicked)
		
		
	#Submit Button
	def ifsubmitclicked(self,event):
		self.query=self.query_box.get()
		if("complaint" in self.query):
			answer="Please enter your complaint in the box"
			self.ans=Label(mainActivity, text=answer, bg="black", fg="green")
			self.ans.place(x=420,y=225,width=300,height=25)
			self.complaint_box=Text(mainActivity)
			self.complaint_box.place(x=420,y=175,width=300,height=50)
			self.submit=Button(mainActivity,text="Register Complaint")
			self.submit.place(x=300,y=275,width=200,height=25)
			self.submit.bind("<Button-1>",self.ifregisterclicked)
			
		
		else:
			import Processes
			self.answer=Processes.process(self.query)
			self.ans=Label(mainActivity,text="%s"%self.answer,bg="black",fg="green")
			self.ans.place(x=420,y=225,width=300,height=25)

    #Function for TTS
	def talk_back(self, s):
		self.engine = pyttsx3.init()
		self.rate = self.engine.getProperty('rate')
		self.engine.setProperty('rate', self.rate)
		self.voices= self.engine.getProperty('voices')                                                                                   
		self.engine.setProperty('voice',  'english-us') 
		self.engine.say(s)
		self.engine.say("   ")
		self.a = self.engine.runAndWait()



mainActivity = Tk()
mainActivity.title("India Post Virtual Assistant")
mainActivity.geometry("800x400")

obj = Process(mainActivity)
mainActivity.mainloop()
