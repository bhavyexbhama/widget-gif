import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

class SunflowerWidget:
    def __init__(self, root, gif_path):
        self.root = root
        
        # 1. Window Configuration
        self.root.overrideredirect(True)  # Remove borders/title bar
        self.root.attributes('-topmost', True) # Keep on top of other windows
        
        # 2. Handle Transparency (Windows specific)
        transparent_color = '#abcdef' 
        self.root.wm_attributes('-transparentcolor', transparent_color)
        self.root.config(bg=transparent_color)

        # 3. Load the GIF
        self.gif_path = gif_path
        self.sequence = []
        try:
            im = Image.open(gif_path)
            # Load all frames
            for frame in ImageSequence.Iterator(im):
                # Convert frame to PhotoImage
                self.sequence.append(ImageTk.PhotoImage(frame.copy()))
        except Exception as e:
            print(f"Error loading GIF: {e}")
            self.root.destroy()
            return

        self.image_label = tk.Label(root, bd=0, bg=transparent_color)
        self.image_label.pack()

        # 4. Position the Widget (Bottom Right Corner)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Adjust these offsets to move the plant
        x_offset = screen_width - 200 
        y_offset = screen_height - 250
        
        self.root.geometry(f"+{x_offset}+{y_offset}")

        # 5. Start Animation
        self.frame_index = 0
        self.animate()
        
        # 6. Add Exit capability (Double click to close)
        self.image_label.bind('<Double-Button-1>', lambda e: self.root.destroy())

    def animate(self):
        # Update the image
        self.image_label.config(image=self.sequence[self.frame_index])
        
        # Advance frame
        self.frame_index = (self.frame_index + 1) % len(self.sequence)
        
        # Schedule next frame (Adjust 100 to speed up/slow down: lower is faster)
        self.root.after(10, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    
    # UPDATED PATH HERE
    # We use r"..." to handle the backslashes correctly
    gif_file = r"C:\Users\HP\Desktop\CODING\projects\gif\sunflower-pvz.gif"
    
    widget = SunflowerWidget(root, gif_file)
    root.mainloop()