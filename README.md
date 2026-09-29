# 🧠 IncidentIQ

## Memory-Powered AI Incident Response Agent

IncidentIQ helps engineers investigate production incidents using AI and persistent organizational memory.

Instead of treating every incident as a completely new problem, IncidentIQ retrieves relevant experiences from previous incidents using Hindsight and gives that context to an AI incident-response agent.

---

## 🚨 The Problem

Production incidents are often repetitive.

Teams may have already solved a similar problem, but the knowledge can be scattered across incident tickets, logs, runbooks, chats, and engineers' memory.

IncidentIQ helps engineers reuse that previous experience when a similar incident happens again.

---

## 💡 How It Works

```text
Current Incident
       ↓
Hindsight Recall
       ↓
Relevant Historical Incidents
       ↓
AI Incident Analysis
       ↓
Root Cause + Recommended Action
       ↓
Engineer Resolves Incident
       ↓
Resolution Stored in Hindsight
       ↓
Future Incidents Can Reuse This Experience
```
### Recall

When a new incident is submitted, IncidentIQ searches Hindsight for relevant previous incidents.

```python
memories = recall_incidents(query)
```

The retrieved memories are provided to the AI as historical context.

### Retain

After an engineer confirms the root cause and resolution, IncidentIQ stores the resolved incident in Hindsight.

```python
save_resolved_incident(resolved_incident)
```

This creates a continuous learning loop:

```text
Incident → Recall → AI Assistance → Resolution → Retain
```