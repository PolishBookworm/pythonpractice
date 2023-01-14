class User:

    active_users = 0
    usernames = []

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        username, email, location = data_str.split(",")
        return cls(username, email, location)

    def __init__(self, username, email=None, location=None):
        if username in User.usernames:
            raise ValueError("This username is already taken")
        self.username = username
        self.email = email
        self.location = location
        self.comments = 0
        User.active_users += 1
        User.usernames.append(username)

    def __repr__(self):
        return f"{self.username}"

    def logout(self):
        User.active_users -= 1
        return f"{self} has logged out"

    def login(self):
        User.active_users += 1
        return f"{self} has logged in"


bilbo = User("MrBaggins", "mrbaggins@gmail.com", "The Shire")
frodo = User("theringbearer", "frodo@gmail.com", "The Shire")
gandalf = User("Mithrandir", "wizard@yahoo.com", "Here And There")
sam = User("SamGam", "sammy@gmail.com", "The Shire")
pippin = User("pip", "friendoftheents@gmail.com", "The Shire")
merry = User("mer", "anotherfriendoftheents@gmail.com", "The Shire")
boromir = User("brmr", "boromir@yahoo.com", "Gondor")
legolas = User("ElfInTheNet", "ElfInTheNet@gmail.com", "Mirkwood")
gimli = User("gimli", "dwarf@gmail.com", "The Lonely Mountain")
aragorn = User("strider", "aragornsonofarathorn@yahoo.com", "Gondor")
gollum = User(
    "myyyyyyypreciooooooousssssssssssss",
    "gollum@outlook.com",
    "The Misty Mountains")
sauron = User("daaaaaaaarknesssssss", "imadethering@outlook.com", "Mordor")
saruman = User("whitesaruman", "saruman@yahoo.com", "Isengard")
elrond = User("elrond", "elrond@gmail.com", "Rivendell")
