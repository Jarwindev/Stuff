import tkinter as tk
from tkinter import simpledialog, filedialog, ttk, messagebox
import random
from PIL import Image, ImageDraw
import math

class ColorGridApp:
    def __init__(self, master):
        self.master = master
        self.cell_size = 25  # Default cell size

        # --- Set default font ---
        default_font = ("Segoe UI", 10)
        self.master.option_add("*Font", default_font)

        # --- Theme switcher (must be packed first) ---
        self.theme_frame = ttk.Frame(master)
        self.theme_frame.pack(side=tk.TOP, fill="x", pady=(8, 0))
        ttk.Label(self.theme_frame, text="Theme:").pack(side=tk.LEFT, padx=(10, 2))
        self.theme_var = tk.StringVar(value="light")
        self.available_themes = ["light", "dark"]
        self.theme_combo = ttk.Combobox(self.theme_frame, textvariable=self.theme_var, values=self.available_themes, width=7, state="readonly")
        self.theme_combo.pack(side=tk.LEFT)
        self.theme_combo.bind("<<ComboboxSelected>>", self._on_theme_change)

        # --- Controls at the top ---
        self.top_frame = ttk.Frame(master)
        self.top_frame.pack(side=tk.TOP, fill="x")

        self.control_frame = ttk.Frame(self.top_frame)
        self.control_frame.pack(side=tk.TOP, fill="x", pady=(8, 0))

        # Centered buttons with padding
        self.button_container = ttk.Frame(self.control_frame)
        self.button_container.pack(side=tk.TOP, pady=4)
        ttk.Button(self.button_container, text="Regenerate Colors", command=self.regenerate_colors, style="Custom.TButton").pack(side=tk.LEFT, padx=8)
        ttk.Button(self.button_container, text="Resize Grid", command=self.ask_resize, style="Custom.TButton").pack(side=tk.LEFT, padx=8)
        ttk.Button(self.button_container, text="Cell Size", command=self.ask_cell_size, style="Custom.TButton").pack(side=tk.LEFT, padx=8)
        ttk.Button(self.button_container, text="Save as Image", command=self.save_image, style="Custom.TButton").pack(side=tk.LEFT, padx=8)

        self.root_colors_map = {
            "Red": (255, 0, 0),
            "Light Red": (255, 128, 128),
            "Dark Red": (128, 0, 0),
            "Green": (0, 255, 0),
            "Light Green": (128, 255, 128),
            "Dark Green": (0, 128, 0),
            "Blue": (0, 0, 255),
            "Light Blue": (128, 128, 255),
            "Dark Blue": (0, 0, 128),
            "Black": (0, 0, 0),
            "White": (255, 255, 255),
            "Gray": (128, 128, 128),
        }

        # Root color config UI
        self.palette_frame = ttk.LabelFrame(self.top_frame, text="Color Palette Configuration")
        self.palette_frame.pack(side=tk.TOP, pady=8, fill="x", padx=10)

        self.selected_root = tk.StringVar(value="Red")
        ttk.Label(self.palette_frame, text="Root Color:").pack(side=tk.LEFT, padx=4)
        ttk.Combobox(self.palette_frame, textvariable=self.selected_root, values=list(self.root_colors_map.keys()), width=7, state="readonly").pack(side=tk.LEFT, padx=2)

        self.distance_entry = ttk.Entry(self.palette_frame, width=5)
        self.distance_entry.insert(0, "100")
        self.distance_entry.pack(side=tk.LEFT, padx=4)
        ttk.Label(self.palette_frame, text="Distance").pack(side=tk.LEFT, padx=2)

        ttk.Button(self.palette_frame, text="Add Root", command=self.add_root_color, style="Custom.TButton").pack(side=tk.LEFT, padx=8)

        self.root_color_listbox = tk.Listbox(self.top_frame, height=5, font=default_font)
        self.root_color_listbox.pack(side=tk.TOP, pady=4, fill="both", padx=10)

        self.clear_palette_btn = ttk.Button(self.top_frame, text="Clear Palette", command=self.clear_palette, style="Custom.TButton")
        self.clear_palette_btn.pack(side=tk.TOP, pady=4)

        # --- Scrollable Canvas for the grid ---
        self.canvas_frame = ttk.Frame(master)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", highlightthickness=2, relief="ridge")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.v_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.v_scroll.grid(row=0, column=1, sticky="ns")
        self.h_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.h_scroll.grid(row=1, column=0, sticky="ew")

        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        self.canvas_frame.rowconfigure(0, weight=1)
        self.canvas_frame.columnconfigure(0, weight=1)

        # --- Style and theme setup (must be after canvas is created) ---
        self.style = ttk.Style()
        self._setup_themes()
        self.set_theme("light")

        self.root_color_constraints = []  # list of tuples: (name, rgb, distance)
        self.rows = 0
        self.cols = 0
        self.colors = []

        self.ask_resize(initial=True)

    def _setup_themes(self):
        # Light theme
        self.style.theme_create("light", parent="clam", settings={
            ".": {
                "configure": {
                    "background": "#f4f4f4",
                    "foreground": "#222",
                    "font": ("Segoe UI", 10)
                }
            },
            "TLabelFrame": {"configure": {"background": "#f4f4f4", "foreground": "#222"}},
            "TFrame": {"configure": {"background": "#f4f4f4"}},
            "Custom.TButton": {
                "configure": {
                    "padding": 6,
                    "background": "#e0e0e0",
                    "bordercolor": "#000000",
                    "relief": "solid",
                    "borderwidth": 1,
                    "foreground": "#222"
                },
                "map": {
                    "background": [
                        ("active", "#d0d0d0"),
                        ("!active", "#e0e0e0")
                    ],
                    "bordercolor": [
                        ("active", "#000000"),
                        ("!active", "#000000")
                    ]
                }
            },
            "TEntry": {"configure": {"fieldbackground": "#fff", "foreground": "#222"}},
            "TCombobox": {"configure": {"fieldbackground": "#fff", "foreground": "#222"}},
        })
        # Dark theme
        self.style.theme_create("dark", parent="clam", settings={
            ".": {
                "configure": {
                    "background": "#23272e",
                    "foreground": "#f4f4f4",
                    "font": ("Segoe UI", 10)
                }
            },
            "TLabelFrame": {"configure": {"background": "#23272e", "foreground": "#f4f4f4"}},
            "TFrame": {"configure": {"background": "#23272e"}},
            "Custom.TButton": {
                "configure": {
                    "padding": 6,
                    "background": "#444444",
                    "bordercolor": "#ffffff",
                    "relief": "solid",
                    "borderwidth": 1,
                    "foreground": "#f4f4f4"
                },
                "map": {
                    "background": [
                        ("active", "#666666"),
                        ("!active", "#444444")
                    ],
                    "bordercolor": [
                        ("active", "#ffffff"),
                        ("!active", "#ffffff")
                    ]
                }
            },
            "TEntry": {"configure": {"fieldbackground": "#333", "foreground": "#f4f4f4"}},
            "TCombobox": {"configure": {"fieldbackground": "#333", "foreground": "#f4f4f4"}},
        })
        # Set default style for all buttons to Custom.TButton
        self.style.configure("TButton", relief="solid", borderwidth=1)

    def set_theme(self, theme_name):
        if theme_name in self.available_themes:
            self.style.theme_use(theme_name)
            # Canvas background for dark mode
            if theme_name == "dark":
                self.canvas.configure(bg="#23272e")
            else:
                self.canvas.configure(bg="#ffffff")

    def _on_theme_change(self, event=None):
        self.set_theme(self.theme_var.get())

    def color_distance(self, rgb1, rgb2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))

    def generate_constrained_color(self, root_rgb, max_dist):
        while True:
            rgb = tuple(random.randint(0, 255) for _ in range(3))
            if self.color_distance(rgb, root_rgb) <= max_dist:
                return "#%02x%02x%02x" % rgb

    def generate_colors(self):
        if not self.root_color_constraints:
            tk.messagebox.showwarning("No Root Colors", "Please add at least one root color before trying to generate the grid.")  
            self.colors = []
            return
        
        self.colors = []
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                name, rgb, dist = random.choice(self.root_color_constraints)
                color = self.generate_constrained_color(rgb, dist)
                row.append(color)
            self.colors.append(row)
        print(f"Generated a color grid of size {self.rows}x{self.cols}")

    def draw_grid(self):
        if not self.colors or len(self.colors) != self.rows or len(self.colors[0]) != self.cols:
            return  # Data mismatch, skip drawing
        self.canvas.delete("all")
        width = self.cols * self.cell_size
        height = self.rows * self.cell_size
        self.canvas.config(scrollregion=(0, 0, width, height), width=min(800, width), height=min(600, height))
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.colors[r][c], outline="black")

    def regenerate_colors(self):
        self.generate_colors()
        self.draw_grid()

    def ask_resize(self, initial=False):
        if not initial:
            self.master.withdraw()
        rows = simpledialog.askinteger("Grid Rows", "Enter number of rows:", parent=self.master)
        cols = simpledialog.askinteger("Grid Columns", "Enter number of columns:", parent=self.master)
        if rows and cols and rows > 0 and cols > 0:
            self.rows = rows
            self.cols = cols
            if not initial:
                self.regenerate_colors()
        else:
            if initial:
                self.master.destroy()
            else:
                print("Invalid input. Resize cancelled.")
        self.master.deiconify()

    def ask_cell_size(self):
        size = simpledialog.askinteger("Cell Size", "Enter new cell size in pixels:", initialvalue=self.cell_size)
        if size and size > 0:
            self.cell_size = size
            self.draw_grid()

    def add_root_color(self):
        name = self.selected_root.get()
        if name not in self.root_colors_map:
            return
        try:
            distance = int(self.distance_entry.get())
            if not (0 <= distance <= 441):
                raise ValueError
        except ValueError:
            print("Invalid distance")
            return
        rgb = self.root_colors_map[name]
        self.root_color_constraints.append((name, rgb, distance))
        self.root_color_listbox.insert(tk.END, f"{name} (Distance {distance})")

    def clear_palette(self):
        self.root_color_constraints = []
        self.root_color_listbox.delete(0, tk.END)
        self.regenerate_colors()

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img = Image.new("RGB", (self.cols * self.cell_size, self.rows * self.cell_size), "white")
            draw = ImageDraw.Draw(img)
            for r in range(self.rows):
                for c in range(self.cols):
                    x1 = c * self.cell_size
                    y1 = r * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    draw.rectangle([x1, y1, x2, y2], fill=self.colors[r][c], outline="black")
            img.save(file_path)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Random Color Grid with Multi-Root Palettes")
    app = ColorGridApp(root)
    root.mainloop()

#Programmet genererar ett rutnät av fyrkantiga celler av slumpmässig färg enligt vissa regler.
