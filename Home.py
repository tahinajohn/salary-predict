import streamlit as st
import matplotlib.pyplot as plt
from model import *

st.sidebar.markdown("# Main page :heavy_dollar_sign:")
st.divider()

# Titre de l'application
st.title("Salary Prediction :moneybag:")
st.divider()

st.markdown(f"<h4>Anticipez votre trajectoire salariale 💵 avec confiance grâce à cette application intuitive, qui analyse vos années d'expérience 📈 pour vous fournir des estimations salariales personnalisées</h4>", unsafe_allow_html=True)

st.markdown("<h3>Dataset utilisé :</h3>", unsafe_allow_html=True)

st.write(dataset)

st.write("**_GRAPHIQUE DU SALAIRE EN FONCTION DES ANNEES D'EXPERIENCE:_**")

fig, ax = plt.subplots()

ax.scatter(X,y)
ax.set_xlabel("Salaire")    
ax.set_ylabel("Année d'experience") 
st.pyplot(fig)

st.write("")
st.write("")
st.write("")
st.write("")


st.write("**_NOTRE MODELE LINEAIRE :_**")
fig, ax = plt.subplots()
ax.plot(X_train, model_salary().predict(X_train), 'red')
ax.scatter(X_train,y_train)
ax.set_xlabel("Salaire")
ax.set_ylabel("Année d'experience") 
st.pyplot(fig)


