#class Student:
    # [assignment] Skeleton class. Add your code here
#    def __init__(self):
#        pass



#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

#class keyword
class Student:
    # [assignment] Skeleton class. Add your code here

    #The init Method or Constructor
    def __init__(self, name, age, tracks, score):

    #Instance Variable
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        pass

    #methods
    def change_name(self, name):
        return (print(name))

    def change_age(self, age):
        return (print(age))

    def add_tracks(self, tracks):
        return (print(tracks))

    def get_score(self, score):
        return (print(score))

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

#output
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks(["Frontend", "Backend", "UI/UX"])
Bob.get_score(Bob.score)