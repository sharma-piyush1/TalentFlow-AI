# 🚀 TalentFlow AI: The Autonomous Recruitment Engine

## Streamlit App: 
https://talentflow-ai.streamlit.app

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/Powered_by-CrewAI-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

**TalentFlow AI** is a multi-agent system designed to automate the early stages of recruitment. It employs a team of intelligent AI agents to **source** candidates from the web, **analyze** their fit against a Job Description, and **draft** personalized outreach emails—all within a clean, interactive Human-in-the-Loop interface.

---

## 🌟 Key Features

* **🔍 Agentic Web Sourcing:** Uses `Exa.ai` (Neural Search) to find high-quality candidate profiles (LinkedIn, GitHub, Portfolios) that match specific tech stacks.
* **🧠 Intelligent Profiling:** A specialized Profiler Agent scores candidates (0-10) based on strict JD alignment using **Google Gemini**.
* **👨‍💻 Human-in-the-Loop Workflow:** The AI doesn't just run wild. It presents candidates in an interactive table for you to review, filter, and edit before proceeding.
* **📧 Automated Outreach:** Generates hyper-personalized cold emails referencing specific skills and projects found in the candidate's profile.
* **📊 Structured Data Export:** Download your shortlisted candidates and their scores as a CSV file for your ATS or Excel.

---

## 🛠️ Tech Stack

* **Framework:** [CrewAI](https://crewai.com) (Multi-Agent Orchestration)
* **Interface:** [Streamlit](https://streamlit.io) (Web UI)
* **LLM Provider:** Google gemini-3-flash-preview (via OpenAI Compatibility Layer)
* **Search Tool:** [Exa.ai](https://exa.ai) (Neural Search API)
* **Language:** Python 3.10+

---

## 📂 Project Structure

```text
TalentFlow-AI/
├── src/
│   ├── agents.py       # Defines the Researcher, Profiler, and Writer agents
│   ├── tasks.py        # Defines the specific instructions for each agent
│   ├── tools.py        # Custom tool for Exa.ai candidate search
│   ├── models.py       # Pydantic models for structured data output
│   ├── main.py         # (Optional) CLI entry point for testing
│   └── app.py          # Main Streamlit Application (The UI)
├── requirements.txt    # Python dependencies
├── .env                # API Keys (Not included in repo)
├── .gitignore          # Files to ignore (secrets, venv)
└── README.md           # Documentation
```
## Installation & Setup

1. Clone the Repository
```bash
git clone [https://github.com/sharma-piyush1/TalentFlow-AI.git](https://github.com/sharma-piyush1/TalentFlow-AI.git)
cd TalentFlow-AI
```
2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Configure API Keys
```bash
# Get a free key from [https://aistudio.google.com/](https://aistudio.google.com/)
GOOGLE_API_KEY="AIzaSy..."

# Get a free key from [https://exa.ai/](https://exa.ai/)
EXA_API_KEY="exa-..."
```

## 🎮 How to Use
1. Run the App:
```bash
streamlit run app.py
```

2. Input Job Details: Paste your Job Description into the sidebar (e.g., "Senior Python Developer in Bhopal").

3. Start Search: Click "Find & Score Candidates". The agents will start searching the web.

4. Review & Filter: A table will appear with found candidates. Uncheck anyone you don't like.

5. Generate Emails: Click "Write Emails". The Writer Agent will draft messages only for your selected candidates.

6. Export: Download the CSV or copy the emails.

## 🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

1. Fork the Project

2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

3. Commit your Changes (git commit -m 'Add some AmazingFeature')

4. Push to the Branch (git push origin feature/AmazingFeature)

5. Open a Pull Request