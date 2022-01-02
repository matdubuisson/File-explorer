import tkinter as tk

class Menu_Button:
  def __init__(self, window=None, label="?", width=100, height=100, x=0, y=0, elements=[]):
    if window == None:
      raise ValueError("The object of type Meny_Button needs to a valid tkinter window in parameter !!")

    # Primary :
    self.label = label
    self.width = width
    self.height = height
    self.x = x
    self.y = y

    # Secundary :
    self.__is_open = False
    self.principal_button = tk.Button(window, text=label, command=self.__open)
    self.length = len(elements)
    self.elements = []
    i = 0
    while i < self.length:
      self.elements.append(tk.Button(window, text="test"))#str(each[0]), command=each[1]))
      i += 1

  def __str__(self):
    return "Menu_Button : label:{0}, width:{1}, height:{2}".format(self.label, self.width, self.height)

  def draw(self):
    self.principal_button.place(x=self.x, y=self.y, width=self.width, height=self.height)

  def __open(self):
    if self.__is_open:
      for each in self.elements:
        each.config(state=tk.DISABLED)
        each.place(x=0, y=0, width=0, height=0)
    else:
      x = self.x
      y = self.y + self.height
      for each in self.elements:
        each.config(state=tk.NORMAL)
        each.place(x=x, y=y, width=self.width, height=self.height)
        y += self.height

    self.__is_open = not self.__is_open

if __name__ == "__main__":
  test = tk.Tk()
  test.title("Test widgtes !!")
  test.geometry("400x400+100+100")

  def f0():
    print("f0")
  def f1():
    print("f1")

  m = Menu_Button(test, "yolo", 100, 40, 10, 10, [["f0", f0], ["f1", f1]])
  m.draw()

  test.mainloop()
