import numbers
from random import random
class Film:
    def __init__(self, title, publ_year, type):
        self.title=title
        self.publ_year=publ_year
        self.type=type
        self.play_num=0
    def play(self, step):
        self.play_num+=step
    def __repr__(self):
        return f"{self.title} ({self.publ_year})."
    def __eq__(self,other):
        return (
            self.title==other.title and
            self.publ_year==other.publ_year and
            self.type==other.type and
            self.play_num==other.play_num
        )
class Series(Film):
    def __init__(self, ep_num, seas_num, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.ep_num=ep_num
        self.seas_num=seas_num
        self.play_num=0
    def play(self, step):
        self.play_num+= step
    def __repr__(self):
        return f"{self.title} S{self.seas_num:02d}E{self.ep_num:02d}.".format(numbers)
    def __eq__(self,other):
        return (
            self.title==other.title and
            self.publ_year==other.publ_year and
            self.type==other.type and
            self.play_num==other.play_num and
            self.ep_num==other.ep_num and
            self.seas_num==other.seas.num
        )
movieslist=[]
movieslist.append(Film(title="Candyman", publ_year=2021, type="Horror"))
movieslist.append(Film(title="Schumacher", publ_year=2021, type="Biography"))
movieslist.append(Film(title="Titanic", publ_year=1997, type="Romantic"))
movieslist.append(Series(title="Wataha", publ_year=2014, type="Action", ep_num=1, seas_num=1))
movieslist.append(Series(title="Manifest", publ_year=2018, type="Action", ep_num=1, seas_num=1))
movieslist.append(Series(title="Black List", publ_year=2013, type="Tragedy", ep_num=1, seas_num=1))
print("Oto twoja biblioteka:")
print(movieslist[0:])
def get_films():
    for obj in movieslist:
        result=isinstance(obj, Series)
        if result==False:
            print(obj)
        else:
            pass
def get_series():
    for obj in movieslist:
        result=isinstance(obj, Series)
        if result==True:
            print(obj)
        else:
            pass
x=input("Wyszczególnić filmy?[T/N]:")
if x=="T":
    get_films()
else:
    print("Okej, może zatem...")
    y=input("Wyszczególnić seriale?[T/N]:")
    if y=="T":
        get_series()
    else:
        print("W takim razie zostawiam Cię z całą biblioteką...")
        print(movieslist[0:])
print("Wyszukaj po tytule!")
def search():
    z=input("Wpisz tytuł filmu:")
    for obj in movieslist:
        result=obj.title==z
        if result==True:
            print(obj)
        else:
            pass
search()
import random
def generateviews():
    obj=random.choice(movieslist)
    step=random.choice(range(1,100))
    obj.play_num=step
generateviews()   
def multipleviews():
    for _ in range(10):
        generateviews()
def top_titles():
    by_views=sorted(movieslist, key=lambda movie:movie.play_num)
    print(by_views)
m=input("Czy posortować bibliotekę zgodnie z ilością wyświetleń?[T/N]:")

if m=="T":
    top_titles()
else:
    pass
