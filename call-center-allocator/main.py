calls = []

for i in range(17):
    calls.append(i)

staff = ["anna", "ben", "cherry"]
staff_count = len(staff)
early_staff = 2
early_calls = calls[:5]

early_allocation = {}
for employee in staff[:early_staff]:
    position = staff.index(employee)
    early_allocation[employee] = early_calls[position::early_staff]

print(early_allocation)

late_calls = calls[5:]
late_staff = staff[::-1]
late_allocation = {}
    