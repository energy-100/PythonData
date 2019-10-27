import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = ts.get_k_data('000001', start='2016-01-01', end='2016-12-31', ktype='D',autype='qfq')
print(data)
# data.index = pd.to_datetime(data['date'],format='%Y-%m-%d')
# per = data['close'].pct_change()[1:]
# p_mu = np.mean(per)
# p_std = np.std(per)
# cil, cir = stats.norm.interval(0.95, loc=p_mu, scale=p_std)
# print(cil, cir)