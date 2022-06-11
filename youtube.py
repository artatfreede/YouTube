from asyncio import streams
from distutils.command.install_egg_info import to_filename
from fileinput import close
from msilib.schema import Icon
from tkinter import W
from turtle import goto, title, update
import os
from typing import Any
import pytube
import base64 
from pytube import YouTube
import PySimpleGUI as sg
with open("d:\dev\icon.png", "rb") as f:
     my_icon = base64.b64encode(f.read())
sg.set_options(icon=my_icon)
os.chdir(r"c:\\")
icon ="d:\dev\icon.png"
directory_path = os.getcwd()

def open_window():
    
    layout = [[sg.Text("Help Menu", key="new")],
              #[sg.Text('1. Select the download directory with the'),sg.Button('Browse'),sg.Text('button.')],
              [sg.Text('1. Press the'), sg.Button('Change Directory'),sg.Text('to change download directory')],
              [sg.Text('2. Press the '),sg.Button('Browse'), sg.Text('to select download directory.')],
              [sg.Text('3. Enter the URL of the YouTube video you want to download')],
              [sg.Text('4. Press the'),sg.Button('Download'), sg.Text('video button to start the download')],
              [sg.Text('5. The software will select the highest quality video and download')],
              [sg.Text('the video into the directory you selected')],
              [sg.Button('Back', key="-BACK-", size=(8,0), border_width=5)]
    ]

    window = sg.Window("Help Menu", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-BACK-":
            window.close()
            
def on_complete(stream, file_path):
    sg.popup('Download Complete')
                
def on_progress(stream, chunk, bytes_remaining):
    print('progress', bytes_remaining)
    # for i in bytes_remaining:
    #     sg.OneLineProgressMeter('Download', i+1, 10000, 'Optional message', 'key')


def download_video():
    (print(values['_KEY1_']))
    
                 
    video_object = YouTube (values['_KEY1_'], 
                        on_complete_callback = on_complete, 
                        on_progress_callback = on_progress)
    video_object.streams.get_highest_resolution().download()
    
sg.theme('darkblue4')
sg.set_options(font = 'Calibri 25')

layout = [
        
    
    [sg.Text('Enter video URL', key = '-IP-')],
    [sg.InputText('', key = '_KEY1_', enable_events=True)],
    #[[sg.Text('Download Folder'), sg.In(size=(25,1), enable_events=True, key ='-FOLDER-'), sg.FolderBrowse(tooltip='Select download folder')]],
    [sg.Text ('Videos will be downloaded to->'), sg.Text(f'{directory_path}', size=(30,1), background_color='#040100',key='-CURRENT-', enable_events=True)],
    [sg.Button('', key = 'Button5', image_filename='c:\\users\\artad\\desktop\\Red-download-button.png', size=(1,0), tooltip='Download video',border_width=3),\
    sg.Button('Change Directory', key= 'CD', tooltip='Change Download Directory', border_width=3), \
    sg.Button('Exit', key ='Button7',size=(10,1), tooltip='Exit the program',border_width=3),\
    sg.Button('Help', key='-help-',size=(10,1), tooltip='Display help window',border_width=3)]
    
]

window = sg.Window('YouTube downloader - written by - Art Adams 2022 Copyright (c) All Rights Reserved',layout, resizable=True)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    if event == 'Button5':
       download_video()
               
    if event == 'Button7' :
        break
    
    if event == 'CD':
        text = sg.popup_get_folder('Browse to select a new download folder')
        #sg.popup(text)
        os.chdir(text)
        window['-CURRENT-'].update(os.getcwd())
    if event == '-help-':
        open_window()

        
                        