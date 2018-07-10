import numpy as np
import sys

number_list = np.arange(int(sys.argv[1]), 0, -1)

for num in number_list:
    print(num)

print('Blastoff!')
