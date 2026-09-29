import streamlit as st

from agent import analyze_incident, save_resolved_incident


st.set_page_config(
    page_title="IncidentIQ",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 IncidentIQ")
st.subheader("Memory-Powered AI Incident Response Agent")

st.write(
    "IncidentIQ helps engineers investigate incidents using "
    "persistent organizational memory from Hindsight."
)

st.divider()

st.header("🚨 Current Incident")

service = st.text_input(
    "Service",
    value="Payment API"
)

error = st.text_input(
    "Error",
    value="HTTP 500"
)

deployment = st.text_input(
    "Deployment Version",
    value="v2.4.1"
)

logs = st.text_area(
    "Logs",
    value="Database connection pool exhausted.",
    height=150
)


if st.button("🔍 Analyze Incident", type="primary"):

    incident = {
        "service": service,
        "error": error,
        "deployment": deployment,
        "logs": logs
    }

    with st.spinner("🧠 Searching memory and analyzing incident..."):

        result = analyze_incident(incident)

    st.session_state["result"] = result
    st.session_state["incident"] = incident


if "result" in st.session_state:

    result = st.session_state["result"]
    incident = st.session_state["incident"]

    st.success("Incident analyzed!")

    st.divider()

    st.header("🤖 AI Incident Analysis")

    st.markdown(result["recommendation"])

    st.divider()

    st.header("🧠 Relevant Organizational Memory")

    memories = result["memories"]

    if memories:

        st.success(
            f"Found {len(memories)} relevant memories in Hindsight."
        )

        for i, memory in enumerate(memories, start=1):

            with st.expander(f"Memory {i}", expanded=True):

                text = getattr(memory, "text", str(memory))

                st.write(text)

    else:

        st.info(
            "No similar incidents were found in organizational memory."
        )

    st.divider()

    st.header("✅ Resolve & Remember")

    root_cause = st.text_area(
        "Confirmed Root Cause",
        placeholder="What actually caused the incident?"
    )

    resolution = st.text_area(
        "Resolution",
        placeholder="What action resolved the incident?"
    )

    outcome = st.text_input(
        "Outcome",
        value="Successfully resolved"
    )

    if st.button("💾 Save Resolution to Hindsight"):

        resolved_incident = {
            **incident,
            "root_cause": root_cause,
            "resolution": resolution,
            "outcome": outcome
        }

        with st.spinner("💾 Saving incident memory..."):

            save_resolved_incident(resolved_incident)

        st.success(
            "✅ Resolution saved to Hindsight! "
            "IncidentIQ will be able to use this experience in future incidents."
        )