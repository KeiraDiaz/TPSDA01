class MovieGoer:
    def __init__(self, id):
        self.id = id

class Member(MovieGoer):
    def __init__(self, id, membership_type):
        super().__init__(id)
        self.membership_type = membership_type

class NonMember(MovieGoer):
    def __init__(self, id):
        super().__init__(id)
