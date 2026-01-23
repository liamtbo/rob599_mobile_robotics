import numpy as np


scan_dist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


scan_dist = np.array(scan_dist) # len(scan_values) = 180
scan_angle = np.linspace(-np.pi/2, np.pi/2, len(scan_dist))
dist_histogram = []
angle_histogram = []
bin_size = 1
for i in range(int(len(scan_dist) / bin_size) - 1):
    dist_bin_i = scan_dist[bin_size * i: bin_size * i + bin_size].sum()
    dist_histogram.append(dist_bin_i)
    angle_bin_i = scan_angle[bin_size * i + bin_size]
    angle_histogram.append(angle_bin_i)

print(dist_histogram)
print(angle_histogram)