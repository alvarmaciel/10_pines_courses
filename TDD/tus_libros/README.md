# Inicio.

- Empezar por los modelos
  - Cliente
  - Libro
  - Cart
- Primeros tests
  - TestClientModel (Vale la pena testear la instanciación de este objeto?)
    - test_can_not_repeat_user_id -> verificar que dos o más clientes no tengan el mismo id
  - TestBookModel ()
    - ¿Necesitamos nombres de libro y autor? 
    - test_can_not_be_repeated_isbn_books -> verificar que no haya libros con isbn repetidos
  - TestCartModel
    - test_a -> /createCart verificar match clientId existe
    - test_b -> /createCart verificar match de passwd con clientID
    - test_c -> /createCart verificar creación y tiempo de vida
      - verificar que en el cualquier momento de los 30 minutos el carrito existe con la data correcta
      - verificar que a los 31' el carrito desaparece
    
  
# Primer Iteración

- Pensamos a través de una metáfora -> Supermercado
  - primero, está el carrito vacio
  - segundo, agrego algo al carrito
  - No puedo agregar un producto que no esta en el supermercado
- si lo pienso en BDD:
  - Feature: Add things to a cart
  - Scenario: Create an empty cart and fill it
    - Given a cart
    - when the cart is empty
    - when I add an item
    - then the cart is not empty

# Segunda Iteración
- TODO: Aplicar tarjeta de crédito
  - No permite tarjeta de credito vencida
  - ver fecha de vencimienot con día actual
  - 
