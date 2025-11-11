#!/usr/bin/env bash
set -euo pipefail

BASE_URL=${1:-http://127.0.0.1:8000}

echo "Testing health endpoint..."
curl -s "${BASE_URL}/health" | jq .

echo
echo "Testing single optimal slot case..."
curl -s -X POST "${BASE_URL}/api/v1/meetings/optimize" \
  -H "Content-Type: application/json" \
  -d '{
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
}' | jq .

echo
echo "Testing multiple equal optimal slots case..."
curl -s -X POST "${BASE_URL}/api/v1/meetings/optimize" \
  -H "Content-Type: application/json" \
  -d '{
  "meetingName": "Project Kickoff",
  "participants": [
    {"name": "Mikko", "preferredSlots": ["2024-07-02T09:00", "2024-07-02T10:00"]},
    {"name": "Joonas", "preferredSlots": ["2024-07-02T09:00", "2024-07-02T11:00"]},
    {"name": "Matias", "preferredSlots": ["2024-07-02T10:00", "2024-07-02T11:00"]}
  ]
}' | jq .

echo
echo "Testing no common slots case (expect error)..."
curl -s -w "\nHTTP status: %{http_code}\n" -o >(jq .) -X POST "${BASE_URL}/api/v1/meetings/optimize" \
  -H "Content-Type: application/json" \
  -d '{
  "meetingName": "Impossible Meeting",
  "participants": [
    {"name": "Alice", "preferredSlots": ["2024-06-10T09:00"]},
    {"name": "Bob", "preferredSlots": ["2024-06-10T10:00"]}
  ]
}'
