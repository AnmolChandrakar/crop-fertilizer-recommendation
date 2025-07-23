Team Members:
1. Milind Panda_(Roll_no.:24CSE097)_(Reg_no.:24UG010163)
2. Anmol Chandrakar_(Roll_no.:24CSEAIML239_)(Reg_no.:24UG010733)
3. Blesson Oddu_(Roll_no.:24CSEAIML234)_(reg_no.:24UG010729)
4. Ankit Kumar Nayak_(Roll_no.:24CSEAIML233)_(Reg_no:24UG010728)

## Project Presentation
[Download the PPT here](Crop_Fertilizer_recommendation(TEAM(SC1)_10).pptx)


Problem statement:

Farmers often face difficulty in selecting the right crop for cultivation due to a lack of scientific knowledge about soil composition, weather conditions, and fertilizer requirements. Wrong crop selection or improper fertilizer use leads to low yield, poor soil health, and financial losses.

There is a need for a data-driven decision support system that can recommend suitable crops and fertilizers based on real soil and environmental parameters (N, P, K levels, pH, temperature, humidity, and rainfall). Such a system can help farmers make better decisions, optimize resources, and increase productivity.

Description:

This project helps farmers choose the best crop to grow based on their soil and weather conditions. By entering values like soil nutrients (N, P, K), pH, temperature, humidity, and rainfall, the system suggests the most suitable crops. It also gives fertilizer advice to improve soil quality. This tool makes farming decisions easier and more scientific.

Tech Stack:

Programming Language: Python
Data Processing: Pandas, NumPy
Machine Learning: Scikit-learn (SVM Classifier)
Web Framework/UI: Streamlit
Model Serialization: Pickle
Dataset: Kaggle Crop Recommendation Dataset
Version Control: Git & GitHub

Installation & Running:

1. Prerequisites
   Python 3.8+ installed on your computer.
   pip (Python package manager).

2. Clone or Download the Repository

   git clone https://github.com/AnmolChandrakar/crop-fertilizer-recommendation.git
   cd crop-fertilizer-recommendation
   (Or download the ZIP from GitHub and extract it.)

3. Install Dependencies

   pip install -r requirements.txt

4. Run the Streamlit App

   streamlit run app.py
   
   The app will open in your web browser.

5. Use the Application

   Enter soil and weather parameters: N, P, K, temperature, humidity, pH, rainfall.

   Click “Recommend Crop”.

   View:

   Top 3 crop recommendations.

   Fertilizer advice (NPK).

   Water requirement and how much more water is needed.

6. Stop the Server

   Press Ctrl + C in the terminal.


