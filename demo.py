import numpy as np
import pandas as pd
import streamlit as st

st.title("SMALL FLOWER")
st.text("warm")
st.write("ABC")
st.info("ABCD")

st.write("# ABC")
st.write("## ABC")

a = np.array([[1,2],[3,4],[5,6]])
st.write(a)

b= pd.DataFrame(a)
st.write(b)
st.table(a) #撐滿滿 不能點
st.table(b)

re = st.checkbox("RED")  # 勾勾
if re:
    st.info("RED")
else:
    st.info("NOTHING")
re2 = st.checkbox("PINK")  # 勾選
if re2:
    st.info("PINK")
else:
    st.info("NOTHING")
re3 = st.checkbox("PINKY", key = "a")  # 有些元件不允許多個(像是button)，加個key當識別ID，就可以建立多個
if re3:
    st.info("PINKY")
else:
    st.info("NOTHING")