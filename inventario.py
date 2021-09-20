producto = {
  'nombre': '',
  'cantidad': 0.0
  }
inventario = []

inventario.append({'nombre':'papa', 'cantidad': .50})
inventario.append({'nombre':'zanahoria', 'cantidad': .42})
inventario.append({'nombre':'carnes', 'cantidad': .34})
inventario.append({'nombre':'libras de arroz', 'cantidad': .61})
inventario.append({'nombre':'yuca', 'cantidad': .30})
inventario.append({'nombre':'limon', 'cantidad': .87})
inventario.append({'nombre':'libras de frijol', 'cantidad': .54})

print(inventario)

for p in inventario:
  print('_________________')
  print('\t Nombre:', p['nombre'])
  print('\t Precio', p['precio'])

buscar = input('Introduce el producto')
for p in inventario:
  if buscar == p['nombre']:
    print('_________________')
    print('\t Nombre:', p['nombre'])
    print('\t Precio', p['precio'])