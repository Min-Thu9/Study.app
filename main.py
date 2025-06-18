import streamlit as st
import pandas as pd
import datetime,time

tab1, tab2, tab3, tab4, tab5= st.tabs(["📃To Do List","🎥Play Video & Learn", "🎵Listen to Music","Study Timer","Reflection"])

with tab1:
    st.title("To-Do List (CRUD)")   #initialize session state for tasks
    if "tasks" not in st.session_state:
        st.session_state.tasks=pd.DataFrame(columns=["Task","Done"])

    #show editable task list   
    st.subheader("Task List")
    edited_df=st.data_editor(
        st.session_state.tasks,
        num_rows="dynamic",
        use_container_width=True,
        key="task_editor"
    )
    if st.button("Save Changes"):
        st.session_state.tasks=edited_df
        st.success("Tasks updated!")

    if not st.session_state.tasks.empty:
        csv = st.session_state.tasks.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Tasks as CSV",
            data=csv,
            file_name='tasks.csv',
            mime='text/csv'
        )

    if st.button("🗑️Clear All Tasks"):
        st.session_state.tasks=pd.DataFrame(columns=["Task","Done"])
        st.success("All tasks cleared.")

with tab2:
    st.subheader("Watch➡️Learn➡️Note➡️Download Your Note🦾")
    url=st.text_input("Enter url for the video")

    if not url:
        st.warning("You haven't entered any url!")
    else:  
        st.video(	#st.video
            data=url,
            start_time=10,   # start playback at 10 seconds
            end_time=20,     # stop playback at 20 seconds
            autoplay=False,
            loop=True        # loop the 10-20 seconds segment
        )
    st.subheader("📝Note")
    note=st.text_area("Note down here. Remember: you can download your note😊.")
    if note:
        st.write("This is your note:",note)
    # Convert note string to bytes for download
        note_bytes = note.encode('utf-8')

        st.download_button(
            label="📁Download your note as text",
            data=note_bytes,
            file_name="note.txt",
            mime="text/plain"
        )
    st.markdown(body='''
            :red[How confident are] :orange[you] :green[in your learning] :rainbow[progress] :blue-background[so far]?
            ''')

    score = st.slider(
    label="Your Confidence",
    min_value=0,
    max_value=5,
    value=3,
    step=1
            )
    if score <3:
        st.write("What's wrong?")
    else:
        st.write("Good!")

with tab3:
    st.subheader("Tired? Take a break & Listen to whatever on Youtube")
    toggle=st.toggle("Toggle to enter your preferred url!")
    if toggle:
        url_music=st.text_input("Enter url for the video (Youtube Recommended!)")
        if not url_music:
            st.write("Please enter url")
        else:  
            st.video(
                data=url_music,
                start_time=10      
            )

    col1, col2=st.columns(2)
    with col1:
        st.image(
            image="https://images.unsplash.com/photo-1671813203207-8cfe0876a97d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHN0dWR5JTIwd2l0aCUyMG11c2ljfGVufDB8fDB8fHww"
        )
    with col2:
        st.image(
            image="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c3R1ZHl8ZW58MHx8MHx8fDA%3D"
        )
    

with tab4:
    st.title("⏳ Study Timer")

    minutes = st.number_input("Enter duration (minutes)", min_value=1, max_value=60, value=1)
    seconds = int(minutes * 60)

    start = st.button("Start Timer")

    if start:
        countdown = st.empty()
        warning_box = st.empty()

        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            countdown.markdown(f"## ⏰ Time Left: {mins:02d}:{secs:02d}")

            if remaining == 10:
                warning_box.warning("⚠️ Only 10 seconds left! Wrap up soon.")
            elif remaining < 10:
                # Keep the warning visible
                pass
            else:
                # Clear warning before 10s
                warning_box.empty()

            time.sleep(1)

        countdown.markdown("## ✅ Time's up! Take a break 🎉")
        warning_box.empty()

with tab5:
    st.subheader("Reflect Here!")
    time=st.time_input(label="How long did you study?", help="Select a time")
    st.write("Selected time:",time)
    if time < datetime.time(0,15,0):
        st.markdown(body='''
            :red-background[You studied for less than 15 minutes. Is everything okay?]
            ''')
    else:
        st.markdown(body='''
            :green-background[You studied for more then 15 minutes.Keep it up! 👏]
            ''')
        
    thingsLearned = st.text_input(
    label="What do you remember from what you've learned today?"   
    )
    if thingsLearned:
        st.markdown(f''':blue-background You remember: {thingsLearned}''')
