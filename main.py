import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")
        
        mixer.init()
        
        self.playlist = []
        self.current_song_index = 0
        self.paused = False
        
        self.add_widgets()

    def add_widgets(self):
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)
        
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)
        
        self.load_button = tk.Button(self.root, text="Load Folder", command=self.load_folder)
        self.load_button.pack(pady=10)
        
    def load_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.playlist = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected) if f.endswith(('.mp3', '.wav'))]
            self.current_song_index = 0
            if self.playlist:
                self.play_music()

    def play_music(self):
        if self.playlist:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
            else:
                mixer.music.load(self.playlist[self.current_song_index])
                mixer.music.play()
                mixer.music.set_endevent(pygame.USEREVENT)
                self.root.bind("<NextSong>", self.play_next_song)

    def stop_music(self):
        mixer.music.stop()

    def pause_music(self):
        if not self.paused:
            mixer.music.pause()
            self.paused = True
        else:
            mixer.music.unpause()
            self.paused = False

    def play_next_song(self, event=None):
        self.current_song_index += 1
        if self.current_song_index < len(self.playlist):
            self.play_music()
        else:
            self.current_song_index = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
