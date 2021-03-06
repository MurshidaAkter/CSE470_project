movies = []

def add_movie():
    title = input("Enter title of the film: ")
    director = input("Enter director of the film: ")
    year = input("Enter year of the film: ")
    genre = input("Enter genre of the film: ")
    movies.append({
        'title': title,
        'year': year,
        'director': director,
        'genre': genre
    })


def list_movies():
    quantity = len(movies)
    titles = [movie['title'] for movie in movies]
    titles = ', '.join(titles)

    if quantity:
        print(f'You have following movies in collection: {titles}. In total you have {quantity} {"movie" if quantity == 1 else "movies"}.')
    else:
        print('There are no movies in you collection.')


def print_movie_info(movie):
    print('Here is information about requested title')
    print(f'Title: {movie["title"]},')
    print(f'Director: {movie["director"]},')
    print(f'Year: {movie["year"]},')
    print(f'Genre: {movie["genre"]}.')

def print_d_info(movie):
    print("Here is information about requested Director's movie")
    print(f'Title: {movie["title"]},')
   # print(f'Director: {movie["director"]},')
    print(f'Year: {movie["year"]},')
    print(f'Genre: {movie["genre"]}.')

def print_g_info(movie):
    print("Here is information about requested Director's movie")
    print(f'Title: {movie["title"]},')
    print(f'Director: {movie["director"]},')
    print(f'Year: {movie["year"]},')
   # print(f'Genre: {movie["genre"]}.')



def find_title():
    search_title = input('Enter title you are looking for: ')
    for movie in movies:
        if movie['title'] == search_title:
            print_movie_info(movie)
       # elif movie['title'] != search_title:
          #  print('Sorry! Requested title was not found in the collection.')


def find_director():
    search_director = input('Enter name you are looking for: ')
    for movie in movies:
        if movie['director'] == search_director:
            print_d_info(movie)
        #elif movie['director'] != search_director:
         #   print('Sorry! No movie information in the collection of this director.')

def find_genre():
    search_genre = input('What type of movie you are looking for: ')
    for movie in movies:
        if movie['genre'] == search_genre:
            print_g_info(movie)
       # elif movie['genre'] != search_genre:
           # print('Sorry! No movie of this genre in the collection.')


