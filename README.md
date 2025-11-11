## Time slot optimizer

A simple backend for getting optimal timeslot for a meeting involving multiple participants.

Lanugages & tools used:

Python
    - FastAPI for serving
    - Pydantic for data validation
    - Pytest for testing

AWS for infra & deployment
    - deployed as Lambda function

Terraform for infrastructure

# Endpoints

Check health: 

GET ´/health´

- Should respond ´{"status":"ok"}´

POST ´POST /api/v1/meetings/optimize´

Example body:

´{
  "meetingName": "Design Sync",
  "participants": [
    {
      "name": "Alice",
      "preferredSlots": [
        "2024-06-10T09:00",
        "2024-06-10T10:00",
        "2024-06-10T13:00"
      ]
    },
    {
      "name": "Bob",
      "preferredSlots": [
        "2024-06-10T10:00",
        "2024-06-10T13:00"
      ]
    },
    {
      "name": "Carol",
      "preferredSlots": [
        "2024-06-10T09:00",
        "2024-06-10T10:00"
      ]
    }
  ]
}
´

Response:

´{
  "meetingName": "Design Sync",
  "optimalSlots": [
    {
      "slot": "2024-06-10T10:00",
      "participants": ["Alice", "Bob", "Carol"]
    }
  ],
  "maxParticipants": 3
}
´

# Hosting

Application is deployed at: 

https://cavbl2x1b9.execute-api.eu-north-1.amazonaws.com/