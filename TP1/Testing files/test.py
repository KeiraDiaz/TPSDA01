import math

class MovieGoer:
    def __init__(self, id, type, money):
        self.id = id
        self.member = type
        self.money = money
        self.FilmsWatched = 0

class Movie:
    def __init__(self, id, price, capacity, percent, genre):
        self.id = id
        self.price = int(price)
        self.capacity = int(capacity)
        self.priority =  math.ceil(int(capacity) * int(percent))
        self.genre = genre
        self.booking_queue = []

    def is_empty(self):
        return len(self.booking_queue) == 0

    def get_position_in_queue(self, moviegoer_id):
        for position, item in enumerate(self.booking_queue, 1):
            if item.id == moviegoer_id:
                return position
        return -1

def BookingMovie(moviegoers_id, movie_id, moviegoers, movies):
    if 1 <= moviegoers_id <= len(moviegoers):
        moviegoer = moviegoers[moviegoers_id - 1]
        movie = movies[movie_id - 1]

        if moviegoer.money >= movie.price:
            movie.booking_queue.append(moviegoer)
            return len(movie.booking_queue)
        else:
            return -1
    else:
        return -1

def PlayingMovie(movie_id, movies):
    movie = movies[movie_id - 1]

    if movie.is_empty():
        return -1

    while not movie.is_empty():
        m = movie.booking_queue.pop(0)
        m.FilmsWatched += 1

    return True

def TrackingQueue(moviegoers_id, movie_id, moviegoers, movies):
    moviegoer = moviegoers[moviegoers_id - 1]
    movie = movies[movie_id - 1]

    position = movie.get_position_in_queue(moviegoer.id)
    return position

if __name__ == "__main__":
    MovieList = []
    MovieGoerList = []
    results = []

    N = 3
    movie_id = 1
    for i in range(N):
        HH, HK, HP = 30, 5, 25
        movieH = Movie(movie_id, HH, HK, HP, "H")
        MovieList.append (movieH)
        movie_id += 1

        AH, AK, AP = 20, 10, 40

        movieA = Movie(movie_id, AH, AK, AP, "A")
        MovieList.append(movieA)
        movie_id += 1

        SH, SK, SP = 25, 12, 50
        movieS = Movie(movie_id, SH, SK, SP, "S")
        MovieList.append(movieS)
        movie_id += 1

    M = 6
    for i in range (M):
        t, u = input().split()
        mg = MovieGoer(i+1, t, int(u))
        MovieGoerList.append(mg)

    T = 6
    for _ in range(T):
        act, *args = input().split()
        if act == "B":
            moviegoer_id, movie_id = map(int, args)
            result = BookingMovie(moviegoer_id, movie_id, MovieGoerList, MovieList)
            results.append(result)
        elif act == "P":
            movie_id = int(args[0])
            result = PlayingMovie(movie_id, MovieList)
            results.append(result)
        elif act == "T":
            moviegoer_id, movie_id = map(int, args)
            result = TrackingQueue(moviegoer_id, movie_id, MovieGoerList, MovieList)
            results.append(result)

    for result in results:
        print(result)
