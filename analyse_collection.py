import json
import os
from IPython import embed


def check_start(file):
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            price = line.split(',')[-2]
            if price != '':
                # print(line)
                
                return line

real_files = os.listdir("NFT_top50_prices")
# check_start(os.path.join("NFT_top50_prices", real_files[0]))

for file in real_files:
    line = check_start(os.path.join("NFT_top50_prices", file))
    print("'"+file.split('_')[1]+"'", ':', "'"+line.split(',')[1].split('T')[0]+"'", ',')
