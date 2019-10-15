import os
import pandas as pd

BASE_DIR = 'images/'
test_folder = BASE_DIR+'test/'

files_in_test = sorted(os.listdir(test_folder))

images=[i for i in files_in_test]

df = pd.DataFrame()
df['images']=[test_folder+str(x) for x in images]

df.to_csv('test.csv', header=None)