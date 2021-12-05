import streamlit as st
import numpy as np
import pandas as pd


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [34.4, 133.2],
    columns=['lat', 'lon']

)
print(df)


# mapでdfの座標をプロットする
st.map(df)

