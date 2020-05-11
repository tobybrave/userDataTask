import string 
import random 
import re

def userDetails():
   firstName = input("Enter your first name: ") 
   lastName = input("Enter your last name: ") 
   user_email = input("Enter your email address: ")
   verifying_email = True
   while verifying_email:
   	#checking if email format is correct
   	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
   	if not re.search(regex, user_email):
   		print("Invalid email address!!! Try again")
   		user_email = input("Enter your email address: ")
   	else:
   		verifying_email = False
   details = (firstName,lastName,user_email)
   return details
 
#generating random password    
def randomPassword(details):
  letters = string.ascii_lowercase
  randomLetters= "". join(random.choice(letters) for i in range(5))
  password_gen = details[0][:2] + randomLetters + details[1][-2:] 
  return password_gen
 
         
new_account = True
all_users = []
while new_account:
	details = userDetails()
	userData = {}
	
	userData["first Name"] = details[0] 
	userData["last Name"] = details[1]
	userData["email"] = details[2]
	password = randomPassword(details)   
	print("Here is a suggested password : "+password)
		
	ask_like_password = input ("Do you like the password? Enter Yes / no: ")
	#checking if user likes the random password generated
	like_password = True
	while like_password:
		if ask_like_password.lower() == "yes":
			userData["password"] = password
			like_password = False	
		elif ask_like_password.lower() == "no":
			user_entered_password = input(" Enter your preferred password (it must be at least 7 letters long) : ")
			
			#is password entered at least 7 characters long
			password_length = True
			while password_length:
				if len(user_entered_password) >= 7:
					userData["user_entered_password"] = user_entered_password
					password_length = False
					like_password = False
				else:
					user_entered_password = input(" Enter your preferred password (it must be at least 7 letters long) : ")  
					
		else:
			print( "You're only meant to type 'yes' or 'no'")
			ask_like_password = input ("Do you like the password? Enter Yes / no: ")
			
	all_users.append(userData)
	new_user = input("Would you like to continue as a new user? Yes / no: ")
	
	#entering as new user or not
	status = True
	while status:
		if new_user.lower() == "yes":
			status = False
			new_account = True
		elif new_user.lower() == "no":	
			print (all_users)
			status = False
			new_account = False
			
		else:
			print("Input either Yes or No")
			new_user = input("Would you like to continue as a new user? Yes / no: ")