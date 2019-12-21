# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:40:37 2019

@author: CEC
"""

import pandas as pd
import numpy as np

data=np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))