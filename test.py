import numpy as np
import pickle

data_dict = {
    'volts': np.random.random(10),
    'current': np.random.random(10),
}

with open('data_pick.pkl' ,'wb') as picklefile:
    pickle.dump(data_dict, picklefile )

with open('data_pick.pkl', 'rb') as picklefile1:
    newdata=pickle.load(picklefile1)

print(newdata)


