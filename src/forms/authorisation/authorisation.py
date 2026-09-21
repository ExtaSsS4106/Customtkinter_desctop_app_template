from .. import ctk

from src.ui.theme import make_entry, make_button, make_error_label, PAD, ENTRY_WIDTH


class Authorisation(ctk.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color="transparent")
        self.app = app

        # Карточка по центру
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        card = ctk.CTkFrame(self, corner_radius=16)
        card.grid(row=0, column=0)

        # Заголовок
        ctk.CTkLabel(
            card, text="Вход",
            font=("", 26, "bold"),
        ).pack(padx=40, pady=(30, 4))

        ctk.CTkLabel(
            card, text="Введите данные аккаунта",
            font=("", 13), text_color="gray70",
        ).pack(pady=(0, 20))

        # Поля
        self.login_entry = make_entry(card, "Логин или email")
        self.login_entry.pack(padx=40, pady=PAD)

        self.password_entry = make_entry(card, "Пароль", show="•")
        self.password_entry.pack(padx=40, pady=PAD)

        # Ошибка
        self.error = make_error_label(card)
        self.error.pack(pady=(4, 0))

        # Enter как «войти»
        self.password_entry.bind("<Return>", lambda e: self.on_login())
        self.login_entry.bind("<Return>", lambda e: self.password_entry.focus())

        # Кнопка «Войти»
        make_button(card, "Войти", self.on_login).pack(padx=40, pady=(10, 8))

        # Ссылка на регистрацию
        ctk.CTkButton(
            card, text="Нет аккаунта? Зарегистрироваться",
            command=lambda: app.switch("signup"),
            fg_color="transparent", hover=False,
            text_color=("#1f6aa5", "#4a9eff"),
            font=("", 12),
            width=ENTRY_WIDTH,
        ).pack(pady=(0, 24))

    # --- логика ---
    def on_login(self):
        login = self.login_entry.get().strip()
        password = self.password_entry.get()

        if not login or not password:
            self.error.configure(text="Заполните все поля")
            return

        if len(password) < 6:
            self.error.configure(text="Пароль слишком короткий")
            return

        # TODO: заменить на реальную проверку (БД/API)
        if login == "admin" and password == "admin123":
            self.error.configure(text="")
            self.app.switch("dashboard", username=login)
        else:
            self.error.configure(text="Неверный логин или пароль")
            self.password_entry.delete(0, "end")