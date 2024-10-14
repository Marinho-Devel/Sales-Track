import csv


products = ["cabo", "interruptor"]

#array of informations of client
header = ["name", "surname", "cpf", "phonenumber", "email", "address"] 

#function for addition informations of client
def headerList(header):
    for i in range(len(header)):
        header[i] = input(f"insert the {header[i]} of client: ")
        if header[i] == "exit":
            break

#funtion for print the informations of client
def printHeader(header):
    for i in range(len(header)):
        print(header[i])
        
   
#declaration of variable "command" for the select the function to be executed
command = ""

while command != "exit":
    command = input("insert the command to start the proccess or product to added to list: ")

    if command == "header":
        headerList(header)
    elif command == "ls header":
        printHeader(header)
    elif command == "name":
        header[0] = input(f"insert the {header[0]} of client: ")
    elif command == "surname":
        header[1] = input(f"insert the {header[1]} of client: ")
    elif command == "cpf":
        header[2] = input(f"insert the {header[2]} of client: ")
    elif command == "phone":
        header[3] = input(f"insert the {header[3]} of client: ")
    elif command == "e-mail":
        header[4] = input(f"insert the {header[4]} of client: ")
    elif command == "address":
        header[5] = input(f"insert the {header[5]} of client: ")

    



