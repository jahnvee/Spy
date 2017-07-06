from spy_details import spy,Spy,friends,ChatMessage
import colorama
from colorama import Fore, Style
from steganography.steganography import Steganography
colorama.init()

status_messages=["A Perfect Spy","Agent Infinity","Fly on the wall","The walls have Ears"]  #default status list
special_text=["SOS","save me","Caution","sos"]
text_to_send=[]
print "Hello!"
question = "Do you want to continue as default user (Y/N)? "
existing = raw_input(question)



def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
        print "Your current status is %s \n" % (spy.current_status_message)
    else:
        print "You don't have any status currently \n"

    default = raw_input("Do you want to select from the older status (y/n)? ")
    #when spy want to add new status
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            status_messages.append(new_status_message) #add new status to status message list
            updated_status_message = new_status_message
    #when spy want to select from previous status
    elif default.upper() == 'Y':

        item_position = 1

        for message in status_messages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection - 1]

    else:
        print "The option you chose is not valid! Press either y or n."

    if updated_status_message:#when status message is updated
        print "Your updated status message is: %s" % (updated_status_message)
    else:
        print "You did not update your status message"

    return updated_status_message

#function to add spy friends
def add_friend():
    new_friend=Spy('','',0,0.0)
    #friend name,salutation age and rating is added to data
    new_friend.name = raw_input("Please add your friend's name: ")
    if set('[~!@#$%^&*()+{}":;\']" "').intersection(new_friend.name):
        print "Invalid entry. Please enter a Valid Name!"
        new_friend.name=raw_input("enter your friend's name=")
        if set('[~!@#$%^&*()+{}":;\']" "').intersection(new_friend.name):
            print"Invalid name! Please try again."
            exit()
    else:
        print "That's a valid friend name"

    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age of your friend ?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)

        print "Friend Added!"
    else:
        print "Sorry!. We can't add spy with the details you provided"

    return len(friends)

#function to select a friend from the list to perform pre selected task
def select_a_friend():
    item_number = 0 #considered as index number

    for friend in friends:
        print '%d. %s %s  with rating %.2f is online' % (item_number +1,friend.salutation, friend.name, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1    #index number of spy friend

    return friend_choice_position

#this function will be called when spy wants to send any message
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")

    Steganography.encode(original_image, output_path, text)


    new_chat = ChatMessage(text, True)
    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    if secret_text != "":
        print "Your secret message has been saved!"
        print "your message is "+ secret_text
        if secret_text in special_text:
            text="Alarming Situation!! You need take action ASAP!"
            print "%s"%(Fore.RED+text)
            print (Style.RESET_ALL)
        secret_text = secret_text.split(" ")
        avrg_words=len(secret_text)
        count=0
        print"words spoken by spy in 1 message are " + str(avrg_words)
        text_to_send.append(avrg_words)
        for words in range(0,len(text_to_send)):
            counts=text_to_send[words]
            count=count+counts
        num=len(text_to_send)
        avrg=count/num

        print"average words spoken by spy are " + str(avrg)
        if count > 100:
            print"this spy is speaking too much"
            friends.pop(sender)
            delete_friend="spy deleted from friend-list"
            print "%s"%(Fore.RED+delete_friend)
            print (Style.RESET_ALL)
        else:
            print"friend is not deleted from the list"
    else:
        print"You don't have any secret message!"

def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me==True:

            print '[%s] %s: %s' % (Fore.BLUE+chat.time.strftime("%d %B %Y"),Fore.RED+spy.name+' said:',Fore.BLACK+ chat.message)
            print (Style.RESET_ALL)
        else:
            print '[%s] %s said: %s' % (Fore.BLUE+chat.time.strftime("%d %B %Y"),Fore.RED+friends[read_for].name,Fore.BLACK+ chat.message)
            print (Style.RESET_ALL)

def start_chat(spy):
    current_status_message = None

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Welcome " + spy.name + " age: " + str(spy.age) + " with rating of: " + str(spy.rating)

        show_menu = True

        while show_menu:
            menu_choices = "choose any option from following :- \n 1. Add a status \n 2. Add a friend \n 3. Send message \n 4. Read message \n 5. Read Chats \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    print "You chose to update the status"
                    spy.current_status_message=add_status()
                elif menu_choice==2:
                    number_of_friends=add_friend()
                    print "Now you have %d friends" % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    break
    else:
        print "Sorry your age is not appropriate to be a spy"





if existing.upper() == "Y":
    start_chat(spy)
else:
    spy = Spy('', '', 0, 0.0)

    spy.name = raw_input("Welcome to spy chat, tell us your spy name: ")
    if set('[~!@#$%^&*()+{}":;\']" "').intersection(spy.name):
        print "Invalid entry. Please enter a Valid Name!"
        spy.name=raw_input("enter your name again=")
        if set('[~!@#$%^&*()+{}":;\']" "').intersection(spy.name):
            print"Invalid username! Please try later."
            exit()
        else:
            print"Please provide more details :\n"
    else:
        print "That's a valid friend name"
    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        spy.is_online = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'