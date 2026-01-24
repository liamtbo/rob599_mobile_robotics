import numpy as np
import copy

threshold = 5

scan_dist = np.array([
    1, 2, 6, 7, 8, 6, 2, 1,
    5, 6, 7, 7, 8, 4, 2,
    1, 6, 6, 7
])


scan_angle = np.linspace(-np.pi/2, np.pi/2, len(scan_dist))

dist_bins = []
angle_bins = []
bin_size = 2

num_bins = len(scan_dist) // bin_size

for i in range(0, len(scan_dist), bin_size - 1):
    start = i
    end = min(i + (bin_size - 1) + 1, len(scan_dist)) # -1 bc that how bins overlap and +1 bc we want the end integer when slicing
    dist_bin = scan_dist[start:end].min()
    dist_bins.append(float(dist_bin))
    angle_bins.append(scan_angle[start:end])

print(dist_bins)
print(angle_bins)

print('-------------------------')

free_bins = []
free_angles = []
for i, dist in enumerate(dist_bins):
    if dist >= threshold:
        free_bins.append(dist)
        free_angles.append(angle_bins[i])

# print(free_bins)
print(free_angles)

print('-------------------------')

# combine adjacent 
grouped_angles = [] 
local_group = copy.copy(free_angles[0])
for i in range(1, len(free_angles)):
    # print(f'free_angle: {free_angles[i]}')
    if free_angles[i][0] == free_angles[i - 1][-1]:
        # print('if path\n')
        if len(free_angles) > 1:
            local_group = np.concatenate((local_group, free_angles[i][1:])) # don't add a duplicate angle
        if i == len(free_angles) - 1:
            grouped_angles.append(local_group)
    else:
        # print(f'else path\n')
        grouped_angles.append(local_group)
        local_group = copy.copy(free_angles[i])
        if i == len(free_angles) - 1:
            grouped_angles.append(local_group)

print(f'grouped angles:\n{grouped_angles}')

print('-------------------------')



target_angle = 0.5

# find which angle bins is closest to target angle
closest_angle = None
target_angle_bin = None
for angle_bin in grouped_angles:
    if target_angle > angle_bin[-1]:
        continue
    target_angle_bin = angle_bin
    min_error = float('inf')
    for i, candidate in enumerate(angle_bin):
        err = abs(target_angle - candidate)
        if err < min_error:
            min_error = err
            closest_angle = candidate
            target_angle_bin = angle_bin
    break

# # return closest_angle
print(closest_angle)
print(target_angle_bin)

print('---------------')

# add padding to angle
padding = 1 # padding off the extremes of target_angle_bin
padded_angle = target_angle
if closest_angle == target_angle_bin[0]:
    padded_angle_i = min(0 + padding, len(target_angle_bin) - 1)
    padded_angle = target_angle_bin[padded_angle_i]
elif closest_angle == target_angle_bin[-1]:
    padded_angle_i = max(len(target_angle_bin) - 1 - padding, 0)
    padded_angle = target_angle_bin[padded_angle_i]

print(padded_angle)
