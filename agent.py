import os

from dotenv import load_dotenv
from groq import Groq

from memory import recall_incidents, retain_incident


load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_incident(incident):
    """Analyze an incident using Hindsight memories + Groq AI."""

    query = f"""
    Service: {incident['service']}
    Error: {incident['error']}
    Deployment: {incident['deployment']}
    Logs: {incident['logs']}
    """

    memories = recall_incidents(query)

    memory_text = "\n".join(
        getattr(memory, "text", str(memory))
        for memory in memories
    )

    prompt = f"""
You are an expert Site Reliability Engineer helping investigate
a production incident.

CURRENT INCIDENT:
Service: {incident['service']}
Error: {incident['error']}
Deployment: {incident['deployment']}
Logs: {incident['logs']}

RELEVANT HISTORICAL INCIDENT MEMORY:
{memory_text if memory_text else "No relevant historical incidents found."}

Based on the current incident and the historical organizational
memory, provide:

1. Likely Root Cause
2. Recommended Immediate Action
3. Why This Recommendation
4. Confidence

Keep the response concise and practical for an engineer.
Do not invent historical incidents that are not present in memory.
"""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a production incident response assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    recommendation = response.choices[0].message.content

    return {
        "incident": incident,
        "memories": memories,
        "recommendation": recommendation
    }


def save_resolved_incident(incident):
    """Save a resolved incident to Hindsight."""
    return retain_incident(incident)