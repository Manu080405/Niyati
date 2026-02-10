file = open("Detail.csv", "r")

lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

header = lines[0].split(",")

data = {}
for h in header:
    data[h] = []

for line in lines[1:]:
    values = line.split(",")
    for i in range(len(header)):
        value = values[i]
        try:
            if "." in value:
                data[header[i]].append(float(value))
            else:
                data[header[i]].append(int(value))
        except:
            data[header[i]].append(value)

print(data)

print(data["user_name"])

while True:
    print("1.Register")
    print("2.Login")
    
    try:
        choice = int(input("Enter the Choice : "))
    except ValueError:
        print("Invalid choice")
        continue

    if choice == 2:
        n = input("Enter the Account name : ")


        if n not in data['user_name']:
            print("User Not Found")
            continue

        print("User Found")


        index = data['user_name'].index(n)

        try:
            p = int(input("Enter the Passcode : "))
        except ValueError:
            print("Passcode must be numbers only")
            continue

        if p != data['passcode'][index]:
            print("Wrong Passcode")
            continue


        if data['status'][index] == 1:
            print("Login Successful")
            print("Account is Active ")
        else:
            print("Account is Inactive")
