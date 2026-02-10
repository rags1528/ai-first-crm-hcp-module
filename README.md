# 🧠 AI-First CRM – Healthcare Professional (HCP) Module

## 📌 Overview
This project implements an **AI-first Customer Relationship Management (CRM) module** tailored for field representatives in the life sciences domain.

The system enables users to log interactions with Healthcare Professionals (HCPs) using both:

✅ Structured form-based workflows  
✅ Conversational AI interface  

By leveraging **LangGraph-powered AI agents**, the platform converts unstructured interaction notes into structured CRM records — reducing manual effort while improving accuracy and productivity.

---

## 🚀 Key Features

### ✅ AI-Powered Interaction Logging
- Capture meeting notes using natural language.
- LLM automatically extracts:
  - Doctor Name  
  - Interaction Summary  
  - Sentiment  

---

### ✅ Hybrid CRM Experience
Combines conversational AI with structured workflows, aligning with modern enterprise CRM design principles.

---

### ✅ Structured Interaction Form
- Supports manual data entry.
- Automatically auto-populated using AI extraction.

---

### ✅ Edit Interaction Capability
- Allows controlled updates (e.g., sentiment).
- Demonstrates a realistic CRM data lifecycle.

---

### ✅ System-Generated Timestamp
- Date and time are automatically populated from the system clock.
- Eliminates manual input and improves audit reliability.

---

## 🧠 System Architecture

React Frontend
↓
FastAPI Backend
↓
LangGraph Agent
↓
Groq LLM
↓
MongoDB



---

## 🔄 Application Flow

1️⃣ User logs an interaction via chat or structured form  
2️⃣ LangGraph agent orchestrates the workflow  
3️⃣ LLM extracts structured entities  
4️⃣ Data is stored in MongoDB  
5️⃣ UI auto-updates with extracted values  

This architecture ensures an **AI-first yet deterministic system**, balancing automation with reliability.

---

## 🤖 Role of the LangGraph Agent

The LangGraph agent acts as the orchestration layer that manages the interaction lifecycle by:

- Receiving free-text interaction notes  
- Invoking AI tools  
- Extracting structured CRM data  
- Maintaining predictable workflow execution  

This approach enables scalable AI integration while preserving enterprise-grade control.

---

## 🛠️ AI Tools Implemented

### 🔹 Log Interaction Tool
Transforms unstructured notes into structured CRM records using LLM-based entity extraction.

### 🔹 Edit Interaction Tool
Supports controlled updates while ensuring data integrity.

---

### 🔹 Additional Conceptual Tools
- HCP Profile Retrieval  
- Automated Follow-up Recommendations  
- Interaction Summarization  

These tools illustrate the extensibility of the AI-agent architecture.

---

## 💻 Tech Stack

### **Frontend**
- React  
- Material UI  
- Google Inter Font  

### **Backend**
- FastAPI  
- LangGraph  

### **AI**
- Groq LLM (Llama)

### **Database**
- MongoDB  

---

## 📂 Project Structure

ai-first-crm-hcp-module
│
├── backend
│ ├── main.py
│ ├── agent.py
│ ├── tools.py
│ ├── routes.py
│ └── requirements.txt
│
├── frontend
│ ├── src
│ ├── package.json
│
└── README.md



A clean separation of frontend and backend promotes scalability and maintainability.

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

🔹 Frontend Setup
cd frontend
npm install
npm start

🔮 Future Enhancements
1. Authentication & role-based access
2. Voice-enabled interaction logging
3. AI-driven follow-up recommendations
4. Analytics dashboard

👨‍💻 Author
Raghavendra Venugopal
