sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# for word in sentence.split():
#     print(word)

# result = {new_key:new_value for (key, value) in dict.items()}

# result = {new_key:new_value for item in list}

result = {word:len(word) for word in sentence.split()}

print(result)
