from datetime import date
from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

###################################################################################################

database = create_engine("sqlite:///toDo.db")                # create database engine

Base = declarative_base()                                    # basic class

Session = sessionmaker(bind=database)                        # opens connection to database

session = Session()                                          # session is open

console = Console()                                          # Rich initialization (module)

######################################## Table ################################################################

class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key = True)
    year = Column(String)
    month = Column(String)
    day = Column(String)
    todo = Column(String)
    status = Column(String)

def initialize_database():
    Base.metadata.create_all(database)

########################################### Input Menu ##########################################################

def show_menu():
    MENU_TEXT = """
    Menu:
    - (A)dd new item
    - (L)ist all items
    - (U)pdate an item
    - (S)how today's task
    - (D)elete an item
    - (E)xit
    """
    print (MENU_TEXT)

def get_users_menu_input():
    menu_choice = input("Choose menue option: ")

    if menu_choice == "A":
        add_new_item()
        
    elif menu_choice == "L":
        list_all_items()
        
    elif menu_choice == "U":
        update_one_item()
    
    elif menu_choice == "S":
        get_todays_task()
        
    elif menu_choice == "D":
        delete_one_item()
        
    elif menu_choice == "E":
        console.print(f"Bye!", style="bold red")
        exit(1)

######################################### Function ###############################################################

def add_new_item():
    print("Add a new item!")
    year = input("Year of due date\t: ")
    month = input("Number of month of due date\t: ")
    day = input("Day of due date\t: ")
    todo = input("What task\t: ")
    status = input("What is the status of task (open or done)\t: ")
    new_item = ToDo(year=year, month=month, day=day, todo=todo, status=status)
    console.print(f"Add a new item {new_item.year} {new_item.month} {new_item.day} {new_item.todo} {new_item.status}.", style="red")
    database_add_item(new_item)

def list_all_items():
    items = database_get_all_items()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("year")
    table.add_column("month")
    table.add_column("day")
    table.add_column("task")
    table.add_column("status")
    for item in items:
        table.add_row(str(item.id), item.year, item.month, item.day, item.todo, item.status)
    console.print(table)

def database_get_one_item(id: int):
    """
    Database command to get one item by ID.
    """
    return session.query(ToDo).get(id)

def update_one_item():
    id = int(input("Please enter the id of item you want to update: "))
    item = database_get_one_item(id)

    item_fields = {}
    item_field_to_update = input("Please enter the field of item to update: ")
    item_field_new_value = input(f"Please enter the new value to {item_field_to_update}: ")
    item_fields[item_field_to_update] = item_field_new_value
    console.print(f"Update item {item.year} {item.month} {item.day} {item.todo} {item.status}.", style="green")
    database_update_item(item, item_fields)

def delete_one_item():
    item_id = int(input("Please enter the ID of the item you want to delete: "))
    item = database_get_one_item(item_id)
    console.print(f"Delete item {item.year} {item.month} {item.day} {item.todo}.", style="red")
    database_delete_item(item)

# def show_todays_task():
#     curr_date = date.today()
#     curr_year = curr_date.year
#     curr_month = curr_date.month
#     curr_day = curr_date.day
#     return curr_year, curr_month, curr_day

##################################### Database ############################################################

def database_add_item(item: ToDo):
    session.add(item)
    session.commit()

def database_get_all_items():
    return session.query(ToDo).all()

def database_get_one_item(item_id: int):
    return session.query(ToDo).get(item_id)

def database_update_item(item: ToDo, fields: dict):
    session.query(ToDo).filter(ToDo.id == item.id).update(fields)
    session.commit()

def database_delete_item(item: ToDo):
    # "DELETE FROM friends WHERE id=4;"
    # friend = session.delete(Friend).id=4
    session.delete(item)
    session.commit()

def get_todays_task():
    # show_todays_task()
    curr_date = date.today()
    curr_year = curr_date.year
    curr_month = curr_date.month
    curr_day = curr_date.day
    tasks = session.query(ToDo).filter(ToDo.year==curr_year,ToDo.month==curr_month,ToDo.day==curr_day).all()
    for i in tasks:
        print (i.todo, i.status)

##################################### Main ################################################################

if __name__ == "__main__":
    initialize_database()
    while True:
        show_menu()
        get_users_menu_input()

###########################################################################################################