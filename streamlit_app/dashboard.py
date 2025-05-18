# import streamlit as st
# import psycopg2
# import pandas as pd
# import plotly.express as px

# # الاتصال بـ PostgreSQL
# conn = psycopg2.connect(
#     dbname="student_db",
#     user="user",
#     password="password",  # حط الباسورد بتاعك هنا
#     host="postgres",
#     port="5432"
# )

# # عنوان الصفحة
# st.title("Student Data Dashboard")

# # 1. جدول grading_data (Students_Grading_Dataset)
# st.subheader("Students Grading Dataset")
# query_grading = 'SELECT "Student_ID", "Department", "Success_Rate", "Source" FROM grading_data'
# df_grading = pd.read_sql(query_grading, conn)
# st.dataframe(df_grading)

# # Visualizations لـ grading_data
# st.subheader("Visualizations for Students Grading Dataset")
# # Bar Chart: عدد الطلاب حسب القسم
# fig1 = px.bar(df_grading, x="Department", title="Number of Students per Department (Grading Data)")
# st.plotly_chart(fig1)
# # Histogram: توزيع Success_Rate
# fig2 = px.histogram(df_grading, x="Success_Rate", title="Distribution of Success Rate (Grading Data)")
# st.plotly_chart(fig2)
# # Pie Chart: توزيع المصادر
# fig3 = px.pie(df_grading, names="Source", title="Source Distribution (Grading Data)")
# st.plotly_chart(fig3)

# # 2. جدول performance_data (student_performance_large_dataset)
# st.subheader("Student Performance Large Dataset")
# query_performance = 'SELECT "Student_ID", "Department", "Success_Rate", "Source" FROM performance_data'
# df_performance = pd.read_sql(query_performance, conn)
# st.dataframe(df_performance)

# # Visualizations لـ performance_data
# st.subheader("Visualizations for Student Performance Large Dataset")
# # Bar Chart: عدد الطلاب حسب القسم
# fig4 = px.bar(df_performance, x="Department", title="Number of Students per Department (Performance Data)")
# st.plotly_chart(fig4)
# # Histogram: توزيع Success_Rate
# fig5 = px.histogram(df_performance, x="Success_Rate", title="Distribution of Success Rate (Performance Data)")
# st.plotly_chart(fig5)
# # Pie Chart: توزيع المصادر
# fig6 = px.pie(df_performance, names="Source", title="Source Distribution (Performance Data)")
# st.plotly_chart(fig6)

# # 3. جدول career_data (education_career_success)
# st.subheader("Education Career Success")
# query_career = 'SELECT "Student_ID", "Department", "Success_Rate", "Source" FROM career_data'
# df_career = pd.read_sql(query_career, conn)
# st.dataframe(df_career)

# # Visualizations لـ career_data
# st.subheader("Visualizations for Education Career Success")
# # Bar Chart: عدد الطلاب حسب القسم
# fig7 = px.bar(df_career, x="Department", title="Number of Students per Department (Career Data)")
# st.plotly_chart(fig7)
# # Histogram: توزيع Success_Rate
# fig8 = px.histogram(df_career, x="Success_Rate", title="Distribution of Success Rate (Career Data)")
# st.plotly_chart(fig8)
# # Pie Chart: توزيع المصادر
# fig9 = px.pie(df_career, names="Source", title="Source Distribution (Career Data)")
# st.plotly_chart(fig9)

# # إغلاق الاتصال
# conn.close()

# import streamlit as st
# import psycopg2
# import pandas as pd
# import plotly.express as px

# # الاتصال بـ PostgreSQL
# conn = psycopg2.connect(
#     dbname="student_db",
#     user="user",
#     password="password",  # حط الباسورد بتاعك هنا
#     host="postgres",
#     port="5432"
# )

# # عنوان الصفحة
# st.title("Student Data Dashboard")

# # 1. جدول grading_data (Students_Grading_Dataset)
# st.subheader("Students Grading Dataset")
# query_grading = 'SELECT "Student_ID", "Department", "Total_Score" AS "Success_Rate", "Source" FROM grading_data'
# df_grading = pd.read_sql(query_grading, conn)
# st.dataframe(df_grading)

# # Visualizations لـ grading_data
# st.subheader("Visualizations for Students Grading Dataset")
# # Bar Chart: عدد الطلاب حسب القسم
# fig1 = px.bar(df_grading, x="Department", title="Number of Students per Department (Grading Data)")
# st.plotly_chart(fig1)
# # Histogram: توزيع Success_Rate
# fig2 = px.histogram(df_grading, x="Success_Rate", title="Distribution of Success Rate (Grading Data)")
# st.plotly_chart(fig2)
# # Pie Chart: توزيع المصادر
# fig3 = px.pie(df_grading, names="Source", title="Source Distribution (Grading Data)")
# st.plotly_chart(fig3)

# # 2. جدول performance_data (student_performance_large_dataset)
# st.subheader("Student Performance Large Dataset")
# query_performance = 'SELECT "Student_ID", "Department", "Final_Grade" AS "Success_Rate", "Source" FROM performance_data'
# df_performance = pd.read_sql(query_performance, conn)
# st.dataframe(df_performance)

