import os

# os.listdir() => Get the list of the files and the folders
datas = os.listdir()
datas.sort()

class Explorer:
  def __init__(self, current_address="/"):
    self.current_address = current_address

  def __str__(self):
    return str(self.current_address)

  def __eq__(self, other):
    if type(other) == Explorer:
      return self.current_address == other.current_address
    return False

  ###################################

  def get_address(self):
    return os.path

  def get_datas(self):
    return os.listdir()

  def is_file(self, data_name):
    return os.path.isfile(data_name)

  def get_files(self):
    l = self.get_datas()
    nl = []
    for each in l:
      if self.is_file(each):
        nl.append(each)
    return nl

  def is_directory(self, data_name):
    return os.path.isdir(data_name)

  def get_directories(self):
    l = self.get_datas()
    nl = []
    for each in l:
      if self.is_directory(each):
        nl.append(each)
    return nl

  def is_link(self, data_name):
    return os.path.islink(data_name)

  def get_links(self):
    l = self.get_datas()
    nl = []
    for each in l:
      if self.is_link(each):
        nl.append(each)
    return nl

  def get_size(self, data_name):
    return os.path.getsize(data_name)

  ###################################

  def set_address(self, new_address="/"):
    os.chdir(new_address)

  def __get_new_name(self, potential_new_name="unnamed"):
    nbr = 0
    new_name = potential_new_name
    while os.path.exists(new_name):
      new_name = potential_new_name + str(nbr)
      nbr += 1
    return new_name

  def set_file(self, file_name="unnamed", contain=""):
    file_name = self.__get_new_name(file_name)
    with open(file_name, "w") as f:
      f.write(contain)

  def set_directory(self, directory_name="unnamed"):
    directory_name = self.__get_new_name(directory_name)
    if not os.path.exists(directory_name):
      os.mkdir(directory_name)

##########################################################

if __name__ == "__main__":
  e = Explorer("/home/racteur/")
  print(e.get_datas())
  print(e.get_files())
  print(e.get_directories())

  #e.set_address("/home/racteur/")
  e.set_file()
  e.set_file()
  e.set_directory()
  e.set_directory()
