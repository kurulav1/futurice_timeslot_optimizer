import json
from app.compute import compute_optimal_slots

def test_compute_optimal_single_slot():
    meeting_name = "Team Sync"
    participants = [
        {"name": "Alice", "preferredSlots": ["2024-07-01T10:00", "2024-07-01T11:00"]},
        {"name": "Bob", "preferredSlots": ["2024-07-01T10:00"]},
        {"name": "Charlie", "preferredSlots": ["2024-07-01T12:00"]},
    ]
    max_participants, optimal_slots = compute_optimal_slots(meeting_name, participants)
    assert max_participants == 2
    assert len(optimal_slots) == 1
    assert optimal_slots[0]["slot"] == "2024-07-01T10:00"
    assert set(optimal_slots[0]["participants"]) == {"Alice", "Bob"}

def test_compute_optimal_multiple_slots():
    meeting_name = "Project Kickoff"
    participants = [
        {"name": "Mikko", "preferredSlots": ["2024-07-02T09:00", "2024-07-02T10:00"]},
        {"name": "Joonas", "preferredSlots": ["2024-07-02T09:00", "2024-07-02T11:00"]},
        {"name": "Matias", "preferredSlots": ["2024-07-02T10:00", "2024-07-02T11:00"]},
    ]
    max_participants, optimal_slots = compute_optimal_slots(meeting_name, participants)
    assert max_participants == 2
    assert len(optimal_slots) == 3
    slots = {slot["slot"]: set(slot["participants"]) for slot in optimal_slots}
    assert slots["2024-07-02T09:00"] == {"Mikko", "Joonas"}
    assert slots["2024-07-02T10:00"] == {"Mikko", "Matias"}

def test_compute_optimal_large_group():
    meeting_name = "Engineering All Hands"
    participants = [
        {"name": "Mikko",  "preferredSlots": ["2024-07-05T09:00", "2024-07-05T10:00", "2024-07-05T11:00"]},
        {"name": "Jani",   "preferredSlots": ["2024-07-05T10:00", "2024-07-05T11:00", "2024-07-05T13:00"]},
        {"name": "Oskari", "preferredSlots": ["2024-07-05T09:00", "2024-07-05T10:00"]},
        {"name": "Milla",  "preferredSlots": ["2024-07-05T10:00", "2024-07-05T11:00"]},
        {"name": "Anna",   "preferredSlots": ["2024-07-05T10:00", "2024-07-05T13:00"]},
        {"name": "Eetu",   "preferredSlots": ["2024-07-05T08:00", "2024-07-05T10:00"]},
        {"name": "Emilia", "preferredSlots": ["2024-07-05T10:00", "2024-07-05T12:00"]},
        {"name": "Jaakko", "preferredSlots": ["2024-07-05T10:00", "2024-07-05T11:00"]},
        {"name": "Matias", "preferredSlots": ["2024-07-05T11:00", "2024-07-05T13:00"]},
        {"name": "Harri",  "preferredSlots": ["2024-07-05T10:00", "2024-07-05T12:00"]},
    ]

    max_participants, optimal_slots = compute_optimal_slots(meeting_name, participants)

    assert max_participants == 9
    assert len(optimal_slots) == 1
    assert optimal_slots[0]["slot"] == "2024-07-05T10:00"

    expected_names = {"Mikko", "Jani", "Oskari", "Milla", "Anna", "Eetu", "Emilia", "Jaakko", "Harri"}
    assert set(optimal_slots[0]["participants"]) == expected_names


def test_compute_optimal_no_common_slots():
    meeting_name = "No Common Time"
    participants = [
        {"name": "Eve", "preferredSlots": ["2024-07-03T14:00"]},
        {"name": "Frank", "preferredSlots": ["2024-07-03T15:00"]},
    ]
    max_participants, optimal_slots = compute_optimal_slots(meeting_name, participants)
    assert max_participants == 0
    assert optimal_slots == []
