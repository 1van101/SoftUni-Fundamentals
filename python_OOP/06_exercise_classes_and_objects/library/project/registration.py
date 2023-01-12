from project import User
from project import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        try:
            library.user_records.remove(user)
        except ValueError:
            return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):
        try:
            searched_user = [x for x in library.user_records if x.user_id == user_id][0]
            if searched_user.username != new_username:
                searched_user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {searched_user.user_id}"
            return "Please check again the provided username - it should be different than the username used so far!"
        except IndexError:
            return f"There is no user with id = {user_id}!"
