from . import ctk


class testview(ctk.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master)
        self.app = app

        # Обе колонки тянутся поровну
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Шапка — по содержимому (не растягиваем по вертикали)
        self.grid_rowconfigure(0, weight=0)

        # Нижняя строка — растягивается на всё оставшееся место
        self.grid_rowconfigure(1, weight=1)

        # Шапка на всю ширину
        card1 = ctk.CTkFrame(self, corner_radius=16, fg_color="#4a9eff")
        card1.grid(row=0, column=0, columnspan=2, sticky="ew",
                   padx=10, pady=(10, 5))

        # Две карточки слева-направо
        card2 = ctk.CTkFrame(self, corner_radius=16, fg_color="#4caf50")
        card2.grid(row=1, column=0, sticky="nsew",
                   padx=(10, 5), pady=(5, 10))

        card3 = ctk.CTkFrame(self, corner_radius=16, fg_color="#e05252")
        card3.grid(row=1, column=1, sticky="nsew",
                   padx=(5, 10), pady=(5, 10))
        card1.grid_rowconfigure(0, weight=1)
        ctk.CTkLabel(
                    card1, text="Вход",
                    font=("", 26, "bold"),
                ).grid(padx=20, pady=(10))