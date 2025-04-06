import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import os

class RacerLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Racer Launcher")
        
        # Game versions and their executable paths
        self.versions = {
            "Racer 0.9.0 RC10": "game/racer090rc10/racer.exe",
            "Racer 0.9.0 RC4": "game/racer090rc4/racer.exe",
            "Racer 0.89": "game/racer089/racer.exe",
            "Racer 0.6.5 Beta 5": "game/racer0655/racer.exe"
        }
        
        # Load and display banner image
        try:
            self.banner_img = Image.open("assets/racerbn.jpg")
            self.banner_photo = ImageTk.PhotoImage(self.banner_img)
            self.banner_label = tk.Label(root, image=self.banner_photo)
            self.banner_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading banner image: {e}")
            self.banner_label = tk.Label(root, text="Racer Launcher", font=("Arial", 16))
            self.banner_label.pack(pady=10)
        
        # Version selection dropdown
        self.version_var = tk.StringVar(value="Racer 0.9.0 RC10")
        self.version_label = tk.Label(root, text="Select Version:")
        self.version_label.pack(pady=5)
        
        self.version_menu = ttk.Combobox(
            root,
            textvariable=self.version_var,
            values=list(self.versions.keys()),
            state="readonly"
        )
        self.version_menu.pack(pady=5)
        
        # Play button
        self.play_button = tk.Button(
            root,
            text="Play!",
            command=self.launch_game,
            bg="green",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=5
        )
        self.play_button.pack(pady=20)
        
    def launch_game(self):
        selected_version = self.version_var.get()
        exe_path = self.versions.get(selected_version)
        
        if not exe_path:
            tk.messagebox.showerror("Error", "Invalid version selected")
            return
            
        if not os.path.exists(exe_path):
            tk.messagebox.showerror("Error", f"Executable not found at: {exe_path}")
            return
            
        try:
            subprocess.Popen(exe_path)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to launch game: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    launcher = RacerLauncher(root)
    root.mainloop()
