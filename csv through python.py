import csv

def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r', newline='', encoding='iso-8859-1') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if len(row) >= 2:  
                credentials[row[0]] = row[1]
    return credentials



def write_credentials(file_path, credentials):
    with open(file_path, 'a+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for username, password in credentials.items():
            csv_writer.writerow([username, password])

def login(k):
    file_path = 'Z:\login.csv'
    credentials = read_credentials(file_path)
    
    username = input("Username: ")
    password = input("Password: ")
    
    if username in credentials and credentials[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


k=1
while k==1:
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        login()
        
    elif choice == '2':
        username=input("Username:")
        password=input("Password:")
        data={username:password}
        file='Z:\login.csv'
        write_credentials(file,data)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a valid option.")


