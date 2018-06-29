class Node: 
  def __init__(self, nombre, apellido, num, email):
    self.num=num
    self.nombre=nombre
    self.apellido=apellido
    self.email=email
    self.next=None
  def getnum(self):
    return self.num
  def getnombre(self):
    return self.nombre
  def getap(self):
    return self.apellido
  def getemail(self):
    return self.email

class Hashi:
  def __init__(self, size):
    self.list=[None]*size
    self.size=size

  def str2num(self, word):
    return(sum(ord(c) for c in word)-96)
  def hash_id(self, apellido):
    return abs(int(self.str2num(apellido)/10))
  
  def agregar_ordenado(self, nombre, apellido, numero, email):
    node = Node(nombre,apellido,numero,email)
    pos=self.hash_id(apellido)
    #print(pos)
    if self.list[pos] is None:
      self.list[pos]=node
      return

    while self.list[pos] is not None:
      if (self.list[pos].nombre==nombre and self.list[pos].apellido==apellido):
        self.list[pos]=node
        return
      else:
        pos=pos+1
    self.list[pos]=node
    return    
    
  
  def buscar(self, apellido):
    print("Buscando contacto...")
    print("")
    pos=self.hash_id(apellido)
    if self.list[pos] is None:
      print("No existe el contacto")
      return     
    while self.list[pos] is not None:
      if (self.list[pos].apellido==apellido):
        print("numero: ", self.list[pos].num, " email: ", self.list[pos].email)
        return
      pos=pos+1  
    print("No existe el contacto")
    return  

  def borrar(self, nombre, apellido):
    print("Eliminando a:", nombre, apellido)
    print("")
    pos=self.hash_id(apellido)
    if self.list[pos] is None:
      print("No existe el contacto")
      return     
    while self.list[pos] is not None:
      if (self.list[pos].nombre==nombre and self.list[pos].apellido==apellido):
        self.list[pos]=None
        print("Borrado.")
        print("-------------")
        return
      pos=pos+1 
    print("No existe el contacto")
    print("")
    return 

  def imprimir(self):
    aux=0
    while aux<400:
      if(self.list[aux] is None):
        aux=aux+1
      else:
        print(self.list[aux].nombre, self.list[aux].apellido,  ", numero: ", self.list[aux].num, ", email: ",self.list[aux].email)
        print("")
        aux=aux+1
    print("----------")
    return      

a = int(400)
b1 = Hashi(a)
