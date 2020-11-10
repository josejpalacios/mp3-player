# Import python libraries
from pygame import mixer
from tkinter import filedialog
from pathlib import Path
import tkinter as tk


# Class to create mp3 player object
class MP3Player:
    def __init__(self, window):
        # Instance variable to store music and determine if music is playing
        self.music = None
        self.playing = False

        # Set title of window
        window.title("MP3 Player")

        # Set up window
        window.geometry("300x200")

        # Button for searching music
        search_music = tk.Button(text="Search", command=self.search_music)
        # Pack search_music to window
        search_music.pack()

        # ==============================
        # Frame for music player buttons
        # ==============================

        # Create frame for buttons
        button_frame = tk.Frame(window)
        button_frame.pack()

        # Label for playing music
        play_label = tk.Label(button_frame, text='\u25b6')
        # Bind play_button to play_music
        play_label.bind("<Button>", self.play_music)
        # Pack play_label to window
        play_label.pack(side="left")

        # Label for pausing music
        pause_label = tk.Label(button_frame, text='\u23f8')
        # Bind pause_label to pause_music
        pause_label.bind("<Button>", self.pause_music)
        # Pack pause_label to window
        pause_label.pack(side="left")

        # Label for stopping music
        stop_label = tk.Label(button_frame, text='\u23f9')
        # Bind stop_label to stop_music
        stop_label.bind("<Button>", self.stop_music)
        # Pack stop_label to window
        stop_label.pack(side="left")

        # ================================
        # Frame for displaying information
        # ================================

        # Label for regular text
        text_label = tk.Label(window, text="Selected Song")
        # Pack text_label to window
        text_label.pack()

        # Create a string variable to update text on window
        self.music_name = tk.StringVar()
        # Set default text to None
        self.music_name.set("None")
        # Label for song name
        music_label = tk.Label(window, textvariable=self.music_name)
        # Pack music_label to window
        music_label.pack()

    def search_music(self):
        """
        Function to search for mp3 file.
        :return:
        """
        # Search for mp3 file path
        self.music = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        # Get name of mp3 file
        music_file_name = Path(self.music).stem
        # Set name of mp3 file
        self.music_name.set(music_file_name)

    def play_music(self, event):
        """
        Function to play mp3 file.
        """
        # If mp3 has been selected
        if self.music:
            # Initialize mixer
            mixer.init()
            # Load mp3 file to mixer
            mixer.music.load(self.music)
            # Play mp3 file
            mixer.music.play()

    def pause_music(self, event):
        """
        Function to pause and unpause music
        """
        # If music is playing
        if self.playing:
            # Pause music
            mixer.music.pause()
            # Set playing to false
            self.playing = False
        else:
            # Else unpause music
            mixer.music.unpause()
            # Set playing to true
            self.playing = True

    def stop_music(self, event):
        """
        Function to stop music
        """
        # Stop music
        mixer.music.stop()
        # Set playing to false
        self.playing = False


# Create tkinter window
root = tk.Tk()
# Create MP3Player object
app = MP3Player(root)
# Run root
root.mainloop()
