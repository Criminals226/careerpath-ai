# CareerPath AI- AI-Powered Career Guidance Assistant

CareerPath AI is a conversational AI application designed to help university students and fresh graduates explore career options, identify skill gaps, and develop practical learning plans based on their goals and current abilities.

The project uses a Large Language Model (LLM) through the OpenRouter API to generate responses to users' questions.

## Features

* **Conversational AI:** Ask questions and receive AI-generated guidance.
* **Career Exploration:** Explore career paths related to your education, interests, and skills.
* **Skill Development:** Identify skills to learn for a target role.
* **Learning Roadmaps:** Get structured suggestions for learning and practice.
* **Personalized Guidance:** Use relevant background information and constraints to tailor recommendations.
* **Follow-up Questions:** Continue a conversation to explore a topic in more detail.

*Features depend on the functionality implemented in the current version of the application.*

## Technology Stack

* Python
* Streamlit
* OpenRouter API
* OpenAI Python SDK
* python-dotenv
* A compatible language model accessed through OpenRouter

## Project Structure

```text
careerpath-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env                 # Local configuration; not committed
```

The exact structure may vary depending on the files included in your implementation.

## Getting Started

### Prerequisites

* Python 3.9 or a compatible supported Python version
* Git
* An OpenRouter API key

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/careerpath-ai.git
cd careerpath-ai
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_actual_api_key
OPENROUTER_MODEL=openrouter/free
```

Replace the placeholder API key with your own key. The configured model must be available to your OpenRouter account.

**Security:** Never commit `.env` or publish your API key. The repository should exclude `.env` through `.gitignore`.

### 5. Run the application

```powershell
streamlit run app.py
```

Streamlit will provide a local URL, typically `http://localhost:8501`.

## How It Works

1. The user submits a question through the Streamlit interface.
2. The application prepares the request and relevant conversation context.
3. The request is sent to a language model through OpenRouter.
4. The model generates a response using its learned knowledge and the supplied context.
5. The application displays the response to the user.

The application does not require a separate training process for the underlying language model.

## Limitations

* AI-generated guidance may contain inaccuracies and should be independently verified.
* Model availability and response quality depend on the selected model and API service.
* CareerPath AI does not guarantee employment, salaries, or admission outcomes.
* Current job openings and salary information should be verified through reliable, up-to-date sources.
* Recommendations are guidance, not a substitute for independent research or professional advice.

## Future Improvements

* Improve response relevance and conversation management.
* Strengthen personalization using user-provided career profiles.
* Add reliable web search for current career and job-market information.
* Evaluate response quality using a structured test suite.
* Improve error handling and deployment reliability.

## Project Links

* **GitHub Repository:** https://github.com/criminals226/careerpath-ai
* **Live Demo:** Add your deployed application URL when available.

## Author

**Aleena Khalid**

Cybersecurity graduate exploring Artificial Intelligence, Machine Learning, and practical LLM application development.

---

*Developed as an AI chatbot development project.*
