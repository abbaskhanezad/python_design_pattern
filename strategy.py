"""
Strategy Design Pattern (Behavioral)
This allows us to specify how to execute the code at runtime.
Ability to select an algorithm at runtime.
If we can do a task in several ways and the desired method is selected at runtime,
 Strategy Pattern will be a good choice.
In this Example :
 we want to implement an automated Message Sender.
"""

class Message:
    _message_types = {
        "text": "text",
        "email": "email",
        "sms": "sms"
    }


    def __init__(self, msg,type):
        self.msg = msg
        self.type = type

    def __str__(self):
        return self.msg

class Sender:
    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def send(cls,msg):
        if msg.type in Message._message_types.values():
            print("Sending {}, by {} service".format(msg,msg.type))
        else:
            print("Message type ({}) not supported".format(msg.type))
  

if __name__=="__main__":

    print("Strategy Design Pattern")
    print("======================")

    m1=Message("Hello, it is a text message","text")
    m2=Message("Hello, it is an email message","email")
    m3=Message("Hello, it is an sms message","sms")
    m4=Message("Hello, it is an slack message","slack")

    Sender.send(m1)
    Sender.send(m2)
    Sender.send(m3)
    Sender.send(m4)
