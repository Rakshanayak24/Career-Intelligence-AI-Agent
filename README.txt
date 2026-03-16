# Agentic JSO – HR Coaching AI Agent Prototype

This prototype demonstrates a simplified **Agentic Career Intelligence AI System** that analyzes HR consultation transcripts and generates performance insights along with coaching recommendations.

The system simulates a **multi-agent architecture** where different analytical components evaluate consultation quality, identify skill discussions, and generate job search optimization guidance.

---

# Prototype Features

The prototype performs the following analysis:

• Consultation transcript analysis  
• HR communication quality evaluation  
• Candidate engagement insights  
• Skill extraction from conversation  
• Career coaching recommendations  
• Job search optimization suggestions  

---

# Setup Instructions

## 1. Install Dependencies

Open your terminal and run:

```bash
cd prototype
pip install -r requirements.txt
pip install streamlit pandas textblob
python -m textblob.download_corpora
```

2. Run the AI Agent Prototype

Start the Streamlit application:
```bash
streamlit run app.py
```
The application will launch in your browser where you can paste a consultation transcript and generate AI insights.

Example Transcript for Testing

Paste the following sample consultation transcript into the application input field.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
HR Coach: Hi, thank you for joining the consultation today. Can you tell me about your current role and career goals?

Candidate: I currently work as a junior software developer. I mainly use JavaScript and Python, but I want to move toward data science or machine learning roles.

HR Coach: That’s a great goal. What kind of projects have you worked on recently?

Candidate: I have built some web applications and small data analysis scripts using Python.

HR Coach: Have you used SQL for data management or analysis?

Candidate: I know basic SQL but I haven't used it much in real projects.

HR Coach: I recommend strengthening your Python and SQL skills first. You should also start learning machine learning concepts and building portfolio projects.

Candidate: Should I also learn cloud technologies like AWS or Azure?

HR Coach: Yes, learning AWS or Azure will help you deploy machine learning models and build scalable systems.

Candidate: What kind of projects would you recommend for my portfolio?

HR Coach: Try building a recommendation system or a data visualization dashboard using Python. These projects will demonstrate your data science capabilities.

Candidate: That sounds helpful. Is there anything else I should focus on?

HR Coach: You should also learn Docker for deploying applications and consider contributing to open-source projects. This will improve your experience and visibility to recruiters.
Prototype Output
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
After analysis, the AI agent will generate insights including:

• HR consultation quality evaluation
• Candidate skill signals detected in the conversation
• Recommended technical skills to develop
• Suggested portfolio project ideas
• Career development guidance for the candidate

Technology Stack

The prototype is built using:

• Python
• Streamlit
• Pandas
• TextBlob (NLP analysis)

Purpose of Prototype

This prototype demonstrates how Agentic AI systems can transform consultation data into structured career intelligence insights.

In a production environment, this system would integrate with:

• Consultation platforms
• HR dashboards
• Career intelligence analytics systems
• Job Search Optimization (JSO) pipelines

to continuously improve career guidance quality.