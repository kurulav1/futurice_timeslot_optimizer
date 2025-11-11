from typing import Dict, List, Set, Tuple
from collections import defaultdict

'''
Algorithm to compute optimal meeting slots based on participant preferences.
'''
def compute_optimal_slots(meeting_name: str, participants: List[Dict]) -> Tuple[int, List[Dict]]:
    slot_participant_map: Dict[str, Set[str]] = defaultdict(set)

    # build a mapping from slots to participants who prefer them
    for participant in participants:
        name = participant["name"]
        seen = set()
        for slot in participant.get("preferredSlots", []):
            if slot in seen:
                continue
            seen.add(slot)
            slot_participant_map[slot].add(name)

    # if no slots are available, return empty results
    if not slot_participant_map:
        return 0, []
    
    # determine the maximum number of participants for any slot
    max_participants = 0
    for names in slot_participant_map.values():
        length = len(names)
        if length > max_participants:
            max_participants = length

    # Only consider slots with more than one participant
    if max_participants <= 1:
        return 0, []

    # collect all slots that have the maximum number of participants
    optimal_slots = []
    for slot, names in slot_participant_map.items():
        if len(names) == max_participants:
            optimal_slots.append({
                "slot": slot,
                "participants": sorted(list(names))
            })
    
    # sort the optimal slots by slot time for consistent output
    optimal_slots.sort(key=lambda x: x["slot"])
    return max_participants, optimal_slots