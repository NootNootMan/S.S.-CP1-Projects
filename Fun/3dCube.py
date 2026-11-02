import math
import tkinter as tk




class Wireframe3DApp:


  def __init__(self, root):
    self.root = root
    self.root.title("3D Tkinter Space")


    self.width = 800
    self.height = 600
    self.canvas = tk.Canvas(
        root, width=self.width, height=self.height, bg="black"
    )
    self.canvas.pack()


    # Camera position and angles
    self.cam_x = 0
    self.cam_y = 0
    self.cam_z = -50
    self.angle_x = 0
    self.angle_y = 0


    # Define a 3D cube (like a supply drop / building block)
    self.vertices = [
        [-10, -10, -10],
        [10, -10, -10],
        [10, 10, -10],
        [-10, 10, -10],
        [-10, -10, 10],
        [10, -10, 10],
        [10, 10, 10],
        [-10, 10, 10],
    ]


    self.edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),  # Back face
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),  # Front face
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),  # Connecting edges
    ]


    # Bind keys for movement
    self.root.bind("<Key>", self.handle_key)


    # Start the loop
    self.animate()


  def handle_key(self, event):
    speed = 5
    rot_speed = 0.1
    if event.keysym == "w":
      self.cam_z += speed
    elif event.keysym == "s":
      self.cam_z -= speed
    elif event.keysym == "a":
      self.cam_x -= speed
    elif event.keysym == "d":
      self.cam_x += speed
    elif event.keysym == "Left":
      self.angle_y -= rot_speed
    elif event.keysym == "Right":
      self.angle_y += rot_speed
    elif event.keysym == "Up":
      self.angle_x += rot_speed
    elif event.keysym == "Down":
      self.angle_x -= rot_speed


  def project(self, x, y, z):
    # Rotate around Y axis
    cos_y = math.cos(self.angle_y)
    sin_y = math.sin(self.angle_y)
    x1 = x * cos_y - z * sin_y
    z1 = z * cos_y + x * sin_y


    # Rotate around X axis
    cos_x = math.cos(self.angle_x)
    sin_x = math.sin(self.angle_x)
    y2 = y * cos_x - z1 * sin_x
    z2 = z1 * cos_x + y * sin_x


    # Translate camera
    tz = z2 - self.cam_z
    if tz <= 0:
      tz = 0.01  # Prevent division by zero


    fov = 400
    px = (x1 - self.cam_x) * (fov / tz) + self.width / 2
    py = (y2 - self.cam_y) * (fov / tz) + self.height / 2
    return px, py


  def animate(self):
    self.canvas.delete("all")


    # Project and draw edges
    projected_vertices = []
    for vertex in self.vertices:
      px, py = self.project(vertex[0], vertex[1], vertex[2])
      projected_vertices.append((px, py))


    for edge in self.edges:
      p1 = projected_vertices[edge[0]]
      p2 = projected_vertices[edge[1]]
      self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="cyan", width=2)


    # Crosshair in the middle (like Fortnite aiming)
    self.canvas.create_line(
        self.width / 2 - 10,
        self.height / 2,
        self.width / 2 + 10,
        self.height / 2,
        fill="white",
    )
    self.canvas.create_line(
        self.width / 2,
        self.height / 2 - 10,
        self.width / 2,
        self.height / 2 + 10,
        fill="white",
    )


    self.root.after(30, self.animate)




root = tk.Tk()
app = Wireframe3DApp(root)
root.mainloop()
