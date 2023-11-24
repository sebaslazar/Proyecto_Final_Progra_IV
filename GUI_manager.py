import os
from PyQt5 import QtWidgets, uic
from GUI import agregar_cliente, menu_principal

app = QtWidgets.QApplication([])

# Carga GUIs
# os.chdir("C:/Users/sebas/PycharmProjects/Proyecto_Final_Progra_IV/GUI/")
gui_paths = "GUI"
main_menu = uic.loadUi(os.path.abspath(os.path.join(gui_paths, "menu_principal.ui")))
add_client = uic.loadUi(os.path.abspath(os.path.join(gui_paths, "agregar_cliente.ui")))
add_product_menu = uic.loadUi(os.path.abspath(os.path.join(gui_paths, "agregar_producto.ui")))
search_client = uic.loadUi(os.path.abspath(os.path.join(gui_paths, "buscar_cliente.ui")))


# Cambio de pantalla
def add_client_screen():
    # add_client.show()
    main_menu.hide()
    agregar_cliente.show_window()


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
    app = menu_principal.show_window()
    app.show()
    # main_menu.show()
    # app.exec()
