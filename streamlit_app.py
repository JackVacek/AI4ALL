import streamlit as st
import pickle
import pandas as pd
def load_model():
    with open('linear_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()
def main():
    st.title("Model Demo")

    # User inputs
    a = st.text_input("Age:", "")
    g = st.selectbox("Gender:", ["Male", "Female"])
    ed = st.selectbox("Education Level:", ["High School", "Bachelor's", "Master's", "PhD"])
    jt = st.selectbox("Job Title:",['Software Engineer Manager', 'Full Stack Engineer', 'Senior Software Engineer', 'Senior Project Engineer', 'Data Scientist', 'Back end Developer', 'Software Engineer', 'Front end Developer', 'Data Analyst', 'Product Manager', 'Web Developer', 'Marketing Coordinator', 'Sales Manager', 'Software Developer', 'Sales Associate', 'Junior Web Developer', 'Senior Data Scientist', 'Marketing Analyst', 'Financial Analyst', 'Junior Software Developer', 'Junior Software Engineer', 'Director of Data Science', 'Front End Developer', 'Senior Software Developer', 'Senior Scientist', 'Senior Data Analyst', 'Senior Manager', 'HR Manager', 'Senior Data Engineer', 'Senior UX Designer', 'Senior Engineer', 'Junior Data Analyst', 'Junior Designer', 'Senior Software Architect', 'Junior Developer', 'Senior Consultant', 'UX Designer', 'Network Engineer', 'Help Desk Analyst', 'UX Researcher', 'Director', 'IT Manager', 'VP of Operations', 'Technical Support Specialist', 'Senior IT Consultant', 'Chief Data Officer', 'Junior UX Designer', 'Data Entry Clerk', 'Senior IT Project Manager', 'Chief Technology Officer', 'Junior Data Scientist', 'Senior IT Support Specialist', 'Junior Web Designer', 'Software Manager', 'Software Project Manager', 'IT Support Specialist', 'IT Support'])
    yoe = st.text_input("Years of Experience:","")
    if st.button("Predict"):
        # Make prediction using the model
        data = {"Age":a,"Gender":g,"Education Level":ed, "Job Title":jt, "Years of Experience":yoe}
        df = pd.DataFrame(data,index = [0])
        prediction = model.predict(df)
        st.write(f"Salary Prediction (Monthly in Rupees): {prediction}")

if __name__ == "__main__":
    main()