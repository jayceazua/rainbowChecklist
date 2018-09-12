# Test Connection
# print("Hello World")
#
# def my_fun_function(say_this):
#     print(say_this)
#
# my_fun_function('Hello World')

# CRUD Functions
checklist = list()
# The power of a programmer is knowing where your knowledge ends and where your connection with put who know what you don't know begins.
# Don't move on if you feel like your missing something
# Building foundation of learning during this time
# Be kind and write your programs for your future self!
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

#Create
def create(item):
    checklist.append(item)

#Read
def read(index):
    print(checklist[index])

#Update
def update(index, item):
    checklist[int(index)] = str(item)

#Destroy
def destroy(index):
    checklist.pop(int(index))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1
# Mark Complete - Working On
def mark_completed(index):
        # print ("√" + checklist[str(index)]
        checklist[int(index)].append("√")

def user_input(prompt):
        # the input function will display a message in the terminal
        # and wait for user input.
        user_input = input(prompt)
        return user_input

#Select which functions we want to run
def select(function_code):
    #Create item
    if function_code == "A":
        input_item = user_input("Add to list:\n ")
        create(input_item)
    #Delete item
    elif function_code == "D":
        input_item = user_input("Which item do you want to delete?\n ")
        destroy(input_item)
    #Read item
    elif function_code =="R":
        input_item = user_input("What is the number of that item?\n ")

        #Remember that item_index (was used as the variable that holds user input and inside read below) must actually exist or our program will crash.
        read(int(input_item))

    # Update item
    elif function_code == "U":
        input_item = user_input("What is the index of the item you want to update?\n ")
        input_update = user_input("What item would you like to replace it with?\n ")
        update(input_item, input_update)
    # Print all items - Works
    elif function_code == "P":
        list_all_items()
    #Mark Complete
    elif function_code == "C":
        input_item = user_input("What item would you like to mark complete?\n")
        mark_completed(input_item)
    # Close out of program - Works
    elif function_code =="Q":
        #This is where we want to stop our loop
        return False
    #Catch all - Works
    else:
        print("Unknown Option")
    return True

running = True
while running:
    selection = user_input("Press A to Add to list, \nD to Delete, \nR to access an item, \nU to Update item, \nC to mark as Completed, \nand P to show list. \nPress Q to Exit \n")
    running = select(selection)

#Testing code
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))

    list_all_items()
    mark_completed(0)

    #Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    user_value = user_input("Please Enter a value:")
    print(user_value)

# Run Tests
#test()
