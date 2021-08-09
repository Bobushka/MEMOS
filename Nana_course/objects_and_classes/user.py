class User:
    def __init__(self, user_email, user_name, user_password, user_title):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.title = user_title

    def change_password(self, new_password):
        self.password = new_password

    def change_title(self, new_title):
        self.title = new_title

    def get_user_info(self):
        print(f"User {self.name} works as {self.title}. You can contact them by {self.email}")


