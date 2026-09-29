import asyncio
from hindsight_client import Hindsight

HINDSIGHT_URL = "http://localhost:8888"
BANK_ID = "incidentiq"


async def _retain_incident(incident):
    client = Hindsight(base_url=HINDSIGHT_URL)

    try:
        content = f"""
Incident ID: {incident.get('id', 'unknown')}

Service: {incident['service']}
Error: {incident['error']}
Deployment: {incident['deployment']}

Logs:
{incident['logs']}

Root Cause:
{incident.get('root_cause', 'Not provided')}

Resolution:
{incident.get('resolution', 'Not provided')}

Outcome:
{incident.get('outcome', 'Not provided')}
"""

        result = await client.aretain(
            bank_id=BANK_ID,
            content=content,
            retain_async=True
        )

        return result

    finally:
        await client.aclose()


def retain_incident(incident):
    """Store an incident in Hindsight."""
    return asyncio.run(_retain_incident(incident))


async def _recall_incidents(query):
    client = Hindsight(base_url=HINDSIGHT_URL)

    try:
        result = await client.arecall(
            bank_id=BANK_ID,
            query=query
        )

        return result.results

    finally:
        await client.aclose()


def recall_incidents(query):
    """Retrieve relevant previous incidents from Hindsight."""
    return asyncio.run(_recall_incidents(query))