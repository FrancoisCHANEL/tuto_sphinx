import numpy as np
import pandas as pd

tutu = pd.Series(index=list('abcdef'),
                    data=range(6))

print(tutu.sum())