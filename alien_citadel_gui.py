import random
import threading
import time
import tkinter as tk

class AlienThread:
    """Represents a thread as a moving, animated circle on the canvas."""
    def __init__(self, canvas, thread_id, x, y):
        self.canvas = canvas
        self.thread_id = thread_id
        self.depth = random.randint(3, 7)
        self.x = x
        self.y = y
        self.color = "green"
        self.circle = self.canvas.create_oval(
            self.x, self.y, self.x + 30, self.y + 30, fill=self.color
        )
        self.text = self.canvas.create_text(
            self.x + 15, self.y + 15, text=f"ID {self.thread_id}", fill="black"
        )
        self.run_thread()

    def update_visuals(self, status):
        """Update the visual appearance of the thread node."""
        if status == "running":
            self.color = "yellow"
        elif status == "safeguard":
            self.color = "red"
        elif status == "complete":
            self.color = "gray"
        self.canvas.itemconfig(self.circle, fill=self.color)

    def run_thread(self):
        """Simulate a thread running recursively and moving randomly on the canvas."""
        if self.depth <= 0:
            self.update_visuals("complete")
            return

        self.update_visuals("running")

        # Randomly move the thread's visual
        dx, dy = random.randint(-20, 20), random.randint(-20, 20)
        self.x += dx
        self.y += dy
        self.canvas.move(self.circle, dx, dy)
        self.canvas.move(self.text, dx, dy)

        self.depth -= 1

        if random.choice([True, False]):
            # Recursive call within the same thread
            self.canvas.after(500, self.run_thread)
        else:
            # Create a new thread and start it
            new_x = self.x + random.randint(-50, 50)
            new_y = self.y + random.randint(-50, 50)
            new_thread_id = self.thread_id + 1
            new_thread = AlienThread(self.canvas, new_thread_id, new_x, new_y)

class AlienCitadelGUI:
    """Main GUI application that creates and controls the Alien Citadel."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Graphic-Intensive Alien Citadel")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.threads = []
        self.start_threads()

    def start_threads(self):
        """Start the initial thread that begins the chaos."""
        initial_thread = AlienThread(self.canvas, thread_id=1, x=400, y=300)
        self.threads.append(initial_thread)

    def run(self):
        """Start the Tkinter main loop to display the GUI."""
        self.root.mainloop()


# Run the graphic-intensive Alien Citadel
if __name__ == "__main__":
    app = AlienCitadelGUI()
    app.run()
