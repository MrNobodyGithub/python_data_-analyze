import numpy as np  
import matplotlib.pyplot as plt 
from numpy.random import randn 
import pandas as pd

s = pd.Series(np.random.randn(100).cumsum(), index = np.arange(0,100,10))
s.plot()


  
