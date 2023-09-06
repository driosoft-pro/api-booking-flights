# Librerias usadas 
    pip install flask
    pip install flask_sqlalchemy


# Los endpoints de la API incluyen:
    1.POST/flights: crea un nuevo vuelo con la información proporcionada en el cuerpo de la solicitud.
    
    2.GET/flights: obtiene una lista de vuelos disponibles según los criterios de búsqueda proporcionados en los parámetros de la URL (origin, destination y departure_date).
    
    3.POST/reservations: crea una nueva reserva de vuelo para el vuelo especificado en el cuerpo de la solicitud.
    
    4.GET/airlines: obtiene una lista de aerolíneas con la cantidad de reservas realizadas.
    
    5.GET/airlines/count: obtiene el número de aerolíneas registradas.

