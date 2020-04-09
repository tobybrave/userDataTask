import string 
import random 

def userDetails():
   firstName = input("Enter your first name: ") 
   lastName = input("Enter your last name: ") 
   email = input("Enter your email address: ") 
   details = (firstName,lastName,email)
   return details
   
details = userDetails()  
        
def randomPassword(details):
  length = 5
  letters = string.ascii_lowercase
  randomLetters= "". join(random.choice(letters)for i in range(length))
  password_gen = details[0][:2] + randomLetters + details[1][-2:] 
  return password_gen
 
         
status = True
 
userData = {}

userData["first Name"] = details[0] 
userData["last Name"] = details[1]
userData["email"] = details[2]
password = randomPassword(details)    
print("Here is a suggested password : "+password)

while status:
  like_password = input ("do you like the password? If you like it enter 'yes', and if you dont, enter 'no': ") 
  """ you can only choose either yes or no""" 
 
  while True:
            if like_password == "yes" or like_password == "Yes":
              userData["password"] = password
              
              
            
            elif like_password == "no" or like_password == "No":
              user_entered_password = input(" Enter your preferred password (it must be at least 7 letters long) : ") 
             
              while True:
                if len(user_entered_password) >= 7:
                  userData["user_entered_password"] = user_entered_password      
        
                else:
                  user_entered_password = input(" Enter your preferred password (it must be at least 7 letters long) : ")  
                 
            else:
              print( " you're only meant to say 'yes' or 'no'") 
              
            new_user = input("would you like to continue as a new user? 'yes' or 'no':") 
            if new_user =="yes" or new_user == "Yes":
              status = True
            else:
              print (userData)
              
 