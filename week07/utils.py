from io import StringIO
import pandas as pd

my_data = """id, length, width
height
1,10.0,10.0
9.0
2,12.0,8.0
17.5
"""

readable_data = StringIO(my_data)

df = pd.read_csv(readable_data, skiprows=2,names=[str(i) for i in range(3)])
np_data = df.values
