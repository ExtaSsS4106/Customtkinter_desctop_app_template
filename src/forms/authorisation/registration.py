from .. import ctk
import re
from src.ui.theme import make_entry, make_button, make_error_label, PAD

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class Registration(ctk.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        card = ctk.CTkFrame(self, corner_radius=16)
        card.grid(row=0, column=0)

        ctk.CTkLabel(
            card, text="Регистрация",
            font=("", 26, "bold"),
        ).pack(padx=40, pady=(30, 4))

        ctk.CTkLabel(
            card, text="Создайте новый аккаунт",
            font=("", 13), text_color="gray70",
        ).pack(pady=(0, 20))

        self.username_entry = make_entry(card, "Имя пользователя")
        self.username_entry.pack(padx=40, pady=PAD)

        self.email_entry = make_entry(card, "Email")
        self.email_entry.pack(padx=40, pady=PAD)

        self.password_entry = make_entry(card, "Пароль", show="•")
        self.password_entry.pack(padx=40, pady=PAD)

        self.confirm_entry = make_entry(card, "Повторите пароль", show="•")
        self.confirm_entry.pack(padx=40, pady=PAD)

        self.error = make_error_label(card)
        self.error.pack(pady=(4, 0))

        # Enter → регистрация
        for e in (self.username_entry, self.email_entry,
                  self.password_entry, self.confirm_entry):
            e.bind("<Return>", lambda _: self.on_register())

        make_button(card, "Зарегистрироваться", self.on_register)\
            .pack(padx=40, pady=(10, 8))

        ctk.CTkButton(
            card, text="Уже есть аккаунт? Войти",
            command=lambda: app.switch("login"),
            fg_color="transparent", hover=False,
            text_color=("#1f6aa5", "#4a9eff"),
            font=("", 12),
            width=280,
        ).pack(pady=(0, 24))

    # --- логика ---
    def on_register(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        error = self._validate(username, email, password, confirm)
        if error:
            self.error.configure(text=error)
            return

        # TODO: сохранить пользователя (БД/API)
        print(f"Зарегистрирован: {username} <{email}>")

        # после успеха → на логин, передав логин для автозаполнения
        self.app.switch("login", prefill_login=username)

    def _validate(self, username, email, password, confirm):
        if not all([username, email, password, confirm]):
            return "Заполните все поля"
        if len(username) < 3:
            return "Имя минимум 3 символа"
        if not EMAIL_RE.match(email):
            return "Некорректный email"
        if len(password) < 6:
            return "Пароль минимум 6 символов"
        if password != confirm:
            return "Пароли не совпадают"
        return None