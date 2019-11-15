import streamlit as st
import pandas as pd
import numpy as np
from math import gcd
import altair as alt

st.title("Balanced Ternary")

st.subheader("Slider")
sl = st.slider("Select N", 1, 10000, 5000)
st.write(sl)

def a(n):
    if n==0: return 0
    if n%3==0: return 3*a(n/3)
    elif n%3==1: return 3*a((n - 1)/3) + 1
    else: return 3*a((n - 2)/3) - 1

r=[a(n) for n in range(sl)]

st.subheader("Sequence")
df=pd.DataFrame(r)
#to_string(index=False)
st.write(df.transpose())

st.subheader("Bar Chart")
st.bar_chart(df)

l=[]
for i,v in enumerate(r):
    l.append([i+1,v])

st.subheader("Scatter Plot")
df = pd.DataFrame(l,columns=['a', 'b'])

c = alt.Chart(df, height=500).mark_circle().encode(x='a', y='b')
st.write(c)