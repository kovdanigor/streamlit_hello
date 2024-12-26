
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Генерация данных


# Импорт необходимых библиотек
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Функция для генерации данных


def generate_data():
    np.random.seed(np.random.randint(0, 10000))
    data = {
        'Category': np.random.choice(['A', 'B', 'C'], size=100),
        'Value': np.random.randint(10, 100, size=100),
        'Date': pd.date_range(start='2024-01-01', periods=100, freq='D')
    }
    return pd.DataFrame(data)


st.title("Визуализация данных в Streamlit с кнопками")


if "data" not in st.session_state:
    st.session_state["data"] = generate_data()


st.subheader("Управление данными")
if st.button("Сгенерировать новые данные"):
    st.session_state["data"] = generate_data()
    st.success("Данные обновлены!")


df = st.session_state["data"]
st.subheader("Сгенерированные данные")
st.write(df)


st.subheader("График данных")

fig = px.line(
    df,
    x="Date",
    y="Value",
    color="Category",
    title="График значений по категориям"
)
st.plotly_chart(fig)
