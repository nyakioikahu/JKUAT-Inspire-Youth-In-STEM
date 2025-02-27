game_score= int(input("Enter your game score: "))

if game_score >= 90:
    print("Qualify for group A")
elif game_score >= 80:
    print("Qualify for group B")
elif game_score >= 70:
    print("Qualify for group C")
elif game_score < 60:
    print("You are Religated")