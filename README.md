# India-Post-Virtual-Assistant
This is a small Design &amp; Engineering project (BE102 - Semester 2) built using Python2. 


## Requirements 
- [x] Linux/Ubuntu
- [x] Gedit
- [x] Python2
- [x] TKinter
- [x] Pyttsx
- [x] Espeak
- [x] Apache

## Installation Steps
Step 1. Unzip data.zip  
Step 2. Install all the requirements  
Step 3. Create a folder '/var/www/html/Complaints/' and run a `chmod` on '/var/www/html/Complaints/.' to make sure that the program can write files under the directory.  
Step 4. Run `python2 main.py`  

## Possible Inputs

1. `complaint`  
This option helps you to register your complaints. The program will store your complaints as  
`/var/www/html/Complaints/ComplaintXXXX.txt`  
User can start `apache2` process so that this system will act as a server and the admin can read the complaints directly via the local network using the IP address of this system.

2. `XXXXXX` : any 6 digit postal pin  
The program will do a reverse pin serach and shows the possible places (stroed in the data.txt file) using gedit.

3. `pincode`
4. `stamp`
5. `track`

The commands 3,4 and 5 opens up the corresponding pages in the India Post site.

6. `goodbye`
Exit.




