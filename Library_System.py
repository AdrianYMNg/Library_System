#class declaration
class person:
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

class items:
    def __init__(self, name, copy):
        self.name = name
        self.copy = copy

class book(items):
    def __init__(self, name, genre, copy):
        super().__init__(name, copy)
        self.genre = genre

class map(items):
    def __init__(self, name, city, copy):
        super().__init__(name, copy)
        self.city = city

class news(items):
    def __init__(self, name, month, copy):
        super().__init__(name, copy)
        self.month = month

class library():
    #lists declaration
    def __init__(self, booklist, maplist, ppllist):
        self.booklist = booklist
        self.maplist = maplist
        self.ppllist = ppllist


    #Check out item
    def rentB(self, personname):
        pplexist = False
        for person in self.ppllist:
            if personname == person.name:
                pplexist = True
                item = input("what would you like to rent? (book, maps, newspaper)").lower()
                if item == "book":
                    itemname = input("which book would you like to check out?").lower()
                    for book in self.booklist:
                        if itemname == book.name:
                            if book.copy == 0:
                                print("there is no available copy of " + itemname)
                                break
                            book.copy = book.copy - 1
                            print(itemname + " is rented to " + person.name)
                            break
                    else:
                        print("we don't have " + itemname + " in this library")
                if item == "maps":
                    itemname = input("which map would you like to borrow?").lower()
                    for map in self.maplist:
                        if itemname == map.name:
                            if map.copy == 0:
                                print("there is no available copy of " + itemname)
                                break
                            map.copy = map.copy - 1
                            print(itemname + " is rented to " + person.name)
                            break
                    else:
                        print("we don't have " + itemname + " in this library")
                if item == "newspaper":
                    itemname = input("which newspaper would you like to check out?").lower()
                    for news in self.newslist:
                        if itemname == news.name:
                            if news.copy == 0:
                                print("there is no available copy of " + itemname)
                                break
                            news.copy = news.copy - 1
                            print(itemname + " is rented to " + person.name)
                            break
                    else:
                        print("we don't have " + itemname + " in this library")
        if not pplexist:
            print("Please register first")

    #Check in item
    def returnB(self, personname):
        pplexist = False
        for person in self.ppllist:
            pplexist = True
            if personname == person.name:
                item = input("what would you like to return? (book, maps, newspaper)")
                if item == "book":
                    itemname = input("which book would you like to return?").lower()
                    for book in self.booklist:
                        if itemname == book.name:
                            book.copy = book.copy + 1
                            print(itemname + " is returned by " + person.name)
                            break
                    else:
                        print(itemname + " does not belong to this library")
                if item == "maps":
                    itemname = input("which map would you like to return?").lower()
                    for map in self.maplist:
                        if itemname == map.name:
                            map.copy = map.copy + 1
                            print(itemname + " is returned by " + person.name)
                            break
                    else:
                        print(itemname + " does not belong to this library")
                if item == "newspaper":
                    itemname = input("which newspaper would you like to check out?").lower()
                    for news in self.newslist:
                        if itemname == news.name:
                            news.copy = news.copy + 1
                            print(itemname + " is returned by " + person.name)
                            break
                    else:
                        print(itemname + " does not belong to this library")
        if not pplexist:
            print("Who dafuk are you?")

    #Add item
    def addB(self, item):
        if item == "book":
            itemname = input("Please enter the name of the book").lower()
            itemtype = input("Please enter the genre of the book").lower()
            itemadd = book(itemname, itemtype, 1)
            booklist.append(book(itemname, itemtype, 1))
            booklist.append(itemadd)
            for book in booklist:
                if itemname == book.name:
                    book.copy = book.copy + 1
                    print(itemname + " is returned by " + person.name)
                    break
            else:
                print(itemname + " does not belong to this library")
        if item == "maps":
            itemname = input("which map would you like to return?").lower()
            for map in maplist:
                if itemname == map.name:
                    map.copy = map.copy + 1
                    print(itemname + " is returned by " + person.name)
                    break
            else:
                print(itemname + " does not belong to this library")
        if item == "newspaper":
            itemname = input("which newspaper would you like to check out?").lower()
            for news in newslist:
                if itemname == news.name:
                    news.copy = news.copy + 1
                    print(itemname + " is returned by " + person.name)
                    break
            else:
                print(itemname + " does not belong to this library")

    '''
    #Remove item
    def delB(itemname):
    
    #Update item
    def updateB(itemname):
    
    #Register person
    def addP(personname):
    
    #Delete person
    def delP(personname):
    
    #Update person
    def updateP(personname):
    '''
booklist = [book('harry potter', 'fiction', 2),book('john wick', 'action', 3),book('anabell', 'horror', 5)]
maplist = [map('brighton', 'uk', 3),map('manchester', 'uk', 4), map('california', 'us', 1)]
newslist = [news('argus', 'may', 3),news('sun', 'june', 2), news('guardian', 'march', 3)]
ppllist = [person('john', 'accounting', 21),person('erica', 'consultant', 40),person('alan ', 'doctor', 30),person('bob', 'nurse', 35),person('eunice', 'builder', 28)]
library = library(booklist,maplist,newslist,ppllist)
action = input("How can I help you?(rent item, return item  add item, remove item, update item, register, delete person, update person)").lower()
while action != "exit":
    if action == "rent item":
        person = input("Please enter your name").lower()
        library.rentB(person)
    elif action == "return item":
        person = input("Please enter your name").lower()
        library(returnB(person))
    elif action == "add item":
        item = input("Which item are you adding?(book, maps, newspaper)").lower()
        library(addB(person))
    elif action == "remove item":
        item = input("Which item are you removing?(book, maps, newspaper)").lower()
        library(delB(person))
    elif action == "update item":
        item = input("Which item are you updating?(book, maps, newspaper)").lower()
        library(updateB(person))
    elif action == "register":
        person = input("Please enter the name you want to add").lower()
        library(addP(person))
    elif action == "delete person":
        person = input("Please enter the name you want to remove").lower()
        library(delP(person))
    elif action == "update person":
        person = input("Please enter the name you want to update").lower()
        library(updateP(person))
    else:
        print("Action not valid")
    action = input("How can I help you?(rentitem, returnitem removeitem, updateitem, registerperson, deleteperson, updateperson)").lower()
