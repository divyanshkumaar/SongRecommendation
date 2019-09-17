import song
print("--------------------------------------Welcome to Recommendation for You------------------------------------\n")
opt= input(print("Enter 1 if you want Movie Recommendations\nEnter 2 if you want Song Recommendations\n"))
if opt == 1:
	movie=int(input(print("Enter User ID:\n")))
elif opt == 2:
	songs=int(input(print("Enter User ID:\n")))
	print(train_data.head(songs))
	user_id = users[songs]
	print(pm.recommend(user_id))
else: 
	print("Please Enter a Valid Choice.")
