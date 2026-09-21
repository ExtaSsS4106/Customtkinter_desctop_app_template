# src/forms/components_demo.py
import customtkinter as ctk


class ComponentsDemo(ctk.CTkFrame):
    """Витрина всех виджетов CustomTkinter."""

    def __init__(self, master, app, **kwargs):
        super().__init__(master, fg_color="transparent")
        self.app = app

        # ---------- Шапка ----------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20, 10))

        ctk.CTkLabel(
            header, text="Все компоненты CustomTkinter",
            font=("", 24, "bold"),
        ).pack(side="left")

        ctk.CTkButton(
            header, text="← Назад",
            width=100, command=lambda: app.switch("login"),
        ).pack(side="right")

        # ---------- Скролл-контейнер ----------
        self.scroll = ctk.CTkScrollableFrame(self, corner_radius=12)
        self.scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self._build_labels()
        self._build_buttons()
        self._build_entries()
        self._build_checkbox_radio()
        self._build_switches()
        self._build_slider_progress()
        self._build_selectors()
        self._build_textbox()
        self._build_segmented()
        self._build_tabview()
        self._build_theme_switcher()

    # =========================================================
    # Утилита: секция с заголовком
    # =========================================================
    def _section(self, title):
        ctk.CTkLabel(
            self.scroll, text=title,
            font=("", 16, "bold"),
            anchor="w",
        ).pack(fill="x", padx=10, pady=(18, 8))
        frame = ctk.CTkFrame(self.scroll, corner_radius=10)
        frame.pack(fill="x", padx=10, pady=(0, 4))
        return frame

    # =========================================================
    # CTkLabel — разные стили
    # =========================================================
    def _build_labels(self):
        f = self._section("CTkLabel")

        ctk.CTkLabel(f, text="Обычный текст").pack(anchor="w", padx=15, pady=6)
        ctk.CTkLabel(f, text="Жирный", font=("", 16, "bold")).pack(anchor="w", padx=15, pady=6)
        ctk.CTkLabel(f, text="Курсив", font=("", 14, "italic")).pack(anchor="w", padx=15, pady=6)
        ctk.CTkLabel(f, text="Красный", text_color="#e05252").pack(anchor="w", padx=15, pady=6)
        ctk.CTkLabel(
            f, text="С рамкой и фоном",
            fg_color=("#e0e0e0", "#2b2b2b"),
            corner_radius=8,
        ).pack(anchor="w", padx=15, pady=(6, 12))

    # =========================================================
    # CTkButton — цвета, состояния, варианты
    # =========================================================
    def _build_buttons(self):
        f = self._section("CTkButton")

        row = ctk.CTkFrame(f, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(row, text="Обычная").pack(side="left", padx=4)
        ctk.CTkButton(row, text="Успех", fg_color="#4caf50", hover_color="#3d8b40").pack(side="left", padx=4)
        ctk.CTkButton(row, text="Опасная", fg_color="#e05252", hover_color="#b03e3e").pack(side="left", padx=4)
        ctk.CTkButton(row, text="Прозрачная", fg_color="transparent", border_width=1).pack(side="left", padx=4)
        ctk.CTkButton(row, text="Отключена", state="disabled").pack(side="left", padx=4)

        row2 = ctk.CTkFrame(f, fg_color="transparent")
        row2.pack(fill="x", padx=15, pady=(0, 12))

        ctk.CTkButton(row2, text="Со стрелкой →", width=160).pack(side="left", padx=4)
        ctk.CTkButton(
            row2, text="С иконкой", width=160,
            image=None,  # сюда можно подсунуть CTkImage
        ).pack(side="left", padx=4)

    # =========================================================
    # CTkEntry — обычный, пароль, с placeholder
    # =========================================================
    def _build_entries(self):
        f = self._section("CTkEntry")

        ctk.CTkEntry(f, placeholder_text="Обычное поле", width=300).pack(anchor="w", padx=15, pady=6)
        ctk.CTkEntry(f, placeholder_text="Пароль", show="•", width=300).pack(anchor="w", padx=15, pady=6)
        ctk.CTkEntry(f, placeholder_text="С рамкой", border_width=2, border_color="#4a9eff", width=300)\
            .pack(anchor="w", padx=15, pady=(6, 12))

    # =========================================================
    # CTkCheckBox и CTkRadioButton
    # =========================================================
    def _build_checkbox_radio(self):
        f = self._section("CTkCheckBox / CTkRadioButton")

        ctk.CTkCheckBox(f, text="Галочка 1").pack(anchor="w", padx=15, pady=6)
        ctk.CTkCheckBox(f, text="Галочка 2 (отмечена)").pack(anchor="w", padx=15, pady=6)
        checked = ctk.CTkCheckBox(f, text="Предустановлено")
        checked.select()
        checked.pack(anchor="w", padx=15, pady=(6, 12))

        self.radio_var = ctk.StringVar(value="a")
        for val, label in [("a", "Вариант A"), ("b", "Вариант B"), ("c", "Вариант C")]:
            ctk.CTkRadioButton(
                f, text=label, variable=self.radio_var, value=val,
            ).pack(anchor="w", padx=15, pady=4)
        ctk.CTkLabel(f, text="").pack(pady=4)  # отступ

    # =========================================================
    # CTkSwitch
    # =========================================================
    def _build_switches(self):
        f = self._section("CTkSwitch")

        ctk.CTkSwitch(f, text="Включить уведомления").pack(anchor="w", padx=15, pady=6)
        on = ctk.CTkSwitch(f, text="Уже включено")
        on.select()
        on.pack(anchor="w", padx=15, pady=(6, 12))

    # =========================================================
    # CTkSlider и CTkProgressBar
    # =========================================================
    def _build_slider_progress(self):
        f = self._section("CTkSlider / CTkProgressBar")

        self.slider_label = ctk.CTkLabel(f, text="Громкость: 50")
        self.slider_label.pack(anchor="w", padx=15, pady=(8, 4))

        ctk.CTkSlider(
            f, from_=0, to=100,
            command=self._on_slider,
            width=300,
        ).pack(anchor="w", padx=15, pady=6)
        ctk.CTkSlider(f, from_=0, to=100, number_of_steps=10, width=300)\
            .pack(anchor="w", padx=15, pady=6)

        self.progress = ctk.CTkProgressBar(f, width=300)
        self.progress.set(0.35)
        self.progress.pack(anchor="w", padx=15, pady=(10, 4))

        self.progress_ind = ctk.CTkProgressBar(f, width=300, mode="indeterminate")
        self.progress_ind.pack(anchor="w", padx=15, pady=(0, 4))
        self.progress_ind.start()

        ctk.CTkButton(f, text="Обновить прогресс", command=self._bump_progress)\
            .pack(anchor="w", padx=15, pady=(4, 12))

    def _on_slider(self, value):
        self.slider_label.configure(text=f"Громкость: {int(value)}")

    def _bump_progress(self):
        v = self.progress.get() + 0.1
        if v > 1:
            v = 0
        self.progress.set(v)

    # =========================================================
    # CTkComboBox и CTkOptionMenu
    # =========================================================
    def _build_selectors(self):
        f = self._section("CTkComboBox / CTkOptionMenu")

        ctk.CTkLabel(f, text="ComboBox (можно вводить своё):").pack(anchor="w", padx=15, pady=(8, 2))
        ctk.CTkComboBox(f, values=["Python", "Rust", "Go", "C++"], width=300)\
            .pack(anchor="w", padx=15, pady=(0, 10))

        ctk.CTkLabel(f, text="OptionMenu (только выбор):").pack(anchor="w", padx=15, pady=(4, 2))
        ctk.CTkOptionMenu(f, values=["Тёмная", "Светлая", "Системная"], width=300)\
            .pack(anchor="w", padx=15, pady=(0, 12))

    # =========================================================
    # CTkTextbox
    # =========================================================
    def _build_textbox(self):
        f = self._section("CTkTextbox")

        tb = ctk.CTkTextbox(f, width=400, height=100)
        tb.pack(anchor="w", padx=15, pady=(8, 12))
        tb.insert("0.0", "Здесь можно писать многострочный текст...\nИ даже ещё строку.\n")

    # =========================================================
    # CTkSegmentedButton
    # =========================================================
    def _build_segmented(self):
        f = self._section("CTkSegmentedButton")

        seg = ctk.CTkSegmentedButton(
            f, values=["День", "Неделя", "Месяц", "Год"],
            command=lambda v: print(f"Выбрано: {v}"),
        )
        seg.set("Неделя")
        seg.pack(anchor="w", padx=15, pady=(8, 12))

    # =========================================================
    # CTkTabview
    # =========================================================
    def _build_tabview(self):
        f = self._section("CTkTabview")

        tab = ctk.CTkTabview(f, width=400, height=140)
        tab.pack(anchor="w", padx=15, pady=(8, 12))

        tab.add("Профиль")
        tab.add("Настройки")
        tab.add("О программе")

        ctk.CTkLabel(tab.tab("Профиль"), text="Тут профиль пользователя").pack(pady=20)
        ctk.CTkLabel(tab.tab("Настройки"), text="Тут настройки").pack(pady=20)
        ctk.CTkLabel(tab.tab("О программе"), text="Demo v1.0").pack(pady=20)

    # =========================================================
    # Переключатель темы (глобальный)
    # =========================================================
    def _build_theme_switcher(self):
        f = self._section("Внешний вид (глобально)")

        row = ctk.CTkFrame(f, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=8)

        ctk.CTkLabel(row, text="Тема:").pack(side="left", padx=(0, 8))
        ctk.CTkOptionMenu(
            row, values=["System", "Light", "Dark"],
            command=ctk.set_appearance_mode, width=140,
        ).pack(side="left")

        ctk.CTkLabel(row, text="  Акцент:").pack(side="left", padx=(20, 8))
        ctk.CTkOptionMenu(
            row, values=["blue", "green", "dark-blue"],
            command=ctk.set_default_color_theme, width=140,
        ).pack(side="left", pady=(0, 4))