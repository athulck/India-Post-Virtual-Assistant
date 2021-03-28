# India-Post-Virtual-Assistant
This is a small Design &amp; Engineering project (BE102 - Semester 2) built using Python3. 

![alt text](https://github.com/athulck/India-Post-Virtual-Assistant/blob/master/Screenshots/img1.png "Sample Image")

## Requirements 
- [x] Linux/Ubuntu
- [x] Gedit
- [x] Python3
- [x] Tkinter
- [x] Pyttsx3
- [x] Espeak

## Installation Steps
Step 1. Unzip data.zip  
Step 2. Install all the requirements  
Step 3. Create a folder 'Complaints' and make sure that the program can write files under the directory.  
Step 4. Run `sudo apt-get install python3-tk`  
Step 5. Run `pip install pyttsx3`  
Step 6. Run `sudo apt-get install espeak -y`  
Step 4. Run `python3 main.py`  

## Possible Inputs

1. `complaint`  
This option helps you to register your complaints. The program will store your complaints as  `Complaints/ComplaintXXXX.txt`

2. `XXXXXX` : any 6 digit postal pin  
The program will do a reverse pin serach and shows the possible places (stroed in the data.txt file) using gedit.

3. `pincode`
4. `stamp`
5. `track`
The commands 3,4 and 5 opens up the corresponding pages in the India Post site.

6. `goodbye`
Exit.
