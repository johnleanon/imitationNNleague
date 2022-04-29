import cv2
import numpy as np

data = np.load("D:\sus/training_data.npy", allow_pickle=True)
targets = np.load("D:\sussy/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_W = 0
count_A = 0
count_S = 0
count_D = 0
count_Nothing = 0

for data in holder_list:
    #print(data[1])
    if data[1] == 'W':
        count_W += 1
        cv2.imwrite(f"D:/GC/W/H7-u{count_W}.png", data[0])
    elif data[1] == 'A':
        count_A += 1
        cv2.imwrite(f"D:/GC/A/H7-l{count_A}.png", data[0])
    elif data[1] == 'D':
        count_S += 1
        cv2.imwrite(f"D:/GC/S/H7-r{count_S}.png", data[0])
    elif data[1] == 'D':
        count_D += 1
        cv2.imwrite(f"D:/GC/D/H7-j{count_D}.png", data[0])
    elif data[1] == '':
        count_Nothing += 1
        cv2.imwrite(f"D:/GC/Nothing/H7-j{count_Nothing}.png", data[0])