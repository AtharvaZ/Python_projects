from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

def view(fer):
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("-", 1)
            decrypted_passw = fer.decrypt(passw.encode()).decode()
            print("Username:", user)
            print("Password:", decrypted_passw)
            print("_" * 20)

def add(fer):
    name = input("Account name: ")
    pwd = input("Account password: ")

    with open('password.txt','a') as f:
        f.write(name + "-" + fer.encrypt(pwd.encode()).decode() + "\n")

def main():

    key = load_key()
    fer = Fernet(key)

    while True:
        mode = input("Would you like to add a new password or view an existing one?(add, view) or press q to quit: ").lower()
        if mode == "q":
            break
        if mode == "add":
            add(fer)
        elif mode == "view":
            view(fer)
        else:
            print("Invalid input.")
            continue

main()