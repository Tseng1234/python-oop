class Email(object):
    def __init__(self,sender,recipients,subject,body,timestamp) :
        self.sender=sender
        self.recipients=recipients
        self.subject=subject
        self.body=body
        self.timestamp=timestamp
    def send():
        print("Sender: %s,recipients: %s,subject: %s,body: %s,timestamp: %s")
    
