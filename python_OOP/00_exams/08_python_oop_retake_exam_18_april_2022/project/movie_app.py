from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __find_movie_by_title(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return movie

    def register_user(self, username, age):
        user = self.__find_user_by_name(username)

        if user:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user = self.__find_user_by_name(username)

        if not user:
            raise Exception("This user does not exist!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        user = self.__find_user_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute_name, new_value in kwargs.items():
            if attribute_name == "title":
                movie.title = new_value
            elif attribute_name == "year":
                movie.year = new_value
            elif attribute_name == "age_restriction":
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        user = self.__find_user_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # TODO
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        user = self.__find_user_by_name(username)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        user = self.__find_user_by_name(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        output = [x.details() for x in sorted_movies]

        return "\n".join(output)

    def __str__(self):
        output = []

        if not self.users_collection:
            output.append("All users: No users.")
        else:
            output.append(f"All users: {', '.join(x.username for x in self.users_collection)}")

        if not self.movies_collection:
            output.append("All movies: No movies.")
        else:
            output.append(f"All movies: {', '.join(x.title for x in self.movies_collection)}")

        return "\n".join(output)