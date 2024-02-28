
import math
from classes import PriorityQueueItem, PriorityQueue 

# -------------------------------------------------------------------------- Classes --------------------------------------------------------------------------

class MovieGoer: # MovieGoer class
    def __init__(self, id, type, money):
        self.id = id
        self.member = type
        self.money = money
        self.FilmsWatched = 0

class Movie: # Movie class

    def __init__(self, id, price, capacity, percent, genre):
        self.id = id
        self.price = int(price)
        self.capacity = int(capacity)
        self.priority =  math.ceil(int(capacity) * int(percent))
        self.genre = genre
        self.booking_queue = PriorityQueue()

    def get_position_in_queue(self, moviegoer_id):
        queue_copy = self.booking_queue.copy()
        position = 1
        while not queue_copy.is_empty():
            if queue_copy.dequeue().data.moviegoer_id == moviegoer_id:
                return position
            position += 1
        return -1


# -------------------------------------------------------------------------- Lists --------------------------------------------------------------------------

MovieList = []
MovieGoerList = []
MemberList = []
NonMemberList = []


# -------------------------------------------------------------------------- Functions --------------------------------------------------------------------------   



def BookingMovie(moviegoers_id, movie_id, moviegoers, movies): # BookingMovie function
    moviegoer = moviegoers[moviegoers_id - 1]
    movie = movies[movie_id]

    if moviegoer.money >= movie.price:
        movie.booking_queue.insert(PriorityQueueItem(moviegoer))
        return True
    else:
        return False

def PlayingMovie(movie_id, movies): # PlayingMovie function
    movie = movies[movie_id]

    if movie.booking_queue.is_empty():
        return -1

    while not movie.booking_queue.is_empty():
        m = movie.booking_queue.dequeue()
        m.data.FilmsWatched += 1

    return True
    
def TrackingQueue(moviegoers_id, movie_id, moviegoers, movies):
    moviegoer = moviegoers[moviegoers_id]
    movie = movies[movie_id]

    position = movie.get_position_in_queue(moviegoer.moviegoer_id)
    if position == -1:
        return -1
    else:
        return position



# -------------------------------------------------------------------------- Priority Queues --------------------------------------------------------------------------

MemberBooking = PriorityQueue()
NonMemberBooking = PriorityQueue()

for p in MovieGoerList:
    if p.member == "M":
        MemberBooking.insert(PriorityQueueItem(p))
    else:
        NonMemberBooking.insert(PriorityQueueItem(p))  



# -------------------------------------------------------------------------- Main Program --------------------------------------------------------------------------    


if __name__ == "__main__":

    N = int(input()) # Number of days of the movie festival

    movie_id = 1
    for i in range(N):
            HH, HK, HP = input().split() # h(price) k(capacity) p(percent)
            movieH = Movie(movie_id, HH, HK, HP, "H")
            MovieList.append(movieH)
            movie_id += 1

            AH, AK, AP = input().split() 
            movieA = Movie(movie_id, AH, AK, AP, "A")
            MovieList.append(movieA)
            movie_id += 1

            SH, SK, SP = input().split()
            movieS = Movie(movie_id, SH, SK, SP, "S")
            MovieList.append(movieS)
            movie_id += 1

    M = int(input()) # Number of moviegoers in the festival

    for i in range (M):
        t, u = input().split() # T = type of moviegoer, U = money
        mg = MovieGoer(i, t, int(u))
        MovieGoerList.append(mg)
        if t == "M":
            MemberList.append(mg)
        else:
            NonMemberList.append(mg)

    T = int(input()) # Number of tugas or activities

    for _ in range(T):
        act, *args = input().split()
        if act == "B":
            moviegoer_id, movie_id = map(int, args)
            BookingMovie(moviegoer_id, movie_id, MovieGoerList, MovieList)
        elif act == "P":
            movie_id = int(args[0])
            PlayingMovie(movie_id, MovieList)
        elif act == "T":
            moviegoer_id, movie_id = map(int, args)
            TrackingQueue(moviegoer_id, movie_id, MovieGoerList, MovieList)
        elif act == "J":
            king = int(args[1])


         