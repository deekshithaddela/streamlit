import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Recamán’s Sequence')

st.subheader("Slider")
sl = st.slider("Select N", 1, 200, 20)
st.write(sl)

ar=[0]
def recaman(n):  
    if(n <= 0): 
        return
    s = set([]) 
    s.add(0)  
    prev = 0
    for i in range(1, n):  
        curr = prev - i  
        if(curr < 0 or curr in s): 
            curr = prev + i 
        s.add(curr) 
        ar.append(curr)
        prev = curr 

st.subheader("Sequence")
recaman(sl)
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
