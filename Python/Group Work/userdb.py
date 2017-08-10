class User(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.id = None

	def display(self):
	    print "Name: ", self.name
	    print "Age: ", self.age

	def getName(self):
		return self.name

class UserDB(object):
	def __init__(self):
		self.users = []
		self.id = 1

	def all(self):  # return a list of all users
		return self.users

	def get(self, name): # get the first user with a first name match
		length = len(self.users)
		for i in range(0,length):
			if(self.users[i].name==name):
				return self.users[i]

	def filter(self,name): # returna  list of users with match on first name
		pass

	def exclude(self,name): # return a list of users that don't match on first name
		notList = []
		for user in self.users:
			if user.getName() != name:
				notList.append(user)
		return notList

	def delete(self,name): # delete the first match on first name
		for i in range(0,len(self.users) ):
			if self.users[i].name == name:
				del self.users[i]
                return self
		return self

	def create(self,name,age): # create a user and put in list
		user = User(name,age)
		self.users.append(user)
		return self

	def display_all(self): # display all the users
		for u in self.users:
			u.display()
		return self

	def createId(self):
		for user in self.users:
			if user.id == None:
				user.id = self.id
				self.id += 1
				
ud = UserDB()
ud.create("Joe",25)
ud.display_all()