class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_list = []
information = input().split()
while 'Stop' not in information:
    sender = information[0]
    receiver = information[1]
    content = information[2]
    email = Email(sender, receiver, content)
    email_list.append(email)
    information = input().split()

sent_emails = input().split(', ')
indexes_sent_emails = [int(index) for index in sent_emails]
for i in indexes_sent_emails:
    email_list[i].send()
for email in email_list:
    print(email.get_info())