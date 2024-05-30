from tkinter import *
from tkinter import colorchooser

class MathDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Edukasi Matematika")
        self.root.geometry("800x600")

        self.canvas = Canvas(self.root, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)

        self.control_frame = Frame(self.root)
        self.control_frame.pack(side=LEFT, fill=Y)

        self.create_controls()

    def create_controls(self):
        Label(self.control_frame, text="Pilih Objek").pack(pady=10)
        self.shape_var = StringVar(value="garis")
        shapes = ["garis", "lingkaran", "persegi panjang"]
        for shape in shapes:
            Radiobutton(self.control_frame, text=shape.capitalize(), variable=self.shape_var, value=shape).pack(anchor=W)

        Label(self.control_frame, text="Koordinat Titik Awal (x1, y1)").pack(pady=10)
        self.x1_entry = Entry(self.control_frame)
        self.x1_entry.pack()
        self.y1_entry = Entry(self.control_frame)
        self.y1_entry.pack()

        Label(self.control_frame, text="Koordinat Titik Akhir (x2, y2)").pack(pady=10)
        self.x2_entry = Entry(self.control_frame)
        self.x2_entry.pack()
        self.y2_entry = Entry(self.control_frame)
        self.y2_entry.pack()

        Label(self.control_frame, text="Koordinat Titik Pusat (x, y) dan Jari-jari (r)").pack(pady=10)
        self.center_x_entry = Entry(self.control_frame)
        self.center_x_entry.pack()
        self.center_y_entry = Entry(self.control_frame)
        self.center_y_entry.pack()
        self.radius_entry = Entry(self.control_frame)
        self.radius_entry.pack()

        Label(self.control_frame, text="Tebal Garis").pack(pady=10)
        self.line_width_entry = Entry(self.control_frame)
        self.line_width_entry.pack()

        Label(self.control_frame, text="Warna Garis").pack(pady=10)
        self.line_color_button = Button(self.control_frame, text="Pilih Warna", command=self.choose_line_color)
        self.line_color_button.pack()

        Label(self.control_frame, text="Warna Isi").pack(pady=10)
        self.fill_color_button = Button(self.control_frame, text="Pilih Warna", command=self.choose_fill_color)
        self.fill_color_button.pack()

        Button(self.control_frame, text="Gambar Objek", command=self.draw_shape).pack(pady=20)

        self.line_color = "black"
        self.fill_color = ""

    def choose_line_color(self):
        color_code = colorchooser.askcolor(title="Pilih Warna Garis")
        self.line_color = color_code[1]

    def choose_fill_color(self):
        color_code = colorchooser.askcolor(title="Pilih Warna Isi")
        self.fill_color = color_code[1]

    def draw_shape(self):
        shape = self.shape_var.get()

        try:
            x1, y1 = int(self.x1_entry.get()), int(self.y1_entry.get())
            x2, y2 = int(self.x2_entry.get()), int(self.y2_entry.get())
            center_x, center_y = int(self.center_x_entry.get()), int(self.center_y_entry.get())
            radius = int(self.radius_entry.get())
            line_width = int(self.line_width_entry.get())
        except ValueError:
            print("Masukkan nilai numerik yang valid!")
            return

        if shape == "garis":
            self.canvas.create_line(x1, y1, x2, y2, width=line_width, fill=self.line_color)
        elif shape == "persegi panjang":
            self.canvas.create_rectangle(x1, y1, x2, y2, width=line_width, outline=self.line_color, fill=self.fill_color)
        elif shape == "lingkaran":
            self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                                    width=line_width, outline=self.line_color, fill=self.fill_color)

if __name__ == "__main__":
    root = Tk()
    app = MathDrawingApp(root)
    root.mainloop()
