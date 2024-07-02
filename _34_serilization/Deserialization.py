import pickle


file_in = open("user.pickle", "rb")
user_new = pickle.load(file_in)
user_new2 = pickle.load(file_in)
file_in.close()


print(user_new)
print(user_new2)
print(user_new['age'])