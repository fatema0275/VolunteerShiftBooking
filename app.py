import tkinter as tk
from tkinter import ttk, messagebox

# List to store volunteer assignments
assignments = []

def update_displays():
    # 1. Calculate shift counts in a simple, beginner-friendly way
    morning_count = 0
    afternoon_count = 0
    evening_count = 0
    
    for item in assignments:
        if item["shift"] == "Morning":
            morning_count += 1
        elif item["shift"] == "Afternoon":
            afternoon_count += 1
        elif item["shift"] == "Evening":
            evening_count += 1
    
    # Update the shift counts label
    lbl_counts.config(
        text=f"Morning: {morning_count}   |   Afternoon: {afternoon_count}   |   Evening: {evening_count}"
    )
    
    # 2. Update the list of assigned volunteers
    if not assignments:
        lbl_volunteer_list.config(text="No volunteers assigned yet.")
    else:
        display_lines = []
        for i, item in enumerate(assignments, 1):
            display_lines.append(
                f"{i}. Name: {item['name']}  |  Shift: {item['shift']}  |  Role: {item['role']}"
            )
        lbl_volunteer_list.config(text="\n".join(display_lines))

def assign_volunteer():
    name = entry_name.get().strip()
    shift = combo_shift.get()
    role = combo_role.get()
    
    # Validation 1: Do not allow empty volunteer name
    if not name:
        messagebox.showwarning("Input Error", "Please enter the volunteer's name.")
        return
    
    # Validation 2: Prevent assigning the same volunteer more than once
    for item in assignments:
        if item["name"].lower() == name.lower():
            messagebox.showwarning(
                "Duplicate Volunteer",
                f"Volunteer '{item['name']}' has already been assigned to a shift."
            )
            return
    
    # Store assignment in the Python list
    assignment = {
        "name": name,
        "shift": shift,
        "role": role
    }
    assignments.append(assignment)
    
    # Display success message using messagebox
    messagebox.showinfo(
        "Assignment Successful",
        f"Volunteer: {name}\nShift: {shift}\nRole: {role}\n\nSuccessfully assigned!"
    )
    
    # Clear name entry for next input
    entry_name.delete(0, tk.END)
    
    # Update assignment list and shift counts
    update_displays()

# Create main window
root = tk.Tk()
root.title("Volunteer Shift Allocator")
root.geometry("480x620")
root.resizable(True, True)

# Main container frame with padding
frame = tk.Frame(root, padx=25, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Title Label
title_label = tk.Label(
    frame,
    text="Volunteer Shift Allocator",
    font=("Arial", 16, "bold"),
    pady=5
)
title_label.pack()

# Volunteer Name Field
lbl_name = tk.Label(frame, text="Volunteer Name:", font=("Arial", 10))
lbl_name.pack(anchor="w", pady=(8, 2))

entry_name = tk.Entry(frame, font=("Arial", 11))
entry_name.pack(fill="x", pady=(0, 8))
entry_name.focus()

# Shift Dropdown
lbl_shift = tk.Label(frame, text="Select Shift:", font=("Arial", 10))
lbl_shift.pack(anchor="w", pady=(4, 2))

shifts = ["Morning", "Afternoon", "Evening"]
combo_shift = ttk.Combobox(frame, values=shifts, state="readonly", font=("Arial", 10))
combo_shift.set(shifts[0])
combo_shift.pack(fill="x", pady=(0, 8))

# Role Dropdown
lbl_role = tk.Label(frame, text="Select Role:", font=("Arial", 10))
lbl_role.pack(anchor="w", pady=(4, 2))

roles = [
    "Registration",
    "Food Management",
    "Crowd Management",
    "Technical Support"
]
combo_role = ttk.Combobox(frame, values=roles, state="readonly", font=("Arial", 10))
combo_role.set(roles[0])
combo_role.pack(fill="x", pady=(0, 12))

# Assign Volunteer Button
btn_assign = tk.Button(
    frame,
    text="Assign Volunteer",
    font=("Arial", 11, "bold"),
    bg="#1976d2",
    fg="white",
    activebackground="#1565c0",
    activeforeground="white",
    cursor="hand2",
    pady=6,
    command=assign_volunteer
)
btn_assign.pack(fill="x", pady=(0, 15))

# --- Shift Summary Section ---
lbl_summary_title = tk.Label(
    frame,
    text="Shift Summary (Total Volunteers per Shift):",
    font=("Arial", 10, "bold")
)
lbl_summary_title.pack(anchor="w", pady=(5, 3))

lbl_counts = tk.Label(
    frame,
    text="Morning: 0   |   Afternoon: 0   |   Evening: 0",
    font=("Arial", 10, "bold"),
    fg="#0d47a1",
    bg="#e3f2fd",
    relief="groove",
    bd=1,
    pady=6
)
lbl_counts.pack(fill="x", pady=(0, 15))

# --- Assigned Volunteers Section ---
lbl_list_title = tk.Label(
    frame,
    text="Assigned Volunteers:",
    font=("Arial", 10, "bold")
)
lbl_list_title.pack(anchor="w", pady=(5, 3))

lbl_volunteer_list = tk.Label(
    frame,
    text="No volunteers assigned yet.",
    font=("Arial", 9),
    justify="left",
    anchor="nw",
    bg="#fafafa",
    relief="groove",
    bd=1,
    padx=10,
    pady=8
)
lbl_volunteer_list.pack(fill="both", expand=True, pady=(0, 5))

# Initialize display with default states
update_displays()

if __name__ == "__main__":
    root.mainloop()
