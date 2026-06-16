# =====================================================
# UNIVERSITY TIMETABLE GENERATOR USING AI CONCEPTS
# =====================================================

from dataclasses import dataclass
from collections import deque

# =====================================================
# STATE REPRESENTATION
# =====================================================

@dataclass
class ClassState:
    subject: str
    faculty: str
    day: str
    time: str
    room: str

# =====================================================
# SEARCH CONCEPT (BFS)
# =====================================================

campus_map = {
    "MainBlock": ["Room101", "Room102"],
    "Room101": ["Lab201"],
    "Room102": [],
    "Lab201": []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)

            for neighbor in campus_map[node]:
                queue.append(neighbor)

    return visited

# Execute internally
bfs("MainBlock")

# =====================================================
# TIMETABLE DATA
# =====================================================

subjects = [
    "CFAI",
    "FEDF",
    "MDSA",
    "GLB",
    "CFAI",
    "MDSA"
]

faculty = {
    "CFAI": "Prof. Lakshmi",
    "FEDF": "Prof. Srinivas",
    "MDSA": "Prof. Ramesh",
    "GLB": "Prof. Anitha"
}

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

slots = [
    "9AM-10AM",
    "10AM-11AM",
    "11AM-12PM",
    "9AM-10AM",
    "10AM-11AM",
    "11AM-12PM"
]

rooms = [
    "Room101",
    "Room102",
    "Lab201"
]

# =====================================================
# CSP CONSTRAINT CHECKING
# =====================================================

used_slots = []
timetable = []

def is_slot_available(day, slot):
    return (day, slot) not in used_slots

for i in range(len(subjects)):

    if is_slot_available(days[i], slots[i]):

        used_slots.append((days[i], slots[i]))

        timetable.append(
            ClassState(
                subjects[i],
                faculty[subjects[i]],
                days[i],
                slots[i],
                rooms[i % len(rooms)]
            )
        )

# =====================================================
# DECISION MAKING
# =====================================================

scores = [85, 92, 88]
best_score = max(scores)

# =====================================================
# BAYESIAN REASONING
# =====================================================

def bayes(pa, pbgivena, pb):
    return (pa * pbgivena) / pb

attendance_probability = bayes(0.7, 0.8, 0.75)

# =====================================================
# HYBRID INTEGRATION
# =====================================================

hybrid_score = best_score * attendance_probability

# =====================================================
# DISPLAY TIMETABLE
# =====================================================

print("\nUNIVERSITY TIMETABLE GENERATOR")
print("-" * 50)

for item in timetable:
    print(
        f"{item.subject} -> "
        f"{item.day} -> "
        f"{item.time}"
    )

print("\nTimetable Generated Successfully")

# =====================================================
# SUBJECT SEARCH
# =====================================================

search = input("\nEnter Subject Name: ")

found = False

print("\nSubject Details")
print("-" * 40)

for item in timetable:

    if item.subject.lower() == search.lower():

        print("Subject :", item.subject)
        print("Faculty :", item.faculty)
        print("Day     :", item.day)
        print("Time    :", item.time)
        print("Room    :", item.room)
        print("-" * 40)

        found = True

if not found:
    print("Subject Not Found")

print("\nUniversity Timetable Management Completed")=========================
