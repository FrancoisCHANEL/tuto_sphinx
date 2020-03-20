import numpy as np
import pandas as pd

my_index = pd.date_range(
    start=2010, 
    periods=10, 
    freq='24h', 
    tz='Europe/Paris'
)

my_data  = np.random.randint(0, 10, len(my_index))

ts = pd.Series(
    index=my_index,
    data=my_data
)