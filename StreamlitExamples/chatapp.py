from datetime import datetime
import os, glob, random
import streamlit as st
from datetime import datetime
import urllib.request as url
import json

# Chat App
greetIntent = ["hi","hello","hii","hey","hello there","hi there"]
dateIntent = ["what's the date","tell me date","date","date please"]
timeIntent = ["what's the time","tell me time","time","time please"]
musicIntent = ["play song", "song", "start song"]
newsIntent = ["news","tell me news","what's the news"]

st.title("Chat Application...")
st.write("Simple Chatbot using Python")

form = st.form(key="chat_form")
msg = form.text_input(label="Enter your message : ")

submitBtn = form.form_submit_button(label="Send")

if submitBtn:
    st.write("You have clicked...")
    msg = msg.lower()

    if msg in greetIntent:
        st.write("Hello User")
    elif msg in dateIntent:
        d = datetime.now().date()
        st.write(d.strftime("%d %B, %Y, %A"))
    elif msg in timeIntent:
        t = datetime.now().time()
        st.write(t.strftime("%I:%M:%S,%p"))
    elif msg in musicIntent:
        path = r"D:\Batches\Songs\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        song = random.choice(songs)
        os.startfile(song)
    elif msg in newsIntent:
        path = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=695e07af402f4b119f0703e9b19f4683"
        response = url.urlopen(path)

        data = json.load(response)
        articles = data["articles"]
        for i in range(len(articles)):
            st.write(articles[i]["title"])
            st.write("*" * 50)
    elif msg == "bye":
        chat = False
    else:
        st.write("I don't understand")
