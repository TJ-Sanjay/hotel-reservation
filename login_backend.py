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
    path = "E:\\software project\\hotel-reservation-main\\login.csv"
    credential = read_credentials(path)
    user = list(credentials.keys())
    if user[0] in credential:
        status = "already"
    else:
        with open(file_path, 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for user_name, pass_word in credentials.items():
                csv_writer.writerow([user_name, pass_word])
            status = "successfully"
    return status


def login(user_name, pass_word):
    file_path = "E:\\software project\\hotel-reservation-main\\login.csv"
    credentials = read_credentials(file_path)
    if user_name in credentials and credentials[user_name] == pass_word:
        status = "successfully"
    else:
        status = "invalid"
    return status
