#!/usr/bin/python3
"""
using the module requests
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    """
    que contiene le header X-Request-Id:
    identificación es generada (aleatoriamente) por el cliente
    no contiene ninguna información sensible y, por lo tanto,
    no debe violar la privacidad del usuario.
    Como se crea una identificación única por solicitud,
    tampoco ayuda con el seguimiento de los usuarios.
    """
    response = requests.get(argv[1])
    print(response.headers["X-Request-Id"])
