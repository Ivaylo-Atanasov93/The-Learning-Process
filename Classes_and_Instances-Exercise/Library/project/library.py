from collections import defaultdict
class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = defaultdict(list)
        self.rented_books = defaultdict(dict)

    def add_user(self, user):
        current_users = [u.user_id for u in self.user_records]
        if user.user_id in current_users:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        user_for_removing = [u for u in self.user_records if u.user_id == user.user_id]
        if user not in user_for_removing:
            return "We could not find such user to remove!"
        self.user_records.remove(user_for_removing[0])

    def change_username(self, user_id: int, new_username: str):
        user = [u for u in self.user_records if u.user_id == user_id]
        if len(user) == 0:
            return f"There is no user with id = {user_id}!"
        elif user[0].username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"
        user[0].username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"

