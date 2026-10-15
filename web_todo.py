import os
import sys
import streamlit as st

# Look one directory level higher than where this file lives
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import it successfully
import backend.helper_funcs as hf

def update_list():
    """
    To make sure every task displays on its own line with its own checkbox,
    you need to ensure each task is saved(appended) with a newline character at the very
    end of its own line in the text file, and that your file reader reads them
    as a list of separate strings.
    """

    # 1. Get the text from input and strip any accidental whitespace around it
    input_field_task=st.session_state["input_list"].strip()

    #2 Strip spaces and prevent blanks
    if input_field_task == "":
        st.warning("Enter a task")
        return # stop processing

    # 3. Fetch the current list of tasks
    todo_list_object=hf.get_todos()

    # 4. Append the new task WITH a newline character at the end
    todo_list_object.append(input_field_task+"\n")

    # 5. Save the updated list back to the file
    hf.write_todo(todo_list_object)

    # 6. Clear the text input box so it's ready for the next task
    st.session_state["input_list"] = ""

task_list_object=hf.get_todos()

st.title("My Todo App")
st.subheader("Task List")
st.write("This app increase productivity")

for index, task in enumerate(task_list_object):
    # Render the valid checkbox with a unique key
    checkbox = st.checkbox(task, key=f"{task}")
    if checkbox:
        task_list_object.pop(index)
        hf.write_todo(task_list_object)
        del st.session_state[task]
        st.rerun() # stops the delay delete, needing to click twice

st.text_input(label="",
              placeholder="Enter your task",
              on_change=update_list,
              key="input_list")

# st.session_state


