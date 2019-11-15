import streamlit as st
import pandas as pd
import numpy as np
from math import gcd
import altair as alt

st.title("Fly Staight DamnIt!")

st.subheader("Slider")
sl = st.slider("Select N", 1, 1000, 50)
st.write(sl)

ar=[1,1]
def fsd(n):    
    for i in range(2, n):
        g=gcd(int(ar[-1]),i) 
        if g>1:
            c=ar[-1]/g
        else:
            c=ar[-1]+i+1
        ar.append(c)

st.subheader("Sequence")
fsd(sl)
df=pd.DataFrame(ar)
#to_string(index=False)
st.write(df.transpose())

st.subheader("Line Chart")
st.line_chart(df)

l=[]
for i,v in enumerate(ar):
    l.append([i+1,v])

st.subheader("Scatter Plot")
df = pd.DataFrame(l,columns=['a', 'b'])
c = alt.Chart(df, height=500).mark_circle().encode(x='a', y='b')
st.write(c)