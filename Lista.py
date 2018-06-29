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


class ContactList:
  def __init__(self):
    self.head=None
    self.tail=None
  def verificar(self):
    if self.head==None:
      print("Lista vacia.")
      print("-------------")
    else:
      print("Hay contactos en tu lista.")
      print("-------------")
  def agregar_ordenado(self, nombre, apellido, numero, email):
    node=Node(nombre, apellido, numero, email)
    #primer caso, verificar que esta vacia
    if self.head==None:
      self.head=node
      self.tail=node
      return
    aux=self.head
    if aux.apellido>node.apellido:
      node.next=aux
      self.head=node
      return
    while aux:
      if(aux.next is not None and aux.next.apellido>node.apellido):
        node.next=aux.next
        aux.next=node
        return
      elif(aux.next==None):
        aux.next=node
        return
      aux=aux.next  

  def borrar(self, nombre, apellido):
    if self.head==None:
      print("Lista vacia.")
      print("-------------")
      return
    aux=self.head
    if aux.nombre==nombre and aux.apellido==apellido and self.head.next is not None:
      self.head=self.head.next
      return
    elif aux.nombre==nombre and aux.apellido==apellido and self.head.next is None:
      self.head=None
      return
    while aux:
      if (aux.next is not None and aux.next.next is not None):
        if (aux.next.nombre==nombre and aux.next.apellido==apellido):
          aux.next=aux.next.next
          return
      elif (aux.next is not None and aux.next.next is None):
        if (aux.next.nombre==nombre and aux.next.apellido==apellido):
          aux.next=None
          return
      aux=aux.next
    print("No existe numero con ese nombre.")
    return

  def imprimir(self):
    aux=self.head
    while aux:
      print(aux.nombre, aux.apellido)
      #print(aux.email)
      aux=aux.next
    print("-------------")
    return

  def buscar(self, nombre, apellido):
    print("Buscando contacto....")
    print(" ")
    if self.head is None:
      print("Lista vacia.")
      return
    aux=self.head
    while aux:
      if(aux.nombre==nombre and aux.apellido==apellido):
        print(aux.nombre, aux.apellido, ", numero:", aux.num, ", email:", aux.email)
        print("------------")
        return
      aux=aux.next
    print("No existe el contacto.")
    print("------------")
    return 

b1 = ContactList()
