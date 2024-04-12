
"""Make a new class called Profile!"""


class Profile:

    username: str
    private: bool


    def __init__(self, username_input: str):
        self.username = username_input
        self.private = True
    
    def tweet(self, msg: str):
        if self.private == False:
            print(msg)


user1: Profile = Profile("110_rulez")
user1.private = False
user1.tweet("OOP is cool!")