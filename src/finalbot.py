import customtkinter as ctk
import tkinter as tk
from tkinter import Toplevel
import datetime
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RoboController:

    def __init__(self, root):
        self.root = root
        self.root.title("RoboController Realistic Navigation")
        self.root.geometry("1200x820")
        self.root.protocol("WM_DELETE_WINDOW", self.safe_close)

        # Robot State
        self.robot_name = ""
        self.total_distance = 0
        self.travelled = 0
        self.initialized = False

        # Logging
        self.logs = []
        self.log_count = 0

        # Movement
        self.animating = False
        self.move_step = 2
        self.move_delay = 35

        # Obstacle control
        self.obstacle_active = False
        self.direction_changed = False

        # Lanes
        self.lanes = {
            "left": 180,
            "center": 250,
            "right": 320
        }
        self.current_lane = "center"

        self.build_ui()

    # ---------------- SAFE CLOSE ----------------
    def safe_close(self):
        self.animating = False
        self.root.destroy()

    # ---------------- UI ----------------
    def build_ui(self):

        title = ctk.CTkLabel(self.root,
                             text="REALISTIC ROBO NAVIGATION SYSTEM",
                             font=("Segoe UI", 28, "bold"))
        title.pack(pady=15)

        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(pady=10)

        self.name_entry = ctk.CTkEntry(input_frame, width=220,
                                       placeholder_text="Robot Name")
        self.name_entry.grid(row=0, column=0, padx=10)

        self.distance_entry = ctk.CTkEntry(input_frame, width=220,
                                           placeholder_text="Target Distance")
        self.distance_entry.grid(row=0, column=1, padx=10)

        ctk.CTkButton(input_frame,
                      text="Initialize",
                      width=130,
                      command=self.initialize_robot,
                      fg_color="#22c55e").grid(row=0, column=2, padx=10)

        # Canvas
        self.canvas = tk.Canvas(self.root,
                                width=1050,
                                height=420,
                                bg="#0f172a",
                                highlightthickness=0)
        self.canvas.pack(pady=15)

        self.canvas.create_rectangle(100, 120, 950, 380,
                                     fill="#1f2937", outline="")

        self.canvas.create_line(100, 120, 100, 380,
                                fill="white", width=4)
        self.canvas.create_line(950, 120, 950, 380,
                                fill="white", width=4)

        self.canvas.create_line(100, 200, 950, 200,
                                fill="white", dash=(10, 8), width=2)
        self.canvas.create_line(100, 290, 950, 290,
                                fill="white", dash=(10, 8), width=2)

        # Robot
        self.robot = self.canvas.create_oval(
            140,
            self.lanes["center"],
            200,
            self.lanes["center"] + 50,
            fill="#00e5ff"
        )

        # Obstacle
        self.obstacle = self.canvas.create_rectangle(
            0, 0, 0, 0,
            fill="#f97316",
            state="hidden"
        )

        # Human
        self.human_parts = []

        # Status
        self.status_label = ctk.CTkLabel(self.root,
                                         text="Status: Ready",
                                         font=("Segoe UI", 18, "bold"))
        self.status_label.pack(pady=8)

        # Distance Bar
        self.distance_bar = ctk.CTkProgressBar(self.root, width=900)
        self.distance_bar.pack(pady=4)

        self.distance_label = ctk.CTkLabel(self.root,
                                           text="Distance: 0m / 0m (0%)")
        self.distance_label.pack()

        # Buttons
        btn_frame = ctk.CTkFrame(self.root)
        btn_frame.pack(pady=15)

        buttons = [
            ("Move", self.move_forward),
            ("Obstacle", self.spawn_obstacle),
            ("Human", self.spawn_human),
            ("Log", self.show_log),
        ]

        for i, (text, cmd) in enumerate(buttons):
            ctk.CTkButton(btn_frame,
                          text=text,
                          width=120,
                          command=cmd).grid(row=0, column=i, padx=10)

    # ---------------- LOG FORMAT ----------------
    def log_event(self, event):
        self.log_count += 1
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        entry = (
            f"\nEvent #{self.log_count}\n"
            f"Time      : {timestamp}\n"
            f"Robot     : {self.robot_name}\n"
            f"Action    : {event}\n"
            f"Lane      : {self.current_lane.upper()}\n"
            f"Distance  : {round(self.travelled,1)} m\n"
            f"{'-'*35}"
        )

        self.logs.append(entry)

    # ---------------- INITIALIZE ----------------
    def initialize_robot(self):
        try:
            self.robot_name = self.name_entry.get()
            self.total_distance = float(self.distance_entry.get())
            self.travelled = 0
            self.initialized = True
            self.obstacle_active = False
            self.direction_changed = False
            self.logs.clear()
            self.log_count = 0

            self.canvas.coords(self.robot,
                               140,
                               self.lanes["center"],
                               200,
                               self.lanes["center"] + 50)

            self.status_label.configure(text="Robot Ready")
            self.log_event("System Initialized")
            self.update_ui()

        except:
            self.status_label.configure(text="Enter valid inputs")

    # ---------------- OBSTACLE ----------------
    def spawn_obstacle(self):
        if not self.initialized:
            return

        obstacle_x = 450

        self.canvas.coords(self.obstacle,
                           obstacle_x,
                           self.lanes["center"] + 10,
                           obstacle_x + 40,
                           self.lanes["center"] + 50)

        self.canvas.itemconfig(self.obstacle, state="normal")

        self.obstacle_active = True
        self.direction_changed = False

        self.log_event("Obstacle Detected")

    # ---------------- HUMAN ----------------
    def spawn_human(self):
        if not self.initialized:
            return

        base_x = 750
        base_y = self.lanes["center"] - 20

        for part in self.human_parts:
            self.canvas.delete(part)
        self.human_parts.clear()

        head = self.canvas.create_oval(base_x, base_y,
                                       base_x + 25, base_y + 25,
                                       fill="white")

        body = self.canvas.create_line(base_x + 12, base_y + 25,
                                       base_x + 12, base_y + 70,
                                       fill="white", width=3)

        arms = self.canvas.create_line(base_x - 10, base_y + 45,
                                       base_x + 35, base_y + 45,
                                       fill="white", width=3)

        leg1 = self.canvas.create_line(base_x + 12, base_y + 70,
                                       base_x - 5, base_y + 100,
                                       fill="white", width=3)

        leg2 = self.canvas.create_line(base_x + 12, base_y + 70,
                                       base_x + 30, base_y + 100,
                                       fill="white", width=3)

        self.human_parts = [head, body, arms, leg1, leg2]

        self.log_event("Human Detected")

    # ---------------- MOVE ----------------
    def move_forward(self):
        if not self.initialized or self.animating:
            return

        self.animating = True
        self.animate_step()

    def animate_step(self):

        rx1, ry1, rx2, ry2 = self.canvas.coords(self.robot)

        # Human collision
        if self.human_parts:
            hx1, hy1, hx2, hy2 = self.canvas.bbox(self.human_parts[0])
            if rx2 >= hx1:
                self.status_label.configure(text="Stopped: Human Ahead")
                self.log_event("Stopped due to Human")
                self.animating = False
                return

        # Obstacle avoidance
        if self.obstacle_active and not self.direction_changed:
            ox1, oy1, ox2, oy2 = self.canvas.coords(self.obstacle)

            if rx2 >= ox1 - 40:
                new_lane = random.choice(["left", "right"])
                self.change_lane(new_lane)
                self.direction_changed = True
                self.log_event(f"Auto Changed Lane → {new_lane.upper()}")

        if rx2 >= 950:
            self.animating = False
            self.status_label.configure(text="Target Reached")
            self.log_event("Target Reached")
            return

        self.canvas.move(self.robot, self.move_step, 0)
        self.travelled += 0.2

        self.update_ui()
        self.root.after(self.move_delay, self.animate_step)

    # ---------------- CHANGE LANE ----------------
    def change_lane(self, lane):
        self.current_lane = lane
        rx1, ry1, rx2, ry2 = self.canvas.coords(self.robot)
        new_y = self.lanes[lane]
        self.canvas.coords(self.robot, rx1, new_y, rx2, new_y + 50)

    # ---------------- SHOW LOG ----------------
    def show_log(self):
        log_window = Toplevel(self.root)
        log_window.title("Mission Log")
        log_window.geometry("600x500")

        textbox = ctk.CTkTextbox(log_window, width=550, height=450)
        textbox.pack(padx=20, pady=20)

        for entry in self.logs:
            textbox.insert("end", entry)

        textbox.configure(state="disabled")

    # ---------------- UPDATE UI ----------------
    def update_ui(self):
        percent = (self.travelled / self.total_distance) if self.total_distance > 0 else 0
        self.distance_bar.set(percent)

        self.distance_label.configure(
            text=f"Distance: {round(self.travelled,1)}m / {self.total_distance}m ({round(percent*100)}%)"
        )


if __name__ == "__main__":
    root = ctk.CTk()
    app = RoboController(root)
    root.mainloop()
