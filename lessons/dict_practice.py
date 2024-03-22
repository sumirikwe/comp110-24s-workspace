"""Practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
#adding
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#Subtracting
ice_cream.pop("mint")
print("after removing mint:")
print(ice_cream)

#accessing
ice_cream["vanilla"] += 1
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)

print(ice_cream["bitch"])
