import os
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

# Carga GUIs
os.chdir("C:/Users/sebas/PycharmProjects/Proyecto_Final_Progra_IV/GUI/")
main_menu = uic.loadUi(os.path.abspath("menu_principal.ui"))
add_client = uic.loadUi(os.path.abspath("agregar_cliente.ui"))
add_product_menu = uic.loadUi(os.path.abspath("agregar_producto.ui"))
search_client = uic.loadUi(os.path.abspath("buscar_cliente.ui"))


# Cambio de pantalla
def add_client_screen():
    add_client.show()
    main_menu.hide()


def add_product_menu_screen():
    add_product_menu.show()
    main_menu.hide()


def search_client_screen():
    search_client.show()
    main_menu.hide()


# Botones
main_menu.buy.clicked.connect(add_client_screen)
main_menu.add_product.clicked.connect(add_product_menu_screen)
main_menu.search_id.clicked.connect(search_client_screen)

if __name__ == "__main__":
    main_menu.show()
    app.exec()
