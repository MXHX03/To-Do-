"""
class Facebook:
 def __innit__(self, email, username, firstname, lastname, dob, education, marital_status, gender, interests, password,)
    self.email = email
    self.username = username
    self.firstname = firstname
    self.lastname = lastname
    self.dob = dob
    self.education = education
    self.marital_status = marital_status
    self.gender = gender
    self.phone = phone
    self.interests = interests
    self.password = password

    filename = "useraccounts.txt"
 def create_account(self):

    with open("useraccounts.txt,""r") as useraccount:
     write to our database "useraccounts.txt"
      this saves the info received from the user in the database
     useraccount.write(self.email + ',' + self.username + ',' + self.firstname + ',' + self.lastname + ',' + self.dob +
                       ',' + self.education + ',' + self.marital_status + ',' + self.gender + ',' + self.phone + ',' +
                       str(self.interests) +',' + self.password + '\n')
    print("account created successfully")

 def login(self): login method
    with open("useraccouts.txt","r") as useraccount:
          fetch the contents line by line and append to a list "user_details"
    user_details = useraccount.readline()
    print(user_details)
    for details in user_details:
        details = details.split(",")
        email = user_details[0]
        phone = user_details[8]
        password = user_details[10]

        if self.email == email or self.phone == phone and self.password == password:
            print("login successful!")
            break
    else:
        print('login failed!')
        # print( email, phone)

 facebook = Facebook(email= "umar@gmail.com", username= "nice_guy", firstname= "umar", lastname= "saad",dob="1-23-4567"
                    education= 'phd', marital_status= "single", gender= "male", phone= "08173367782", interests=
                    ["football","coding"], password= "123456")

facebook = Facebook(email= "moses@gmail.com", username= "moses_guy", firstname= "moses", lastname= "josh"
                    ,dob="1-23-4567"
                    education= 'phd', marital_status= "married", gender= "male", phone= "08173367782", interests=
                    ["basketball","coding"], password= "1234")

         facebook.login()
   add_friend_facebook = Facebook(email= "umar@gmail.com", username="", firstname="moses", lastname="",)
"""

