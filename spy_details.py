from datetime import datetime
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Jahnvee', 'Ms.', 19, 4.9)

friend_one = Spy('Ridhima', 'Ms.', 4.9, 21)
friend_two = Spy('Sonali', 'Ms.', 4.7, 21)
friend_three = Spy('Nikita', 'Ms.', 4.8, 20)
friend_four = Spy('Jaspreet', 'Ms.', 4.6, 20)
friend_five = Spy('Anshul', 'Ms.', 4.5, 19)
friend_six = Spy('Himani', 'Ms.', 4.55, 21)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five,friend_six]




