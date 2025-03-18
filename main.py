import re
import streamlit as st
st.markdown("""
        <style>
               .block-container {
                    padding-top: 35px;
                }
        </style>
        """, unsafe_allow_html=True)
st.title("🔏 Password Strength Meter")

errorList:list[str] = []

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    # Upper & Lowercase Check
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            errorList.append("both uppercase and lowercase letters")  # adding error in list
        
        # Digit Check
        if re.search(r"\d", password):
            score += 1
        else:
            errorList.append("atleast one number")  # adding error in list

        # Special Character Check
        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            errorList.append("atleast one special character (!@#$%^&*)") # adding error in list
    
    else:  # rendering error if the length of password is < 1
        st.error("❌ Password should be at least 8 characters long")
    
    if len(errorList)>1:   # loop for rendering multiple errors in a single line
        error = "Your password should contain "
        for i in range(len(errorList)):
            if(i<(len(errorList)-1)):
                error+=f"{errorList[i]}, "
            else:
                error+=f"and {errorList[i]}"
            
        st.error(error)

    elif len(errorList)==1:  # directly render error if length of errorList is == 1          
        st.error(f"Your password should contain {errorList[0]}")


    # Strength Rating
    if score == 4:
        st.caption("✅ Strong Password!")
    elif score == 3:
        st.caption("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.caption("❌ Weak Password - Improve it using the suggestions above.")


# Get user input
space = st.empty()
space.markdown("<br>",unsafe_allow_html=True)
password = st.text_input("Enter your password")
if st.button("Check Password"):
    check_password_strength(password)

