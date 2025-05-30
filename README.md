# 💡 Financial Support Recommendation System

This service evaluates financial documents and credit information to determine whether an applicant is eligible for financial support. It leverages agent-based reasoning using **CrewAI** to provide transparent and explainable recommendations.

---

## 🎯 Purpose

To analyze submitted applicant data and generate a decision on whether to:
- ✅ **Approve** the financial support, or  
- ⚠️ **Soft Decline** based on risk and capacity evaluation.

---

## 🧱 Components

- **Frontend:**  
  - Built with **Streamlit**.  
  - Allows users to input an **Applicant ID**.

- **Backend:**  
  - Powered by an **AI decision engine** using **CrewAI agents**.  
  - Performs analysis on bank statements, credit info, and related metadata.

---

## 🔁 Workflow

### 1. User Action
- User enters the **Applicant ID** in the Streamlit interface.
- Clicks "Submit" to trigger the recommendation pipeline.

### 2. Backend Processing
- The backend fetches relevant applicant data:
  - Bank Statement
  - Credit Report
  - Document Metadata

- CrewAI agents perform:
  - 📊 Financial capacity analysis
  - 🚦 Risk parameter evaluation
  - 🔍 Contextual reasoning and insight generation

### 3. Decision Output
- The service provides one of the following:
  - ✅ **Approved** – if financial health is satisfactory.
  - ⚠️ **Soft Decline** – if risk indicators are present.

- Decision is accompanied by **insights and rationale** for transparency and auditability.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- CrewAI
- PostgreSQL / MongoDB (data backend)
- Pandas / Langchain (for data handling and NLP)

---

## 🚀 Getting Started

Clone the Repository and follow below steps
```bash
1. git clone https://github.com/karishmac91/Generate_Agent.git
cd Generate_Agent

2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment
POSTGRES_URI=postgresql://user:password@localhost:5432/yourdb
MONGODB_URI=mongodb://localhost:27017

5. Run the app
streamlit run app.py
