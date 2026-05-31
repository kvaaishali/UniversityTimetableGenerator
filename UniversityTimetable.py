# =========================================================
# UNIVERSITY TIMETABLE GENERATOR USING CSP CONCEPT
# =========================================================

# Subjects
subjects = ["CSP", "AI", "ML", "DS", "CN"]

# Days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Time Slots
slots = ["9AM-10AM", "10AM-11AM", "11AM-12PM"]

# Faculty Assignment
faculty = {
    "CSP": "Dr.Smith",
    "AI": "Dr.John",
    "ML": "Dr.Ravi",
    "DS": "Dr.Kiran",
    "CN": "Dr.Anu"
}

# Classroom Assignment
rooms = ["Room101", "Room102", "Lab201"]

# Empty timetable
timetable = []

# Used slots tracking
used_slots = []

# Function to check clash
def is_slot_available(day, slot):
    if (day, slot) in used_slots:
        return False
    return True

# Generate timetable
room_index = 0

for i in range(len(subjects)):

    assigned = False

    for day in days:

        for slot in slots:

            if is_slot_available(day, slot):

                # Mark slot as used
                used_slots.append((day, slot))

                # Assign room
                room = rooms[room_index % len(rooms)]

                # Store timetable entry
                entry = {
                    "Subject": subjects[i],
                    "Faculty": faculty[subjects[i]],
                    "Day": day,
                    "Time": slot,
                    "Room": room
                }

                timetable.append(entry)

                room_index += 1
                assigned = True
                break

        if assigned:
            break

# =========================================================
# DISPLAY TIMETABLE
# =========================================================

print("\n")
print("=" * 65)
print("         UNIVERSITY TIMETABLE GENERATOR")
print("=" * 65)

print("\nSubject\tFaculty\t\tDay\t\tTime\t\tRoom")
print("-" * 65)

for item in timetable:

    print(
        f"{item['Subject']}\t"
        f"{item['Faculty']}\t"
        f"{item['Day']}\t"
        f"{item['Time']}\t"
        f"{item['Room']}"
    )

print("\n")
print("=" * 65)
print(" Timetable Generated Successfully ")
print("=" * 65)

# =========================================================
# SEARCH FUNCTION
# =========================================================

print("\nSearch Subject Timetable")

search = input("Enter subject name: ")

found = False

for item in timetable:

    if item["Subject"].lower() == search.lower():

        print("\nSubject Found")
        print("-----------------------------")
        print("Subject :", item["Subject"])
        print("Faculty :", item["Faculty"])
        print("Day     :", item["Day"])
        print("Time    :", item["Time"])
        print("Room    :", item["Room"])

        found = True

if not found:
    print("Subject not found")

# =========================================================
# END OF PROGRAM
# =========================================================