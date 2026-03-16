import streamlit as st
import pandas as pd
import re
from textblob import TextBlob
from collections import Counter

st.set_page_config(page_title="Agentic JSO Career Intelligence Agent", layout="wide")

st.title("Agentic JSO – Career Intelligence AI Agent")
st.caption("A lightweight agentic system for analyzing HR consultations and generating job search optimization strategies.")
st.write("AI-powered consultation analysis and job search optimization system")

# ----------------------------------------
# Knowledge Bases
# ----------------------------------------

SKILLS_DB = [
    "python","java","javascript","sql","aws","azure","cloud","machine learning",
    "data science","react","node","docker","kubernetes","tableau","power bi"
]

ADVICE_KEYWORDS = [
    "recommend","suggest","should","consider","improve","build","learn",
    "practice","develop","focus","optimize","update"
]

QUESTION_WORDS = ["why","what","how","when","where","should","can"]

# ----------------------------------------
# Agent Modules
# ----------------------------------------

def skill_extraction_agent(text):
    detected = []
    text_lower = text.lower()

    for skill in SKILLS_DB:
        if skill in text_lower:
            detected.append(skill)

    return detected


def conversation_analysis_agent(text):

    words = re.findall(r'\w+', text.lower())
    sentences = re.split(r'[.\n]', text)

    word_count = len(words)
    question_count = text.count("?")

    advice_count = sum(
        1 for word in words if word in ADVICE_KEYWORDS
    )

    clarity_score = min(word_count // 25 + 4, 10)
    engagement_score = min(question_count * 2 + 3, 10)
    guidance_score = min(advice_count + 4, 10)

    return {
        "words": word_count,
        "questions": question_count,
        "advice": advice_count,
        "clarity": clarity_score,
        "engagement": engagement_score,
        "guidance": guidance_score
    }


def sentiment_agent(text):

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        label = "Positive"
    elif polarity < -0.2:
        label = "Negative"
    else:
        label = "Neutral"

    return polarity, label


def career_gap_agent(skills):

    target_skills = [
        "python","sql","machine learning","cloud","aws","docker"
    ]

    missing = []

    for s in target_skills:
        if s not in skills:
            missing.append(s)

    return missing


def coaching_recommendation_agent(metrics):

    suggestions = []

    if metrics["engagement"] < 6:
        suggestions.append(
            "Ask more diagnostic questions to better understand candidate goals."
        )

    if metrics["guidance"] < 6:
        suggestions.append(
            "Provide more structured and actionable career guidance."
        )

    if metrics["clarity"] < 6:
        suggestions.append(
            "Break down advice into step-by-step recommendations."
        )

    if len(suggestions) == 0:
        suggestions.append("Consultation quality is strong.")

    return suggestions


def job_search_optimizer(skills, gaps):

    plan = []

    if "python" in gaps:
        plan.append("Strengthen Python programming with real projects")

    if "sql" in gaps:
        plan.append("Practice SQL queries and database design")

    if "machine learning" in gaps:
        plan.append("Build ML projects such as recommendation systems")

    if "cloud" in gaps or "aws" in gaps:
        plan.append("Learn cloud deployment using AWS or Azure")

    if "docker" in gaps:
        plan.append("Learn containerization with Docker")

    if len(plan) == 0:
        plan.append("Focus on portfolio projects and job applications")

    return plan


# ----------------------------------------
# UI Input
# ----------------------------------------

transcript = st.text_area(
    "Paste HR Consultation Transcript",
    height=250
)

# ----------------------------------------
# Run Analysis
# ----------------------------------------

if st.button("Run AI Agent Analysis"):

    if transcript.strip() == "":
        st.warning("Please paste a transcript.")
    else:

        # Agents execution
        skills = skill_extraction_agent(transcript)

        metrics = conversation_analysis_agent(transcript)

        polarity, sentiment_label = sentiment_agent(transcript)

        gaps = career_gap_agent(skills)

        suggestions = coaching_recommendation_agent(metrics)

        plan = job_search_optimizer(skills, gaps)

        overall_score = round(
            (metrics["clarity"]*0.35 +
             metrics["engagement"]*0.30 +
             metrics["guidance"]*0.35),2
        )

        st.success("AI Agent Analysis Completed")

        # ----------------------------------------
        # Score Dashboard
        # ----------------------------------------

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Clarity Score", metrics["clarity"])
        col2.metric("Engagement Score", metrics["engagement"])
        col3.metric("Guidance Depth", metrics["guidance"])
        col4.metric("Overall AI Score", overall_score)

        # ----------------------------------------
        # Conversation Statistics
        # ----------------------------------------

        st.subheader("Conversation Statistics")

        stats = pd.DataFrame({
            "Metric":[
                "Total Words",
                "Questions Asked",
                "Advice Statements"
            ],
            "Value":[
                metrics["words"],
                metrics["questions"],
                metrics["advice"]
            ]
        })

        st.table(stats)

        # ----------------------------------------
        # Skills
        # ----------------------------------------

        st.subheader("Detected Skills")

        if skills:
            for s in skills:
                st.write("•", s)
        else:
            st.write("No skills detected.")

        # ----------------------------------------
        # Skill Gap Analysis
        # ----------------------------------------

        st.subheader("Career Skill Gap Analysis")

        if gaps:
            for g in gaps:
                st.write("• Missing:", g)
        else:
            st.write("No major skill gaps detected.")

        # ----------------------------------------
        # Sentiment
        # ----------------------------------------

        st.subheader("Conversation Sentiment")

        if sentiment_label == "Positive":
            st.success("Positive tone detected")
        elif sentiment_label == "Negative":
            st.error("Negative tone detected")
        else:
            st.info("Neutral tone detected")

        # ----------------------------------------
        # Suggestions
        # ----------------------------------------

        st.subheader("AI Coaching Suggestions")

        for s in suggestions:
            st.write("•", s)

        # ----------------------------------------
        # Job Search Optimization Plan
        # ----------------------------------------

        st.subheader("JSO Career Optimization Plan")

        for step in plan:
            st.write("•", step)

        # ----------------------------------------
        # Chart
        # ----------------------------------------

        st.subheader("Consultation Performance")

        chart_data = pd.DataFrame({
            "Metric":[
                "Clarity",
                "Engagement",
                "Guidance"
            ],
            "Score":[
                metrics["clarity"],
                metrics["engagement"],
                metrics["guidance"]
            ]
        })

        st.bar_chart(chart_data.set_index("Metric"))

        # ----------------------------------------
        # AI Reasoning
        # ----------------------------------------

        st.subheader("AI Reasoning Explanation")

        reasoning = f"""
The Agentic Career Intelligence System analyzed the consultation transcript.

Total words analyzed: {metrics['words']}
Questions detected: {metrics['questions']}
Advisory statements detected: {metrics['advice']}

Detected technical skills: {", ".join(skills) if skills else "None"}.

The system evaluated consultation clarity, engagement, and guidance depth.
Skill gaps were identified based on common industry skill requirements.

Based on these signals, the system generated career coaching recommendations
and a Job Search Optimization (JSO) action plan for the candidate.
"""

        st.write(reasoning)