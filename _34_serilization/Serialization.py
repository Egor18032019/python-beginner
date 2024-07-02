import pickle

user = {'name': 'John', 'age': 34, 'weight': 87}
user2 = {'name': 'John', 'age': 35, 'weight': 87}
file = open('user.pickle', "wb")
pickle.dump(user, file)
pickle.dump(user2, file)
file.close()

