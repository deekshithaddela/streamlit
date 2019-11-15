import streamlit as st
import pandas as pd
import numpy as np
from math import gcd
import altair as alt

st.title("Forest Fire")

st.subheader("Slider")
sl = st.slider("Select N", 1, 50000, 10000)
st.write(sl)

r = []
def a(n):
    for n in range(n):
        i, j, b = 1, 1, set()
        while n-2*i >= 0:
            b.add(2*r[n-i]-r[n-2*i])
            i += 1
            while j in b:
                b.remove(j)
                j += 1
        r.append(j)
a(sl) 
st.subheader("Sequence")
df=pd.DataFrame(r)
#to_string(index=False)
st.write(df.transpose())

st.subheader("Line Chart")
st.line_chart(df)

l=[]
for i,v in enumerate(r):
    l.append([i+1,v])

st.subheader("Scatter Plot")
df = pd.DataFrame(l,columns=['a', 'b'])
c = alt.Chart(df, height=500).mark_circle().encode(x='a', y='b')
st.write(c)