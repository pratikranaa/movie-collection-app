#Complete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Create other functions for:
#   - listing movies

def list_movies():
    for counter, movie in enumerate(movies, 1):
        print(f"{counter}. {movie['title']} released in {movie['year']} directed by {movie['director']}")

#   - finding movies
def find_movie():
    name = input("Enter the title of movie: ").lower()
    for movie in movies:
        if movie['title'].lower() == name:
            print(f"Found: {movie['title'].title()} released in {movie['year']} directed by {movie['director']}")

# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movie()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)

# Remember to run the user menu function at the end!

menu()
    