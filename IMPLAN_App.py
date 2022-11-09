import pandas as pd
import streamlit as st
import plotly.express as px

# Set the page title and header
st.set_page_config(page_title='IMPLAN Results')
st.title("Industry-specific Benefits of CISFs")

# Load the data and group them per industry
data = pd.read_csv('./Trade_Off_Analysis_Kazi.csv')
data = data.round()
dataGrouped = data.groupby("Industry Sector").sum().round()

# Display the grouped dataframe
# st.dataframe(dataGrouped.style.set_precision(0))

# Create lists holding the name of industries and categories
industry = dataGrouped.index.unique().tolist()
category = dataGrouped.columns.unique().tolist()

# Create selection options
category_selection1 = st.selectbox("Select a Category for Industry Breakdown",category)

# Create a pie chart for jobs
pie_chart = px.pie(dataGrouped,
                    # title='Industry Contributions',
                    values=category_selection1,
                    names=dataGrouped.index,
                    color_discrete_sequence=px.colors.sequential.Blugrn)

# Display the plot
st.plotly_chart(pie_chart)

# Create selection options
industry_selection= st.selectbox("Select an Industry",industry)
category_selection2 = st.selectbox("Select a Category",category)

data = data[data['Industry Sector']==industry_selection]
data = data[['Description',category_selection2]]

data = data[data[category_selection2]>=1]

bar_chart = px.bar(data,
                x = category_selection2,
                y = 'Description',
                # title = "Industry Breakdown",
                color=category_selection2,
                color_continuous_scale='Blugrn',
                orientation='h',
                template='ggplot2')

# bar_chart.update_traces(marker_color = '#007f71')

st.plotly_chart(bar_chart)
