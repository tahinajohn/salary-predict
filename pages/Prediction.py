import streamlit as st
from model import *
from fire_state import create_store, get_state, set_state

slot = "Prediction"

key1 = create_store(slot, [
    ("state1", ''),
    ("state2", '')
])

def predict():
    new_value = np.array([float(y_e)]).reshape(-1, 1)
    print("value = ", new_value)
    m_p = model_salary().predict(new_value)
    formated_mp = "{:.2f}".format(m_p[0])
    set_state(slot, ("state2", f"<h2 style='text-align: center;'> Vous méritez d'avoir: {formated_mp} Dollars💲</h2>"))

st.markdown("# Prediction :bar_chart:")
st.sidebar.markdown("# Prediction :bar_chart:")

y_e = st.text_input("Entrer votre année d'experience :", value=get_state(slot, 'state1'))

set_state(slot, ("state1", y_e))

prediction_button = st.button("Prédire salaire", on_click=predict)

response = st.markdown(f"{get_state(slot, 'state2')}",unsafe_allow_html=True)

