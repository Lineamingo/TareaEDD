import Lista
import ABB
import Hash


while True:
  print("Bienvenido al Administrador de contactos, para comenzar, presione 1, para salir presione 0")
  opcion = input()
  if opcion !=0 and opcion !=1:
    print("Opcion invalida, porfavor, ingrese nuevamente.")
  else:
    if opcion==0:
      break
    elif opcion==1:
      print("Porfavor, elija una de las opciones ofrecidas a continuacion: ")
      print("Para una Lista, escriba -lista-")
      print("Para un Arbol Binario de Busqueda (ABB), escriba -abb-")
      print("Para Hashing, escriba -hash-")
      Edd = raw_input() #quitar el raw_ si no funciona
      print(Edd)
      if (Edd !="-lista-" and Edd !="-abb-" and Edd !="-hash-"):
        print("Opcion invalida, porfavor, ingrese nuevamente.")
      elif Edd=="-lista-":
        while True:
          print("Si desea agregar un contacto, escriba -agregar-")
          print("Si desea buscar un contacto, escriba -buscar-")
          print("Si desea eliminar un contacto, escriba -eliminar-")
          print("Si desea ver su lista de contactos, escriba -listado-")
          metodo = raw_input() #quitar el raw_ si no funciona
          if metodo != "-agregar-" and metodo != "-buscar-" and metodo !="-eliminar-" and metodo !="-listado-":
            print("Opcion invalida, porfavor, ingrese nuevamente.")
            break
          else:
            if metodo=="-agregar-":
              print("porfavor ingrese el nombre del contacto: ")
              nombre = raw_input() #quitar el raw_ si no funciona
              print("porfavor ingrese el apellido del contacto: ")
              apellido = raw_input() #quitar el raw_ si no funciona
              print("porfavor ingrese el numero del contacto: ")
              numero = input()
              print("porfavor ingrese el email del contacto: ")
              email = raw_input() #quitar el raw_ si no funciona
              Lista.b1.agregar_ordenado(nombre,apellido,numero,email)
            elif metodo=="-buscar-":
              print("porfavor ingrese el nombre del contacto: ")
              nombre = raw_input() #quitar el raw_ si no funciona
              print("porfavor ingrese el apellido del contacto: ")
              apellido = raw_input() #quitar el raw_ si no funciona
              Lista.b1.buscar(nombre,apellido)
            elif metodo=="-eliminar-":
              print("porfavor ingrese el nombre del contacto: ")
              nombre = raw_input() #quitar el raw_ si no funciona
              print("porfavor ingrese el apellido del contacto: ")
              apellido = raw_input() #quitar el raw_ si no funciona
              Lista.b1.borrar(nombre,apellido)
            elif metodo=="-listado-":
              Lista.b1.imprimir()
              
            break  
              
      elif Edd=="-abb-":
         
         while True:
          print("Si desea agregar un contacto, escriba -agregar-")
          print("Si desea buscar un contacto, escriba -buscar-")
          print("Si desea eliminar un contacto, escriba -eliminar-")
          print("Si desea ver su lista de contactos, escriba -listado-")
          metodo = raw_input()
          if metodo != "-agregar-" and metodo != "-buscar-" and metodo !="-eliminar-" and metodo !="-listado-":
            print("Opcion invalida, porfavor, ingrese nuevamente.")
            break

          else:
            if metodo=="-agregar-":
              print("porfavor ingrese el nombre del contacto: ")
              nombre = raw_input() #quitar el raw_ si no funciona
              print("porfavor ingrese el apellido del contacto: ")
              apellido = raw_input() #quitar el raw_ si no funciona
              print("porfavor ingrese el numero del contacto: ")
              numero = input()
              print("porfavor ingrese el email del contacto: ")
              email = raw_input() #quitar el raw_ si no funciona
              ABB.b1.agregar(nombre,apellido,numero,email)
            elif metodo=="-buscar-":
              print("porfavor ingrese el numero del contacto: ")
              numero = input()
              ABB.b1.find(numero)
            elif metodo=="-eliminar-":
              print("porfavor ingrese el numero del contacto: ")
              numero = input()
              ABB.b1.borrar(numero)
            elif metodo=="-listado-":
              ABB.b1.imprimir()

            break
              
