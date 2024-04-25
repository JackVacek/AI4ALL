import streamlit as st
import pickle
import pandas as pd
def load_model():
    with open('linear_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()
def main():
    st.title("CS Salary Calculator")

    # User inputs
    a = st.text_input("Age:", "")
    g = st.selectbox("Gender:", ["Male", "Female"])
    ed = st.selectbox("Education Level:", ["High School", "Bachelor's", "Master's", "PhD"])
    jt = st.selectbox("Job Title:",['Software Engineer Manager', 'Full Stack Engineer', 'Senior Software Engineer', 'Senior Project Engineer', 'Data Scientist', 'Back end Developer', 'Software Engineer', 'Front end Developer', 'Data Analyst', 'Web Developer', 'Software Developer', 'Junior Web Developer', 'Senior Data Scientist', 'Junior Software Developer', 'Junior Software Engineer', 'Director of Data Science', 'Front End Developer', 'Senior Data Analyst', 'Senior Software Developer', 'Senior Data Engineer', 'Senior UX Designer', 'Junior Data Analyst', 'IT Support Specialist', 'Chief Data Officer', 'Data Entry Clerk', 'IT Support', 'Software Manager', 'Junior Developer', 'UX Designer', 'Network Engineer', 'Help Desk Analyst', 'UX Researcher', 'IT Manager', 'Technical Support Specialist', 'Senior Software Architect', 'Senior IT Consultant', 'Junior UX Designer', 'Chief Technology Officer', 'Senior IT Project Manager', 'Junior Designer', 'Junior Data Scientist', 'Senior IT Support Specialist', 'Junior Web Designer', 'Software Project Manager'])
    yoe = st.text_input("Years of Experience:","")
    if st.button("Predict"):
        # Make prediction using the model
        data = {"Age":a,"Gender":g,"Education Level":ed, "Job Title":jt, "Years of Experience":yoe}
        df = pd.DataFrame(data,index = [0])
        prediction = model.predict(df)[0]
        st.write(f"Salary Prediction: ₹{prediction:.2f}/Month")
        st.write(f"This is equal to: ${float(prediction)*0.012:.2f}/Month")
        if data[1] != "Male:
            data = {"Age":a,"Gender":"Male","Education Level":ed, "Job Title":jt, "Years of Experience":yoe}
            df = pd.DataFrame(data,index = [0])
            prediction = model.predict(df)[0]
            st.write(f"If you were a male you would make: ₹{prediction:.2f}/Month")
        st.write(f"This is equal to: ${float(prediction)*0.012:.2f}/Month")
if __name__ == "__main__":
    main()
