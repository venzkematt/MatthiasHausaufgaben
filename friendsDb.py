from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

#############################################################################################

database = create_engine("sqlite:///contacts.db")           # create database engine

Base = declarative_base()                                   # basic class

Session = sessionmaker(bind=database)                       # opens connection to database

session = Session()                                         # session is open

console = Console()                                         # Rich initialization (module)

##############################################################################################

class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    city = Column(String)
    street = Column(String)
    zip_code = Column(String)

    # foreignkeys
    profession_id = Column(Integer, ForeignKey("profession.id"))
    hobby_id = Column(Integer, ForeignKey("hobby.id"))
    language_id = Column(Integer, ForeignKey("language.id"))

    def __repr__(self) -> str:
        return f"<{self.last_name}, {self.first_name}>"

class Profession(Base):
    __tablename__ = "profession"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Language(Base):
    __tablename__= "language"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Hobby(Base):
    __tablename__ = "hobby"

    id = Column(Integer, primary_key=True)
    name = Column(String)

def initialize_database():
    Base.metadata.create_all(database)

def show_menu():
    MENU_TEXT = """
    Menu:
    - (A)dd new Friend
    - (L)ist all Friends
    - (U)pdate a friend
    - (D)elete a Friend
    - (E)xit
    """
    print (MENU_TEXT)

def get_users_menu_input():
    menu_choice = input("Choose menue option: ")

    if menu_choice == "A":
        add_new_friend()
    elif menu_choice == "L":
        # database_get_all_friends()
        list_all_friends()
    elif menu_choice == "U":
        update_one_friend()
    elif menu_choice == "D":
        delete_one_friend()
    elif menu_choice == "E":
        console.print(f"Bye!", style="bold red")
        exit(1)

def add_new_friend():
    print("Add a new friend!")
    first_name = input("First name\t:")
    last_name = input("Last name\t:")
    new_friend = Friend(first_name=first_name, last_name=last_name)
    console.print(f"Add a new friend {new_friend.first_name} {new_friend.last_name}.", style="red")
    database_add_friend(new_friend)
    # session.commit()

def database_add_friend(friend: Friend):
    session.add(friend)
    session.commit()

def list_all_friends():
    friends = database_get_all_friends()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("First Name")
    table.add_column("Last Name")
    table.add_column("email_address")
    for friend in friends:
        table.add_row(str(friend.id), friend.first_name, friend.last_name, friend.email)
    console.print(table)

def delete_one_friend():
    friend_id = int(input("Please enter the ID of your friend: "))
    friend = database_get_one_friend(friend_id)
    console.print(f"Delete friend {friend.first_name} {friend.last_name}.", style="red")
    database_delete_friend(friend)

def database_get_all_friends():
    # all_friends = session.query(Friend).all()
    # print(all_friends)
    return session.query(Friend).all()

def database_get_one_friend(friend_id: int):
    """
    Database command to get one friend by ID.
    """
    return session.query(Friend).get(friend_id)

def update_one_friend():
    friend_id = int(input("Please enter the ID of your friend: "))
    friend = database_get_one_friend(friend_id)

    friend_fields = {}
    friend_field_to_update = input("Please enter the field of your friend to update: ")
    friend_field_new_value = input(f"Please enter the new value to {friend_field_to_update}: ")
    friend_fields[friend_field_to_update] = friend_field_new_value
    console.print(f"Update friend {friend.first_name} {friend.last_name}.", style="green")
    database_update_friend(friend, friend_fields)

def database_update_friend(friend: Friend, fields: dict):
    session.query(Friend).filter(Friend.id == friend.id).update(fields)
    session.commit()

def database_delete_friend(friend: Friend):
    # "DELETE FROM friends WHERE id=4;"
    # friend = session.delete(Friend).id=4
    session.delete(friend)
    session.commit()
    
########################################################################################
           ## main ##
########################################################################################
if __name__ == "__main__":
    initialize_database()
    # session.commit()

    # print ("Add a new friend!")
    # first_name = input("First name\t: ")
    # last_name = input("Last name\t: ")

    # new_friend = Friend(first_name=first_name, last_name=last_name)

    # database_add_friend(new_friend)
    # session.commit()


    # # Example to add a new friend
    # new_friend = Friend(e_mail="jack@example.com", first_name="Jack")
    # database_add_friend(new_friend)

    # # Example to list all friends
    # database_get_all_friends()
    while True:
        show_menu()
        get_users_menu_input()