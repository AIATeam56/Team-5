import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


@st.cache_data
def train():
    data = pd.read_csv(
        "/home/sam/Documents/projects/personal/ai/creditcard_2023.csv", header=0
    )

    x_train, x_test, y_train, y_test = train_test_split(
        data[data.columns.to_list()[:-1]],
        data.Class,
        test_size=0.25,
        random_state=16,
        shuffle=True,
    )

    model = LogisticRegression(random_state=16, max_iter=10000)
    model.fit(x_train, y_train)

    return data, model, [x_test, y_test]


data, model, [x_test, y_test] = train()

st.title("Credit Card Fraud Detection")

st.subheader("Raw data")
st.write(data)


st.subheader("Test data")
st.write(x_test)

index = st.select_slider(
    "Select test index",
    options=range(1, len(x_test)),
)
st.write("You selected the following row:", x_test[index : index + 1])
st.write(f"It is {"" if y_test[index:index+1].values[0] == 1 else "not "}fraudulent.")
st.write(
    f"Predicted as: {"" if model.predict(x_test[index : index + 1])[0] == 1 else "not "}fraudulent."
)
