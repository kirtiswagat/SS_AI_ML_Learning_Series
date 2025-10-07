# # Writing data to a file
# with open("data.txt", "w") as f:
#     f.write("Machine Learning is fun!")

# # Reading data back
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)

# Writing multiple lines
# lines = ["Python", "AI", "Machine Learning"]
# with open("topics.txt", "w") as f:
#     for line in lines:
#         f.write(line + "\n")

# # Reading line by line
# with open("topics.txt", "r") as f:
#     for line in f:
#         print(line.strip())

import json, csv

# Writing JSON
data = {"model": "RandomForest", "accuracy": 0.92}
with open("model.json", "w") as f:
    json.dump(data, f)

# Reading JSON
with open("model.json", "r") as f:
    model_info = json.load(f)
    print(model_info["accuracy"])

