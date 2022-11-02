from datetime import datetime

# Chat App
greetIntent = ["hi","hello","hii","hey","hello there","hi there"]
dateIntent = ["what's the date","tell me date","date","date please"]
timeIntent = ["what's the time","tell me time","time","time please"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = datetime.now().date()
        print(d.strftime("%d %B, %Y, %A"))
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime("%I:%M:%S,%p"))
    elif msg == "bye":
        chat = False
    else:
        print("I don't understand")
