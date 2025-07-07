from recommender.logic import recommend_outfit

gender = input("Enter gender: ").lower()
weather = input("Enter weather (cold/hot): ").lower()
occasion = input("Enter occasion: ").lower()

outfit = recommend_outfit(gender, weather, occasion)
print("Recommended Outfit:", outfit)

