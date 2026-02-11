import customtkinter as ctk
from tkinter import Toplevel
import datetime

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RoboController:
    def __init__(self, root):   # ✅ FIXED CONSTRUCTOR
        self.root = root
        self.root.title("RoboController Dashboard")
        self.root.geometry("1000x700")

        # Data
        self.robot_name = "RoboX"
        self.total_distance = 100
        self.travelled = 0
        self.battery = 100
        self.logs = []

        self.build_ui()

    # ---------------- UI ----------------
    def build_ui(self):

        self.main_card = ctk.CTkFrame(
            self.root,
            corner_radius=25,
            fg_color="#1e293b"
        )
        self.main_card.pack(padx=40, pady=40, fill="both", expand=True)

        title = ctk.CTkLabel(
            self.main_card,
            text="ROBOCONTROLLER DASHBOARD",
            font=("Segoe UI", 26, "bold")
        )
        title.pack(pady=20)

        # Robot Name
        self.name_entry = ctk.CTkEntry(
            self.main_card,
            width=250,
            placeholder_text="Enter Robot Name"
        )
        self.name_entry.pack(pady=10)

        # Target Distance
        self.distance_entry = ctk.CTkEntry(
            self.main_card,
            width=250,
            placeholder_text="Enter Target Distance"
        )
        self.distance_entry.pack(pady=10)

        self.init_button = ctk.CTkButton(
            self.main_card,
            text="Initialize Robot",
            command=self.initialize_robot,
            fg_color="#22c55e"
        )
        self.init_button.pack(pady=10)

        # Status
        self.status_label = ctk.CTkLabel(
            self.main_card,
            text="Status: Ready",
            font=("Segoe UI", 18, "bold")
        )
        self.status_label.pack(pady=15)

        # Distance Progress
        self.distance_progress = ctk.CTkProgressBar(
            self.main_card,
            width=700,
            height=20
        )
        self.distance_progress.set(0)
        self.distance_progress.pack(pady=10)

        self.distance_label = ctk.CTkLabel(
            self.main_card,
            text="Distance: 0m / 0m (0%)"
        )
        self.distance_label.pack()

        # Battery Progress
        self.battery_progress = ctk.CTkProgressBar(
            self.main_card,
            width=700,
            height=20
        )
        self.battery_progress.set(1)
        self.battery_progress.pack(pady=10)

        self.battery_label = ctk.CTkLabel(
            self.main_card,
            text="Battery: 100%"
        )
        self.battery_label.pack()

        # Buttons
        btn_frame = ctk.CTkFrame(self.main_card, fg_color="transparent")
        btn_frame.pack(pady=30)

        self.forward_btn = ctk.CTkButton(
            btn_frame,
            text="Move Forward",
            fg_color="#22c55e",
            command=self.move_forward
        )
        self.forward_btn.grid(row=0, column=0, padx=15)

        ctk.CTkButton(
            btn_frame,
            text="Obstacle",
            fg_color="#f97316",
            command=self.obstacle_detected
        ).grid(row=0, column=1, padx=15)

        ctk.CTkButton(
            btn_frame,
            text="Human",
            fg_color="#ef4444",
            command=self.human_detected
        ).grid(row=0, column=2, padx=15)

        ctk.CTkButton(
            btn_frame,
            text="Show Log",
            fg_color="#334155",
            command=self.show_log
        ).grid(row=0, column=3, padx=15)

        # Direction Buttons (hidden)
        self.left_button = ctk.CTkButton(
            self.main_card,
            text="Move Left",
            fg_color="#facc15",
            command=lambda: self.avoid("Left")
        )

        self.right_button = ctk.CTkButton(
            self.main_card,
            text="Move Right",
            fg_color="#facc15",
            command=lambda: self.avoid("Right")
        )

    # ---------------- Logic ----------------

    def initialize_robot(self):
        try:
            name = self.name_entry.get()
            distance = float(self.distance_entry.get())

            if distance <= 0:
                raise ValueError

            self.robot_name = name if name else "RoboX"
            self.total_distance = distance
            self.travelled = 0
            self.battery = 100
            self.logs.clear()

            self.update_ui()
            self.status_label.configure(text=f"{self.robot_name} Initialized")

        except:
            self.status_label.configure(text="Enter valid details")

    def move_forward(self):
        if self.battery <= 0:
            self.status_label.configure(text="Battery Dead")
            self.forward_btn.configure(state="disabled")
            return

        if self.travelled >= self.total_distance:
            self.status_label.configure(text="Target Already Reached")
            return

        self.travelled += 10
        self.battery -= 5

        if self.travelled > self.total_distance:
            self.travelled = self.total_distance

        if self.battery < 0:
            self.battery = 0

        self.add_log("Moved Forward 10m")
        self.update_ui()

    def obstacle_detected(self):
        self.status_label.configure(text="Obstacle Detected! Choose Direction")
        self.left_button.pack(pady=5)
        self.right_button.pack(pady=5)

    def avoid(self, direction):
        self.left_button.pack_forget()
        self.right_button.pack_forget()

        self.travelled += 5
        self.battery -= 5

        if self.travelled > self.total_distance:
            self.travelled = self.total_distance

        if self.battery < 0:
            self.battery = 0

        self.add_log(f"Obstacle Avoided → Moved {direction} 5m")
        self.update_ui()

    def human_detected(self):
        self.status_label.configure(text="🚨 Human Detected! STOPPED")
        self.add_log("Stopped due to Human Detection")

    def update_ui(self):
        percent = (self.travelled / self.total_distance) if self.total_distance else 0

        self.distance_progress.set(percent)
        self.battery_progress.set(self.battery / 100)

        self.distance_label.configure(
            text=f"Distance: {self.travelled}m / {self.total_distance}m ({round(percent * 100)}%)"
        )

        self.battery_label.configure(
            text=f"Battery: {self.battery}%"
        )

        if self.travelled >= self.total_distance:
            self.status_label.configure(text="🎯 Target Reached!")

    def add_log(self, message):
        time_stamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{time_stamp}] {message}")

    def show_log(self):
        log_window = Toplevel(self.root)
        log_window.title("Mission Log")
        log_window.geometry("600x500")

        text_box = ctk.CTkTextbox(
            log_window,
            width=550,
            height=450
        )
        text_box.pack(pady=20, padx=20)

        if self.logs:
            for log in self.logs:
                text_box.insert("end", log + "\n")
        else:
            text_box.insert("end", "No logs available.")

        text_box.configure(state="disabled")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    root = ctk.CTk()
    app = RoboController(root)
    root.mainloop()
