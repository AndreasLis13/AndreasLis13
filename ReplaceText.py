#Replace text in file 

def main():
    openfile = input("Enter a file to open: ")

    old_string = input("Enter old string in file: ")

    new_string = input("Enter new string: ")

    with open(openfile, 'r') as file:
        data = file.read()

        data = data.replace(old_string, new_string)

    with open (openfile, 'w') as file:

        file.write(data)

    print("String has been successfully replaced")

main() 


