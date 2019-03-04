import Tkinter as tk
import time

def parse_float_point(string):
  pieces = string.split(",")
  if len(pieces) != 2:
    return None
  x = float(pieces[0])
  y = float(pieces[1])
  return [x, y]

class Line:
  def __init__(self, canvas, p1, p2):
    self.canvas = canvas
    self.id = canvas.create_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), arrow=tk.LAST)

class Circle:
  def __init__(self, canvas, p1, radius):
    self.canvas = canvas
    self.radius = radius
    self.id = canvas.create_oval(int(p1[0] - radius), int(p1[1] - radius),
                                 int(p1[0] + radius), int(p1[1] + radius))

tk_root = tk.Tk()
canvas = tk.Canvas(tk_root, width=200, height=100)
canvas.pack()

while True:
  try:
    args = raw_input("Enter command: ").split()
    command = args[0]
    if command == "":
      continue
    if command == "line":
      if len(args) < 3:
        print("Not enough args. Usage:  line  a,b  c,d  ")
        continue
      point1 = parse_float_point(args[1])
      point2 = parse_float_point(args[2])
      # TODO REMOVE THESE
      point1 = [20, 30]
      point2 = [150, 50]
      if not point1 or not point2:
        print("Could not parse points for line")
        continue
      print("OK rendering line: " + str(point1) + " " + str(point2))
      line = Line(canvas, point1, point2)
    if command == "circle":
      if len(args) < 3:
        print("Not enough args. Usage:  circle  a,b  int_radius")
        continue
      point1 = parse_float_point(args[1])
      radius = int(args[2])
      # TODO REMOVE THESE
      point1 = [40, 90]
      radius = 5
      if not point1:
        print("Could not parse points for circle")
        continue
      print("OK rendering circle: " + str(point1))
      circle = Circle(canvas, point1, radius)
    if command == "sleep":
      if len(args) < 2:
        print("Not enough args. Usage:  sleep  time  ")
        continue
      t = float(args[1])
      print("OK sleeping for: " + str(t) + " seconds")
      time.sleep(t)
    if command == "clear":
      print("OK clearing canvas")
      canvas.delete("all")

    tk_root.update_idletasks()
    tk_root.update()
    time.sleep(0.01)

  except EOFError:
    print("\nGot EOF, exiting")
    exit()
