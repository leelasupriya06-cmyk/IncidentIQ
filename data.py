INCIDENTS = [
    {
        "id": "INC-001",
        "service": "Payment API",
        "error": "HTTP 500",
        "deployment": "v2.4.1",
        "logs": "Database connection pool exhausted.",
        "root_cause": "Database connection pool exhaustion",
        "resolution": "Increased the database connection pool and restarted the affected service.",
        "outcome": "Successfully resolved"
    },
    {
        "id": "INC-002",
        "service": "Authentication Service",
        "error": "HTTP 504",
        "deployment": "v1.8.2",
        "logs": "Authentication requests timing out.",
        "root_cause": "Authentication service timeout caused by high request load.",
        "resolution": "Scaled authentication service instances and restarted unhealthy instances.",
        "outcome": "Successfully resolved"
    },
    {
        "id": "INC-003",
        "service": "Payment API",
        "error": "HTTP 503",
        "deployment": "v2.5.0",
        "logs": "Redis connection timeout while processing payment request.",
        "root_cause": "Redis connection timeout.",
        "resolution": "Restarted Redis connection pool and increased connection timeout.",
        "outcome": "Successfully resolved"
    }
]