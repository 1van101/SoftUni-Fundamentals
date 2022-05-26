class Email:
    def __init__(self, s, r, c):
        self.s = s
        self.r = r
        self.c = c
        self.is_sent = False


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.s} says to {self.r}: {self.c}. Sent: {self.is_sent}"

emails = []
while True:
    current_command = input().split()
    if "Stop" in current_command:
        break

    sender = current_command[0]
    receiver = current_command[1]
    content = current_command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(x) for x in input().split(", ")]

for e in range(len(emails)):
    if e in indices:
        emails[e].send()
    print(emails[e].get_info())
