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

spy = Spy('Jahnvee', 'Ms.', 19, 4.5)

friend_one = Spy('Ridhima', 'Ms.', 21, 4.9)
friend_two = Spy('Sonali', 'Ms.', 21, 4.7)
friend_three = Spy('Nikita', 'Ms.', 20, 4.8)
friend_four = Spy('Jaspreet', 'Ms.', 20, 4.7)
friend_five = Spy('Anshul', 'Ms.', 19, 4.7)
friend_six = Spy('Himani', 'Ms.', 21, 4.7)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five,friend_six]




