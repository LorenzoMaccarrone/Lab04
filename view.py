import flet as ft
'''------------------------------------ATTENZIONE------------------------------------
    Quando parliamo di nomi di variabili dobbiamo porre attenzione agli underscore
    Ad esempio: la variabile txtIn voglio che sia visualizzabile, anzi utilizzabile,
    non solo in view ma anche in controller, anche se viene definita solo in view. 
    Nel caso in cui io ponga due underscore prima di txtIn, ovvero __txtIn,
    il controller non riesce a vederla in nessun modo; per il controllore quella
    variabile non esiste nel file view.
    Se invece pongo un solo underscore, ovvero _txtIn, il controllore riesce a visualizzare 
    tale varibile ed ad utilizzarla.
    Fare sempre molta attenzione: le variabili che devono essere utilizzate in più file non
    devono avere mai più di un underscore, altrimenti i file dove tale variabile non è definta 
    non riescono ad utilizzarla
    ----------------------------------------------------------------------------------'''


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        #row 1
        self.__dd = ft.Dropdown(
            label="Language",
            options=[
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Spanish"),
            ],
        )
        row1=ft.Row([self.__dd], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row1)
        #row2
        self.__dd1 = ft.Dropdown(
            label="Mode", width=100,
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Lineare"),
                ft.dropdown.Option("Dicotomica"),
            ],
        )

        self._txtIn=ft.TextField(label="Insert your Text here")
        self.__btn=ft.ElevatedButton(text="start",on_click=self.__controller.iniziaRicerca)
        row2 = ft.Row([self.__dd1, self._txtIn, self.__btn], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row2)

        #row3
        self.lvOut= ft.ListView()
        row3=ft.Row([self.lvOut])
        self.page.controls.append(row3)
        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
