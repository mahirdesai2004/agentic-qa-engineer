# 🤖 Agentic AI QA Engineer

An AI-powered automated testing system that converts **natural language requirements** into executable Selenium tests using **Google Gemini AI**.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5-purple.svg)
![Selenium](https://img.shields.io/badge/Automation-Selenium-green.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)

---

## ✨ Features

- 🧠 **AI-Powered Test Generation** - Describe requirements in plain English
- 🌐 **Selenium Automation** - Automatic browser testing with explicit waits
- 📸 **Screenshot Capture** - Automatic screenshots on test failure
- 🔍 **Intelligent Failure Analysis** - AI explains why tests fail
- 🛡️ **Guardrails** - Validates AI output before execution

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment

Create a `.env` file with your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=models/gemini-2.5-flash
```

### 3. Start the Test Website

```bash
python serve_test_sites.py
```

This starts a local server with demo pages:
- **Login**: http://localhost:8000/login
- **Signup**: http://localhost:8000/signup

**Demo credentials**: `admin` / `password123`

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📋 Test Scenarios

### ✅ PASS Case - Invalid Login Should Show Error

**Requirement:**
> "User should not be able to login with wrong password"

**Expected Result:** 
- AI generates steps to enter wrong credentials
- System correctly shows "Invalid credentials" message
- Test **PASSES** ✅

### ❌ FAIL Case - Valid Login But Wrong Message Expected

**Requirement:**
> "User should see welcome message after login"

*Using wrong credentials will show error instead of welcome → Test FAILS*

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        STREAMLIT UI                             │
│                   User enters requirement + URL                 │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                        AI AGENT                                 │
│  • Gemini 2.5 Flash                                             │
│  • Converts requirements → JSON test steps                      │
│  • Explains failures with context                               │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EVALUATION LAYER                             │
│  • Validates AI output structure                                │
│  • Guardrails: only allowed actions pass through                │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                   SELENIUM RUNNER                               │
│  • WebDriverWait for stability                                  │
│  • Screenshot on failure                                        │
│  • Clean browser lifecycle                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
agentic-qa-engineer/
├── app.py                 # Streamlit UI
├── ai_agent.py            # Gemini AI integration
├── selenium_runner.py     # Browser automation
├── evaluation_layer.py    # Input validation
├── notifier.py            # Notification system
├── serve_test_sites.py    # Local test server
├── test_websites/
│   ├── login/             # Demo login page
│   └── signup/            # Demo signup page
├── screenshots/           # Failure screenshots (auto-generated)
├── requirements.txt
└── README.md
```

---

## 🔧 Supported Actions

| Action | Description | Example |
|--------|-------------|---------|
| `navigate` | Go to URL | `{"action": "navigate"}` |
| `input` | Type into field | `{"action": "input", "selector": "username", "value": "test"}` |
| `click` | Click element | `{"action": "click", "selector": "button"}` |
| `check` | Verify text | `{"action": "check", "selector": "message", "value": "Invalid"}` |

---

## 🛡️ Prerequisites

- Python 3.12+
- Chrome browser
- ChromeDriver (matching your Chrome version)
- Gemini API key

---

## 👥 Team

Built for hackathon demonstration of agentic AI capabilities.

---

## 📄 License

MIT License
