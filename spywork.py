from spy_details import spy,Spy,friends,ChatMessage
import colorama
from colorama import Fore
from steganography.steganography import Steganography
colorama.init()

status_messages=["A Perfect Spy","Agent Infinity","Fly on the wall","The walls have Ears"]
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

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            status_messages.append(new_status_message)
            updated_status_message = new_status_message

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

    if updated_status_message:
        print "Your updated status message is: %s" % (updated_status_message)
    else:
        print "You did not update your status message"

    return updated_status_message


def add_friend():
    new_friend=Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
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
        print "Sorry! Invalid entry. We can't add spy with the details you provided"

    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s  with rating %.2f of age %d is online' % (item_number +1,friend.salutation, friend.name, friend.age,friend.rating)


        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


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


    print "Your secret message has been saved!"
    print "your message is "+ secret_text
    secret_text=secret_text.split()
    avrg_words=len(secret_text)
    print"the average words spoken by spy are "+str(avrg_words)
    if avrg_words> 100:
        print"this spy is speaking too much"
        friends.pop(sender)
        print"spy deleted from friend-list"
    else:
        print"friend is not deleted from the list"


def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me==True:

            print '[%s] %s: %s' % (Fore.BLUE+chat.time.strftime("%d %B %Y"),Fore.RED+spy.name+' said:',Fore.BLACK+ chat.message)
        else:
            print '[%s] %s said: %s' % (Fore.BLUE+chat.time.strftime("%d %B %Y"),Fore.RED+friends[read_for].name,Fore.BLACK+ chat.message)


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