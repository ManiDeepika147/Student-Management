import streamlit as st

# Initialize session state for students list
if "students" not in st.session_state:
    st.session_state.students = []

# Dummy variable to trigger rerun when toggled
if "refresh" not in st.session_state:
    st.session_state.refresh = False

def add_student(name, roll_no):
    st.session_state.students.append({"name": name, "roll_no": roll_no})
    st.success("Student added!")

def update_student(index, name, roll_no):
    st.session_state.students[index] = {"name": name, "roll_no": roll_no}
    st.success("Student updated!")

def delete_student(index):
    st.session_state.students.pop(index)
    st.success("Student deleted!")

st.title("🎓 Student Management System")

menu = ["Add Student", "View / Update / Delete Students"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.header("Add New Student")
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    if st.button("Add Student"):
        if name and roll_no:
            add_student(name, roll_no)
        else:
            st.error("Please enter both name and roll number.")

elif choice == "View / Update / Delete Students":
    st.header("Student List")
    if len(st.session_state.students) == 0:
        st.info("No students found. Add some first!")
    else:
        for i, student in enumerate(st.session_state.students):
            with st.expander(f"{student['name']} (Roll No: {student['roll_no']})"):
                new_name = st.text_input("Update Name", value=student["name"], key=f"name_{i}")
                new_roll = st.text_input("Update Roll No", value=student["roll_no"], key=f"roll_{i}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Update", key=f"update_{i}"):
                        if new_name and new_roll:
                            update_student(i, new_name, new_roll)
                        else:
                            st.error("Both fields required to update.")
                with col2:
                    if st.button("Delete", key=f"delete_{i}"):
                        delete_student(i)
                        # Toggle dummy variable to force rerun
                        st.session_state.refresh = not st.session_state.refresh
