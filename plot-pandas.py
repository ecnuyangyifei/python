import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.close('all')

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

# print(ts)

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()

ts.plot()
# df.plot()
plt.show()
