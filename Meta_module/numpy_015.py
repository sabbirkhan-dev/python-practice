import numpy as np
import pandas as pd
# a = np.zeros(10)
# print(a)

# b = np.full((2,10), 0.7)
# print(b)

# c = np.linspace(0,25,7)
# print(c)

# print(type(c))

df = {
    "Name": ["Rahim", "Karim", "Salam", "Rafi"],
    "Math": [85, 70, 90, 60],
    "English": [78, 65, 88, 72]
}

df = pd.DataFrame(df)

df["Total"] = np.array(df["Math"]) + np.array(df["English"])
print(df)

