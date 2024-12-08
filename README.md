# P3-Spam-Mail-Classification-by-NLP-and-ML

<h1>📧 Email Spam Classification Application</h1>

This project is an **Email Spam Classification Application** built using **Machine Learning** and **Natural Language Processing (NLP)** techniques. The application allows users to input email content and predicts whether it is a **Spam** email or **Not Spam** using a trained model.

The project includes:
- A machine learning model trained on a dataset of spam and ham emails.
- A user-friendly web interface built with **Streamlit**.

![image](https://github.com/user-attachments/assets/0fb63352-aaf6-4f69-8206-955f067c519a)


---

<h2>🛠️ How to Execute the Project</h2>

### Requirements:
- Python 3.8 or higher
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Pickle

### Steps to Run the Application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abhishek0112cs221008/Spam-Mail-Classification-by-NLP-and-ML.git
   cd Spam-Mail-Classification-by-NLP-and-ML
   
2. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Application**:
    ```bash
    streamlit run Spam_Detector.py

4. **Access the App**:
  - Open your browser and navigate to the URL shown in the terminal (e.g., http://localhost:8501).
   
5. **Classify Emails**:
  - Input an email in the provided text box.
  - Click "Classify" to determine if the email is spam or not.


<h2>📋 Project Overview</h2>

  This project leverages NLP for text preprocessing and feature extraction and uses a Naive Bayes Classifier for spam detection.

<h2>📁 Project Structure</h2>
    ``` bash
    
    Spam-Mail-Classification-by-NLP-and-ML/
    │
    ├── spam.pkl              # Pre-trained spam classification model
    ├── vec.pkl               # Trained CountVectorizer object for feature extraction
    ├── requirements.txt      # List of dependencies
    ├── Spam_Detector.py      # Main Streamlit app script
    ├── spam.csv              # Sample dataset of spam and ham emails (if applicable)
    ├── README.md             # Documentation

<h2>✨ Thanks' 😊</h2>
