class Emailclient():
    def __init__(self):
        self.inbox=[]
    def receive_email(self,email):
        self.inbox.append(self,email)
    def display_inbox(self):
        print(self.inbox)

        
