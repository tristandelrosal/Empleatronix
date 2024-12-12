import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('employees.csv')

st.title("Empleatronix")

# Display the dataframe
st.write("Los datos de los empleados:")
st.write(df)


# Plot a bar graph
# Create columns for color picker and switches
col1, col2, col3 = st.columns(3)
# Color picker
with col1:
    color = st.color_picker("Escoge un color:", "#0000ff")

# Add switches to show/hide names and salaries
with col2:
    show_names = st.toggle('Mostrar/Ocultar Nombres', value=True)
with col3:
    show_salaries = st.toggle('Mostrar/Ocultar Salarios', value=False)

# Plot the bar graph with conditions
fig, ax = plt.subplots()
if show_names:
    df.plot(kind='barh', x='full name', ax=ax, legend=False, color=color)
else:
    df_temp = df.copy()
    df_temp['full name'] = ""
    df_temp.plot(kind='barh', x='full name', ax=ax, legend=False, color=color)

# Remove x-axis label
ax.set_ylabel('')

# Set max y limit
ax.set_xlim(right=4500)

if show_salaries:
    for i, v in enumerate(df['salary']):
        ax.text(v + 3, i, f"{v}€", color='black', va='center')

st.pyplot(fig)