import streamlit as st
import pandas as pd
import numpy as np
from math import gcd
import altair as alt

st.title("Wisteria")

st.subheader("Slider")
sl = st.slider("Select N", 1, 2000, 500)
st.write(sl)

def a(n):
    ar=[int(d) for d in str(n)]
    ar=list(filter(lambda a: a != 0, ar))
    s=np.prod(np.array(ar)) 
    return n-s
r=[a(n) for n in range(sl)]

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