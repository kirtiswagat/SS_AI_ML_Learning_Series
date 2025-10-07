import time

start_time = time.time()
data = [1, 2, 3, 4]
squared = [x**2 for x in data]
print(squared)  
end_time = time.time()
print("Time taken:", end_time - start_time)