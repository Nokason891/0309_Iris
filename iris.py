import streamlit as st
import joblib

st.title("鳶尾花品種預測")
knn = joblib.load("app\knn_model.joblib")
svm = joblib.load("app\svm_model.joblib")
rf  = joblib.load(r'app\rf_model.joblib')
# 不知道為甚麼rf的有問題


# 左側
#clf = st.sidebar.selectbox("### 請選擇分類器:",("SVM","KNN"))
clf = st.sidebar.selectbox("### 請選擇分類器:",("SVM","KNN","RandomForest"))
if clf =="SVM":
    model = svm
elif clf=="KNN":
    model = knn
else:
    model = rf
    
# 產生預測用的資料

s1 = st.slider("花萼的長度:",3.0, 8.0, 5.8) # min /max / default
s2 = st.slider("花萼的寬度:",2.0, 5.0, 3.8) 
s3 = st.slider("花瓣的長度:",1.0, 7.0, 4.8)
s4 = st.slider("花瓣的寬度:",0.1, 2.6, 1.8)

# 預測
ans = st.button("進行預測")   # 按下去>True
name = ['Setosa','Versicolor','Virginica']
if ans:
    y = model.predict([[s1,s2,s3,s4]])
    st.write("### 預測結果： ",name[y[0]])