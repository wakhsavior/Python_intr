string = "Privet eto i tut zhivu"
print(string.strip())

delete_data = ''
print(type(string))
print(type(string) ==str) 
int_conv_bool = True
while int_conv_bool:
    try:
        delete_data = int(input("Which contact do you want to delete? "))
        int_conv_bool = False
    except (TypeError, ValueError):
        pass
   
    