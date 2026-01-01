🏦 Bank Marketing Deposit Prediction — Machine Learning Project

This project predicts whether a customer will subscribe to a term deposit based on bank marketing campaign data.  
It includes a trained ML model and an interactive Streamlit web app for real-time prediction.

The project includes:
- Data cleaning & preprocessing
- Feature engineering (age/balance grouping)
- One-hot encoding & feature scaling
- Model training and evaluation
- Deployment as an interactive Streamlit web app

📌 Tech Stack: Python, Pandas, Scikit-Learn, Streamlit

📦 Model File (Download)

The trained model file (`bank.pkl`) is larger than GitHub’s upload limit, so it’s hosted externally.

👉 **[Download bank.pkl from Google Drive](https://drive.google.com/file/d/1xtdSMh9vvAre5gZeK33W5Msd3BU0kt9-/view?usp=sharing)**

After downloading, place the file in the project folder (same directory as `app.py`) before running the Streamlit app.


📂 Project Structure

| File | Description |
|------|------------|
| `app.py` | Streamlit web application |
| `bank.pkl` | Trained ML model + encoder + scaler |
| `bank.csv` | Dataset used for model training |
| `main.ipynb` | Model training & experimentation notebook |
| `requirements.txt` | Project dependencies |

## 🚀 How to Run the Project

1️⃣ Install the required libraries

```bash
pip install -r requirements.txt
```

2️⃣ Download the model file and place it in the project folder

➡️ `bank.pkl` must be in the same directory as `app.py`

3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```
