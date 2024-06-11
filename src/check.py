import numpy as np

A = np.load('/home/wzw/Desktop/imuProject/TLIO/golden-new-format-cc-by-nc-with-imus/110982076486017/imu0_resampled.npy')
print('A:',A[10:15,1:7])

B = np.load('/home/wzw/Desktop/imuProject/TLIO/golden-new-format-cc-by-nc-with-imus/newdata/imu0_resampled.npy')
print('B:',B[10:15,1:7])
