class Email:
    def __init__(self, sender, recipients, subject, body, timestamp):
        self.sender = sender
        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.timestamp = timestamp

    def send(self):
        print("Sender: ", self.sender)
        print("Recipients: ", ", ".join(self.recipients))
        print("Subject: ", self.subject)
        print("Body: ", self.body)
        print("Timestamp: ", self.timestamp)


class EmailClient:
    def __init__(self):
        self.inbox = []

    def receive_email(self, email):
        self.inbox.append(email)

    def display_inbox(self):
        for email in self.inbox:
            email.send()
            print("-------------------------------")
# 建立一封郵件
email1 = Email("sender@example.com", ["recipient1@example.com", "recipient2@example.com"], "Hello", "This is the body of the email.", "2023-06-13 09:00")

# 建立郵件客戶端
client = EmailClient()

# 接收郵件
client.receive_email(email1)

# 顯示收件匣中的郵件
client.display_inbox()
