from os import path

file_base = "d:/1_Learn_Programming/GeekBrains/Python/Seminar_08/base.txt"
next_id = 0
all_data = {}


# If file doesn't exist create file
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

# show all result from menu
def show_all():
    show_result(all_data)

# Show data from dictionary - show_data in readable format
def show_result(show_data):
    if not show_data:
        print("Empty data")
    else:   
        line = "{0:15} {1:15} {2:15} {3:15}".format("surname","Last name","patronymic","phone_number")
        print(f"ID : {line}")
        
        key_list = [int(k) for k in show_data.keys()]
        key_list.sort() 
        for key in key_list:
            line = "{0:15} {1:15} {2:15} {3:15}".format(show_data[key][0],show_data[key][1],show_data[key][2],show_data[key][3])
            print(f"{key:3}: {line}")
    
# Read data from file to dictionary, key is ID 
def read_record():
    global next_id, all_data
    all_data = {}
    if not path.getsize(file_base):
        return {}
    with open(file_base, encoding="utf-8") as f:
        id = 0            
        for i in f:
            list_01 = i.split()
            id = int(list_01[0])
            list_01.pop(0)
            all_data[id] = list_01
        
        next_id = int(list(all_data.keys())[-1]) + 1   
    return all_data
    

# Rewrite all data into file from all_data, it can be used after all changes
def write_record(filename):
    global all_data   
    with open(filename, "w", encoding="utf-8") as f:        
        key_list = [int(k) for k in all_data.keys()]
        key_list.sort()       
        for k in key_list:
            line = ' '.join(all_data[k])
            f.write(f"{k} {line}\n")

# Add new contact to the end of dictionary all_data and call the function wrte_record
def add_new_contact(contact_id):
    global next_id, all_data
    array = ["surname", "name", "patronymic", "phone_number"]
    string = []
    
    for i in array:
        input_data = ""
        while len(input_data.split()) != 1:            
            input_data = input(f"Enter {i}: ")
            input_data = input_data.strip()
 #           print (len(input_data.split()))
        string.append(input_data)    
    all_data [contact_id] = string
    write_record(file_base)


# Change existing contact
def change_contact():
    global all_data
    search_data = input("Which data do you want to change? ")
    result = search(search_data)
    contact_id = choose_contact(result)        
    if contact_id:        
        delete(contact_id)
        add_new_contact(contact_id)
        write_record(file_base)


# Requset data for search, call search and show result
def search_contacts():
    search_data = input("Which data do you want to find? ")
    result = search(search_data)
    show_result(result)

# Search data in all_data and return dictionary with data
def search(search_data):    
    global all_data    
    search_result = {}    
    for id, line in all_data.items():
        if search_data in line:
            search_result[id] = line               
    return search_result
            
def delete(id):
    global all_data
    all_data.pop(id)

def choose_contact(contact_dict):
    if contact_dict == {}:
        print("There are no contact you choose!")
    else:
        show_result(contact_dict)
        try:
            contact = int(input("Which contact do you want to delete? "))
            int_conv_bool = False
            if contact in contact_dict.keys():
                return contact
            else:
                print("There are no contact you choose!")
                return 0
        except (TypeError, ValueError):
            print("There are no contact you choose!")
            return 0


def delete_contact():
    search_data = input("Which data do you want to delete? ")    
    result = search(search_data)   
    contact_id = choose_contact(result)        
    if contact_id:
        delete(contact_id)
        write_record(file_base)      
            

def exp_imp():
    play = True
    while play:
        answer = input("Phone book Export/Import:\n"
                        "1. Export records\n"
                        "2. Import records\n"
                        "3. Return to Main Menu\n"
                        "4. Exit\n")
        match answer:
            case "1":
                export_all()
            case "2":
                import_new()
            case "3":
                return True 
            case "4":
                return False        
            case _:
                print("Try again!\n")

def export_all():
    
    global file_base, all_data
    read_record()
    export_file = input("Enter Filename to Export: ")
    export_file += ".txt"
    write_record(export_file)


def import_new():
   
    global file_base
    import_file = input("Enter Filename to import: ")
    if not path.exists(import_file):
        print(f"File {import_file} doesn't exist!")
        return
    file_base = import_file

def main_menu():
    play = True
    while play:
        read_record()               
        answer = input("Phone book:\n"
                        "1. Show all records\n"
                        "2. Add a record\n"
                        "3. Change a record\n"
                        "4. Search a record\n"
                        "5. Delete a record\n"
                        "6. Exp/Imp\n"
                        "0. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact(next_id)
            case "3":
                change_contact()
            case "4":
                search_contacts()
            case "5":
                delete_contact()
            case "6":
                play = exp_imp()
            case "0":
                play = False
            case _:
                print("Try again!\n")



if __name__ == "__main__":
    main_menu()