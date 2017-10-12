class User(object):
    def __init__(self):
        self.user_details = [{"Admin": "default"}]

    def register(self, name, email, passwd):
        self.user_details.append({ name :{"email_address":email, "password": passwd}})
        return self.user_details

    def login(self, name, passwd):
        if name not in self.user_details:
            return "The username is not recognised"
        else:
            return "Login successful"


if __name__ == '__main__':
    me = User()
    print me.register("Derrick", "derrick.korir@gmail.com", "Renegade4751")
    you = User()
    print me.register("Brenda", "brenda@gmail.com", "Renegade4751")
    print me.login("Derrick", "letmein")

