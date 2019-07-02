from  Crypto.Hash import MD5

def createUser():
    psw = MD5.new()
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    psw.update(b"{password}")
    if len(name) > 0 and len(password) > 0:
        user = { 'name' : name , 'password' : str(psw.hexdigest()) }
        print(" user created 👍")
        print(user)
    else:
        AssertionError

createUser()

# def getUser(name, password):    
#     createUser(name, str(password))

# getUser('Jean', MD5Hash.new(12345678))