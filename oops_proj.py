class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbook! how would you like to proceed?
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit
                           
                           -> """)
        if  user_input == "1":
            self.signup()
        elif  user_input == "2":
            self.signin()
        elif  user_input == "3":
            self.my_post()
        elif  user_input == "4":
            self.sendmsg()
        else:
            exit()
    
    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Setup your password here -> ")
        self.username = email
        self.password = pwd
        print("you have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username== '' and self.password == '':
            print("Please signup first by pressing 1")
        else:
            uname = input("Enter your username/email here -> ")
            pwd = input("Enter your password here -> ")

            if self.username == uname and self.password == pwd:
                self.loggedin = True
                print("You have successfully loggedin")
            else:
                print("please input correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            text = input("Enter your meassage here -> ")
            print(f"following content has been posted -> {text}")
        else:
            print("you need to signin first for writing a message")
        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin == True:
            msg = input("write a message to send -> ")
            frnd = input("whom to send the message -> ")
            print(f"your message has been sent to your friend, {frnd}")
        else:
            print("you need to signin first to write a message to your friend")
        print("\n")
        self.menu()
obj = chatbook()
