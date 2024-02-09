# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:09:37 2024

@author: ADMIN
"""
import pyttsx3
import PyPDF2

with open('C:/Users/ADMIN/Documents/School/theory of estimation notes1.pdf', 'rb') as book:
  reader = PyPDF2.PdfReader(book)
  import pyttsx3
  audio_reader = pyttsx3.init()
  audio_reader.setProperty("rate", 100)

  for page in range(len(reader.pages)):
    next_page = reader.pages[page]
    content = next_page.extract_text()

    audio_reader.say(content)
    
    audio_reader.save_to_file(string, 'speech.mp3')
    audio_reader.runAndWait()
