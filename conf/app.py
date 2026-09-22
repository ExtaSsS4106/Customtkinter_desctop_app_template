import customtkinter as ctk
from src.forms.page_register import routes, init_page
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.current = None
        self._routes = {name: cls for name, cls in routes}
        self.start_point = init_page
        self.minsize(600, 400)     # не меньше 600×400
        self.maxsize(1200, 900)    # не больше 1200×900

    def register(self, name, page_class):
        """Регистрируем страницу под именем."""
        self._routes[name] = page_class

    def switch(self, name, **kwargs):
        """Переключаемся по имени."""
        if self.current:
            self.current.destroy()

        PageClass = self._routes[name]
        self.current = PageClass(self, self, **kwargs)
        self.current.pack(fill="both", expand=True)

    def init_page(self):
        if self.start_point:
            self.switch(self.start_point)
        else:
            raise KeyError(f"start_point can't be None")