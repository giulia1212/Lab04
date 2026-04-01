import flet as ft

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
        self.ddLanguage = None      # menù a tendina lingua
        self.ddModality = None      # modalità di ricerca
        self._txtSentence = None    # frase
        self._btnSpellCheck = None  # bottone
        self._lvOut = None          # list view

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
        # ROW1
        # menù a tendina per scegliere la lingua
        self.ddLanguage = ft.Dropdown(label="Select language",
                                options=[ft.dropdown.Option("italian"),
                                         ft.dropdown.Option("english"),
                                         ft.dropdown.Option("spanish")],
                                width=1200,
                                on_change=lambda e: self.__controller.handleLanguageSelection(e.control.value))

        row1 = ft.Row([self.ddLanguage])

        #ROW2
        # modalità di ricerca
        self.ddModality = ft.Dropdown(label="Search Modality",
                                      options=[ft.dropdown.Option("Default"),
                                               ft.dropdown.Option("Linear"),
                                               ft.dropdown.Option("Dichotomic")],
                                      width=300,
                                      on_change=lambda e: self.__controller.handleModalitySelection(e.control.value))

        self._txtSentence = ft.TextField(label="Add your sentence here", width=700)
        self._btnSpellCheck = ft.ElevatedButton(text="Spell Check",
                                                    on_click= lambda e: self.__controller.handleSpellCheck(
                                                        self._txtSentence.value,
                                                        self.ddLanguage.value,
                                                        self.ddModality.value),
                                                    width=200)

        row2 = ft.Row([self.ddModality, self._txtSentence, self._btnSpellCheck])

        # List view
        self._lvOut = ft.ListView(expand=True)

        self.page.add(row1, row2, self._lvOut)

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
