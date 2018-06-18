## Made by: Jaslyn Palomino
## My Social Network


class User:
    def __init__(self, firstName, lastName, username, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.friends = []
        self.posts = []
    
    def addFriend(self,username):
        self.friends.append(username)

##    def unFriend():
##        
##
    def viewNewsFeed(self, friends):
     for Friend in self.friends:
      print (friends.posts)
        

if __name__ == "__main__":

    ##My Account
    firstName = "Jaslyn"
    lastName = "Palomino"
    username = "jaslynpolynomial"
    bio = "Hi, my name last name is actually Palomino"
    userID = "0000"

    ##My Friends
    jaslyn = User(firstName, lastName, username, bio, userID)
    jaslyn = User("Jaslyn", "Palomino", "jaslynpolynomial", "Hi, my name last name is actually Palomino","0000")  
    maxx = User("Maxx", "Maxine", "maxuel","this is max","0123")
    emily = User("Emmy", "Emily", "em","this is M","0124")

    ##Friend-Maxx
    print(jaslyn.firstName)
    print(maxx.firstName)
    jaslyn.addFriend("maxuel")
    print(jaslyn.friends)

    ##Friend-Maxx-Post
    maxx.posts.append ("this is max")
    maxx.posts = maxx.posts
    print (maxx.posts)

    ##Friend-Emily
    print(jaslyn.firstName)
    print(emily.firstName)
    jaslyn.addFriend("em")
    print(jaslyn.friends)

    ##Friend-Emily-Post
    emily.posts.append ("this is M")
    emily.posts = emily.posts
    print (emily.posts)

jaslyn.viewNewsFeed(username)

    
