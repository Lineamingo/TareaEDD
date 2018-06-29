class Node:
  def __init__(self, nombre, apellido, num, email):
    self.num = num
    self.left = None
    self.right = None
    self.parent = None
    self.nombre = nombre
    self.apellido = apellido
    self.num = num
    self.email=email

  def set_num(self,num):
    self.num = num
  def get_num(self):
    return self.num    
  def set_left(self,left):
    self.left=left
  def get_left(self):
    return self.left
  def set_right(self,right):
    self.right = right
  def get_right(self):
    return self.right
  def get_nom(self):
    return self.nombre
  def get_ap(self):
    return self.apellido
  def get_email(self):
    return self.apellido
    
class Tree:
  def __init__(self):
    self.root = None
    self.count = int(0)
    self.aux = None

  def set_root(self,root):
    self.root = root
    
  def get_root(self):
    return self.root

  def verificar(self):
    if self.root==None:
      print("Usted no tiene contactos.")
      print("------------------------------")
      return
    else:
      self.verificar_t(self.root)
    print("Usted tiene:", self.count,"contactos")
    self.count=int=(0)
    print("------------------------------")
    return

  def verificar_t(self, node):
    if node is not None:
      self.count=self.count+1
      if node.left is not None and node.right is not None:
        self.verificar_t(node.left)
        self.verificar_t(node.right)
      if node.left is None:
        self.verificar_t(node.right)
      elif node.right is None:
        self.verificar_t(node.left)
    else:
      return  

#verificar

  def agregar(self, nombre, apellido, num, email):
    node = Node(nombre, apellido, num, email)
    if self.root == None:
      self.root = node
    else:
      self.insertar(self.root,node)
    
  def insertar(self,root,node):
    if node.get_num() < root.get_num():
      if root.get_right() != None:
        self.insertar(root.get_right(),node)
      else:
        node.parent=root
        root.set_right(node)
    elif node.get_num() > root.get_num():
      if root.get_left() != None:
        self.insertar(root.get_left(),node)
      else:
        node.parent=root
        root.set_left(node)

#agregar

  def imprimir(self):
    if self.root == None:
      print("No existen contactos aun")
    else:
      self.show_t(self.root)
    print("------------------------------")
      
  def show_t(self,node):
    if node != None:
      print("Nombre:",node.nombre, node.apellido," numero:", node.num," email:",node.email)
      print("")
      self.show_t(node.left)
      self.show_t(node.right)
        
#imprimir

  def find(self,num):
    if self.root == None:
      print("No existe el contacto.")
      print("------------------------------")
      return None
    else:
      self.findintree(self.root,num)
      return
    
  def findintree(self,node,num):
    if node.num == num:
      print("Nombre:", node.nombre, node.apellido,"numero:", node.num,"email: ", node.email)
      print("------------------------------")
      self.aux=node
    if num > node.num and node.left !=None:
      self.findintree(node.left,num)   
    if num < node.num and node.right != None:
      self.findintree(node.right,num)

#buscar, con numero
  def borrar(self,num):
    self.find(num)
    if(self.aux is not None and self.aux!=self.root):
      self.delete(self.aux)
      print("----------------------------")
      return
    elif(self.aux==self.root):
      if (self.aux.left is not None and self.aux.right is not None):
        if (self.aux.left.left is not None and self.aux.left.right is not None and self.aux.right.left is None and self.aux.right.right is None):
          self.root.left.right.parent=self.root.right
          self.root.left.right.parent.left=self.root.left.right
          self.root.right.left=self.root.left.right
          self.root.left.right=None
          self.root.right.parent=self.root.left
          self.root.right.parent.right=self.root.right
          self.root.left.right=self.root.right
          self.root=self.root.left
          return
        elif (self.aux.right.right is not None and  self.aux.right.left is not None and self.aux.left.left is None and self.aux.left.right is None):
          self.root.right.left.parent=self.root.left
          self.root.right.left.parent.right=self.root.right.left
          self.root.left.right=self.root.right.left
          self.root.right.left=None
          self.root.left.parent=self.root.right
          self.root.left.parent.left=self.root.left
          self.root.right.left=self.root.left
          self.root=self.root.right
          return
        elif self.aux.right.right is not None and self.aux.right.left is not None and self.aux.left.left is not None and self.aux.left.right is not None:
          self.root.left.right.parent=self.root.right.left
          self.root.left.right.parent.left=self.root.left.right
          self.root.right.left.left=self.root.left.right
          self.root.left.right=None
          self.root.right.parent=self.root.left
          self.root.right.parent.right=self.root.right
          self.root.left.right=self.root.right
          self.root=self.root.left
          return  
        else:
          self.root.right.parent=self.root.left
          self.root.right.parent.right=self.root.right
          self.root.left.right=self.root.right
          self.root=self.root.left
          return
      elif self.aux.right is None and self.aux.left is None:
        self.root=None
        return
      elif self.aux.right is None:
        self.root=self.root.left
        self.root.left=None
        return
      elif self.aux.left is None:
        self.root=self.root.right
        self.root.right=None
    else:  
      print("No existe el contacto")
      return

  def delete(self,node):
    if (node.left is not None and node.right is not None):
      if (node.left.left is not None and node.left.right is not None and node.right.left is None and node.right.right is None):
        node.left.parent=node.parent
        node.parent.left=node.left
        node.left.right.parent=node.right
        node.left.right.parent.left=node.left.right
        node.right.left=node.left.right
        node.left.right=None
        node.right.parent=node.left
        node.right.parent.right=node.right
        node.left.right=node.right
        node=None
        return
      elif (node.right.right is not None and node.right.left is not None and node.left.left is None and node.left.right is None):
        node.right.parent=node.parent
        node.parent.right=node.right
        node.right.left.parent=node.left
        node.right.left.parent.right=node.right.left
        node.left.right=node.right.left
        node.right.left=None
        node.left.parent=node.right
        node.left.parent.left=node.left
        node.right.left=node.left
        return
      elif node.right.right is not None and node.right.left is not None and node.left.left is not None and node.left.right is not None:
        node.left.parent=node.parent
        node.parent.left=node.left
        node.left.right.parent=node.right.left
        node.left.right.parent.left=node.left.right
        node.right.left.left=node.left.right
        node.left.right=None
        node.right.parent=node.left
        node.right.parent.right=node.right
        node.left.right=node.right
        node=None
        return  
      else:
        node.left.parent=node.parent
        node.parent.left=node.left
        node.right.parent=node.left
        node.left.right=node.right
        node=None
        return
    elif node.right is None and node.left is None:
      if node.parent.right is None:
        node.parent.left=None
        node=None
        return
      else:
        node.parent.right=None
        node=None
        return
    elif node.right is None:
      node.left.parent=node.parent
      node.parent.left=node.left
      node=None
      return
    elif node.left is None:
      node.right.parent=node.parent
      node.parent.right=node.right
      node=None

#borrar

b1 = Tree()
