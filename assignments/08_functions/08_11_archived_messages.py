# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
def show_messages(messages):
    for message in messages:
        msg = ("This is for you: ")
        print(message)

#I am unsure of what it is asking for me to do.
un_sent = ["Have you heard about Brad?", "You should be doing your work at a more reasonable time.", "Don't forget about Monday!"]
un_sent = ["Have you heard about Brad?", "You should be doing your work at a more reasonable time.", "Don't forget about Monday!"]
sent = []

while un_sent:
    current_message = un_sent.pop()
    print(f"\nSending message: {current_message}")
    sent.append(current_message)

print("\nThe following messages have been sent:")
show_messages(un_sent[:], sent)