# import streamlit as st
# import pickle

# model = pickle.load(open('spam.pkl','rb'))
# cv = pickle.load(open('vec.pkl','rb'))

# def main():
# 	st.title("Email Spam Classification Application")
# 	st.write("This is a Machine Learning application to classify emails as spam or ham.")
# 	st.subheader("Classification")
# 	user_input=st.text_area("Enter an email to classify" ,height=150)
# 	if st.button("Classify"):
# 		if user_input:
# 			data=[user_input]
# 			print(data)
# 			vec=cv.transform(data).toarray()
# 			result=model.predict(vec)
# 			if result[0]==0:
# 				st.success("This is Not A Spam Email")
# 			else:
# 				st.error("This is A Spam Email")
# 		else:
# 			st.write("Please enter an email to classify.")
# main()


import streamlit as st
import pickle

# Load the machine learning model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vec.pkl', 'rb'))

def main():
    # App title
    st.title("📧 Email Spam Classification Application")
    st.markdown(
        """
        Welcome to the **Email Spam Classifier**!  
        This application uses a **Machine Learning** model to determine whether an email is spam or not.
        """
    )
    
    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.info(
        """
        - Enter your email text in the input box.
        - Click **Classify** to check if it's spam or not.
        """
    )
    st.sidebar.markdown(
        """
        ### About
        This app is built using **Streamlit** and **Machine Learning** techniques.  
        Trained using NLP features like **CountVectorizer**.
        """
    )

    # Input Section
    st.subheader("🔍 Classify Your Email")
    user_input = st.text_area(
        "Type or paste the email content here 👇",
        height=150,
        placeholder="E.g., Congratulations! You've won a $1000 gift card. Claim now!"
    )

    # Button to classify email
    if st.button("🚀 Classify"):
        if user_input.strip():
            # Preprocess input and predict
            data = [user_input]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)

            # Display result
            if result[0] == 0:
                st.success("✅ This is **NOT** a Spam Email.")
            else:
                st.error("🚨 This is a **Spam Email**.")
        else:
            st.warning("⚠️ Please enter some content to classify.")

    # Footer
    st.markdown(
        """
        ---
        ### 🚀 Powered by Machine Learning
        - Built with **Streamlit**
        - Using a pre-trained **Naive Bayes Classifier** for spam detection
        """
    )

# Run the main function
if __name__ == '__main__':
    main()