# # Visualizations لـ performance_data
# st.subheader("Visualizations for Student Performance Large Dataset")
# # Bar Chart: عدد الطلاب حسب القسم
# fig4 = px.bar(df_performance, x="Department", title="Number of Students per Department (Performance Data)")
# st.plotly_chart(fig4)
# # Histogram: توزيع Success_Rate
# fig5 = px.histogram(df_performance, x="Success_Rate", title="Distribution of Success Rate (Performance Data)")
# st.plotly_chart(fig5)
# # Pie Chart: توزيع المصادر
# fig6 = px.pie(df_performance, names="Source", title="Source Distribution (Performance Data)")
# st.plotly_chart(fig6)

# # 3. جدول career_data (education_career_success)
# st.subheader("Education Career Success")
# query_career = 'SELECT "Student_ID", "Department", "Career_Satisfaction" AS "Success_Rate", "Source" FROM career_data'
# df_career = pd.read_sql(query_career, conn)
# st.dataframe(df_career)

# # Visualizations لـ career_data
# st.subheader("Visualizations for Education Career Success")
# # Bar Chart: عدد الطلاب حسب القسم
# fig7 = px.bar(df_career, x="Department", title="Number of Students per Department (Career Data)")
# st.plotly_chart(fig7)
# # Histogram: توزيع Success_Rate
# fig8 = px.histogram(df_career, x="Success_Rate", title="Distribution of Success Rate (Career Data)")
# st.plotly_chart(fig8)
# # Pie Chart: توزيع المصادر
# fig9 = px.pie(df_career, names="Source", title="Source Distribution (Career Data)")
# st.plotly_chart(fig9)

# # إغلاق الاتصال
# conn.close()


import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

# الاتصال بـ PostgreSQL
conn = psycopg2.connect(
    dbname="student_db",
    user="user",
    password="password",
    host="postgres",
    port="5432"
)

# عنوان الصفحة
st.title("Student Data Dashboard")

# 1. جدول grading_data (Students_Grading_Dataset)
st.subheader("Students Grading Dataset")
query_grading = 'SELECT "Student_ID", "Department", "Total_Score" AS "Success_Rate", "Source" FROM grading_data'
df_grading = pd.read_sql(query_grading, conn)
st.dataframe(df_grading)

# Visualizations لـ grading_data
st.subheader("Visualizations for Students Grading Dataset")
# Bar Chart: عدد الطلاب حسب القسم
fig1 = px.bar(df_grading, x="Department", title="Number of Students per Department (Grading Data)")
st.plotly_chart(fig1)
# Histogram: توزيع Success_Rate
fig2 = px.histogram(df_grading, x="Success_Rate", title="Distribution of Success Rate (Grading Data)")
st.plotly_chart(fig2)
# Pie Chart: توزيع المصادر
fig3 = px.pie(df_grading, names="Source", title="Source Distribution (Grading Data)")
st.plotly_chart(fig3)

# 2. جدول performance_data (student_performance_large_dataset)
st.subheader("Student Performance Large Dataset")
# بما إن "Department" مش موجود، نستخدم عمود موجود (مثل "Preferred_Learning_Style" أو "Final_Grade")
query_performance = 'SELECT "Student_ID", "Preferred_Learning_Style" AS "Department", "Final_Grade" AS "Success_Rate", "Source" FROM performance_data'
df_performance = pd.read_sql(query_performance, conn)
st.dataframe(df_performance)

# Visualizations لـ performance_data
st.subheader("Visualizations for Student Performance Large Dataset")
# Bar Chart: عدد الطلاب حسب Preferred_Learning_Style (بديل لـ Department)
fig4 = px.bar(df_performance, x="Department", title="Number of Students per Preferred Learning Style (Performance Data)")
st.plotly_chart(fig4)
# Histogram: توزيع Success_Rate
fig5 = px.histogram(df_performance, x="Success_Rate", title="Distribution of Success Rate (Performance Data)")
st.plotly_chart(fig5)
# Pie Chart: توزيع المصادر
fig6 = px.pie(df_performance, names="Source", title="Source Distribution (Performance Data)")
st.plotly_chart(fig6)

# 3. جدول career_data (education_career_success)
st.subheader("Education Career Success")
query_career = 'SELECT "Student_ID", "Field_of_Study" AS "Department", "Career_Satisfaction" AS "Success_Rate", "Source" FROM career_data'
df_career = pd.read_sql(query_career, conn)
st.dataframe(df_career)

# Visualizations لـ career_data
st.subheader("Visualizations for Education Career Success")
# Bar Chart: عدد الطلاب حسب القسم
fig7 = px.bar(df_career, x="Department", title="Number of Students per Field of Study (Career Data)")
st.plotly_chart(fig7)
# Histogram: توزيع Success_Rate
fig8 = px.histogram(df_career, x="Success_Rate", title="Distribution of Success Rate (Career Data)")
st.plotly_chart(fig8)
# Pie Chart: توزيع المصادر
fig9 = px.pie(df_career, names="Source", title="Source Distribution (Career Data)")
st.plotly_chart(fig9)

# إغلاق الاتصال
conn.close()