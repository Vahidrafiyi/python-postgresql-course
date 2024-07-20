import datetime
import database

menu = """\nPlease select one of the following options:
1) Add a new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Exit.

Your selection: """

welcome = "Welcome to the watchlist app!"

print(welcome)

database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    release_timestamp = parsed_date.timestamp()
    database.add_movie(title, release_timestamp)

def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1]).strftime("%d %b %Y")
        print(f"{movie[0]} (on {movie_date})")
    print("------ \n")

def print_watched_movie_list(username, movies):
    print(f"-- {username}'s watched movies --")
    for movie in movies:
        print(f"{movie[1]}")

    print("---- \n")
    

def prompt_watch_movie():
    title = input("Enter a movie title which you've wathed: ")
    username = input("Enter watcher username: ")
    database.watch_movie(username, title)
    print("Wached successfully!")


def prompt_get_watched_movies():
    username = input("Enter watcher username: ")
    movies = database.get_watched_movies(username)
    print_watched_movie_list(username, movies)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(upcoming = True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies(upcoming = False)
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_get_watched_movies()
    else:
        print("Invalid input, please try again!")