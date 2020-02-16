#Imports
import string
import webbrowser
import time
import pyttsx

#Functions
#This converts the program output list into output eligible string.
def form_string(lst):
    pgm_output = str()
    pgm_output=""
    for word in lst:
        pgm_output = pgm_output+" "+str(word)
    pgm_output=pgm_output[1:]
    return pgm_output
    
def google_search(lst):
    #Google Search URL
    google_url = "https://www.google.co.in/?gws_rd=ssl#q="
    for word in lst:
        google_url = google_url+word+"+"
    google_url = google_url[:-1]
    webbrowser.open(google_url,new=1)
    pgm_op_lst=['your','search','result', 'will', 'show', 'up', 'in', 'your', 'browser']
    return pgm_op_lst

# def youtube_search(lst):
#     point=0
#     #Youtube Search URL
#     youtube_url = "https://www.youtube.com/results?search_query="
#     for i,word in enumerate(lst):
#         if word == "play":
#             point=i+1
#     for j in range(point,len(lst)):
#         youtube_url = youtube_url+lst[j]+"+"
#     youtube_url = youtube_url[:-1]
#     webbrowser.open(youtube_url,new=1)
#     pgm_op_lst=['your','music', 'will', 'show', 'up', 'in', 'your', 'browser']
#     return pgm_op_lst


def talk_back(s):
     engine = pyttsx.init()
     rate = engine.getProperty('rate')
     engine.setProperty('rate', rate)
     voices= engine.getProperty('voices')                                                                                   
     engine.setProperty('voice', 'english-us')                                                                                         
     engine.say(s)
     engine.say("   ")
     a = engine.runAndWait()


def process(usr_input):


    # 1.Reading the INPUT from the user
	usr_ip_lst = list()
	usr_ip_lst = usr_input.split()


    #List which stores the output values
	pgm_op_lst=list()


    #For each word in user input :
	for i,word in enumerate(usr_ip_lst):

			if len(word) == 6:
				if word.isdigit():
					import Reverse_pin_finder	
					if(Reverse_pin_finder.find_pin(word)):
						pgm_op_lst=['Hope','you', 'found', 'what','you','were','looking','for']
					else:
						pgm_op_lst=['Sorry','no', 'results', 'found']
					break

			elif word == 'pincode':
					webbrowser.open('https://www.indiapost.gov.in/vas/pages/FindPinCode.aspx',new=1)
					pgm_op_lst=['find','your', 'pin', 'code']	
					break	
          
			elif word == 'stamp':
					webbrowser.open('https://www.indiapost.gov.in/VAS/Pages/calculatePostage.aspx',new=1)
					pgm_op_lst=['find','your', 'stamp']	
					break	

			elif word == 'track':
					webbrowser.open('https://www.indiapost.gov.in/VAS/Pages/trackconsignment.aspx',new=1)
					pgm_op_lst=['feed','in','your', 'consignment','number']	
					break			
			elif word == 'goodbye':
					pgm_op_lst = ['Have', 'a','nice','day']
                    #This is the TTS part
					engine = pyttsx.init()
					engine.say(form_string(pgm_op_lst))
					engine.runAndWait()
					return form_string(pgm_op_lst)
    
			else:
					if len(usr_ip_lst) == i+1:
                            #No words matches with our options !
                            #So, we show the google results :)
							pgm_op_lst=google_search(usr_ip_lst)
        

    #This is the TTS part
	talk_back(form_string(pgm_op_lst))
	return form_string(pgm_op_lst)
