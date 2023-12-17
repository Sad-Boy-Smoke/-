import customtkinter as ok

ok.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ok.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ok.CTk):
    def __init__(self):
        super().__init__()
        self.element_created = False
        self.boli = False
        # Конфигурация окна проги
        self.title("Made by kurda team")
        self.geometry(f"{260}x{710}")
        self.resizable(False, False)

        # Конфигурация сетки для виджетов (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1), weight=0)
        self.grid_rowconfigure((2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # Frame для девиза&текста&выпадающего меню
        self.sidebar_frame = ok.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))

        # Девиз проги
        self.logo_label = ok.CTkLabel(self.sidebar_frame, text="Likes for work",
                                      font=ok.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Текст описывающий поле выбора метода авторизации
        self.logo_label = ok.CTkLabel(self.sidebar_frame, text="Выберите метод авторизации", font=ok.CTkFont(size=14))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))

        # Выбор метода авторизации
        list_choose_method_log = ["Стандартная авторизация", "Авторизация через Google", "Ручная авторизация"]
        self.choose_log = ok.CTkOptionMenu(self.sidebar_frame, values=list_choose_method_log, width=200,
                                           command=self.add_entry)
        self.choose_log.grid(row=2, column=0, padx=20, pady=(10, 10))

        # Frame для theme и scale
        self.theme_scale = ok.CTkFrame(self, width=140, corner_radius=0)
        self.theme_scale.grid(row=11, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))
        # Выбор темы приложения
        self.appearance_mode_label = ok.CTkLabel(self.theme_scale, text="Выбор темы")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ok.CTkOptionMenu(self.theme_scale, values=["Light", "Dark", "System"],
                                                            command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Выбор масштаба интерфейса
        self.scaling_label = ok.CTkLabel(self.theme_scale, text="Масштабирование интерфейса")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ok.CTkOptionMenu(self.theme_scale, values=["80%", "90%", "100%", "110%", "120%"],
                                                    command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

    def add_entry(self, a):

        def write_to_file_like(w):

            global data_like
            data_like = int(w)
            
            self.Label.configure(text=f"Выбронно кол-во лайков: {data_like}")
            
        def create_for_3():
            # Frame для кнопки запуск
            self.run_button = ok.CTkFrame(self, width=1, corner_radius=0)
            self.run_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

            # Кнопка запуска
            self.run = ok.CTkButton(self.run_button, text="Запуууууск!!!!!", command=self.bot, width=220)
            self.run.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

            # Frame для slider
            self.bar = ok.CTkFrame(self, width=140, corner_radius=0)
            self.bar.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), )

            # Slider like
            self.slider_1 = ok.CTkSlider(self.bar, command=write_to_file_like, from_=1, to=200, number_of_steps=20)
            self.slider_1.grid(row=0, column=0, padx=20, pady=(10, 10))
            self.slider_1.set(1)

            # Текст значение с ползунка
            self.Label = ok.CTkLabel(self.bar, text="Выбранное кол-во лайков: ")
            self.Label.grid(row=1, column=0, padx=20, pady=(10, 10))            

        def create():
            # Frame для полей ввода и кнопки сохранения данных
            self.entry_frame = ok.CTkFrame(self, width=140, corner_radius=0)
            self.entry_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

            # Ввод Gmail
            self.entry_gmail = ok.CTkEntry(self.entry_frame, placeholder_text="Введите Gmail", width=220)
            self.entry_gmail.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

            # Ввод пароля
            self.entry_password = ok.CTkEntry(self.entry_frame, placeholder_text="Введите пароль", width=220)
            self.entry_password.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

            # Кнопка сохранения данных
            self.write_button = ok.CTkButton(self.entry_frame, text="Сохранить", command=self.write_to_file)
            self.write_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

            # Frame для slider
            self.bar = ok.CTkFrame(self, width=140, corner_radius=0)
            self.bar.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), )

            # Slider like
            self.slider_1 = ok.CTkSlider(self.bar, command=write_to_file_like, from_=1, to=200, number_of_steps=20)
            self.slider_1.grid(row=0, column=0, padx=20, pady=(10, 10))
            self.slider_1.set(1)

            # Текст значение с ползунка
            self.Label = ok.CTkLabel(self.bar, text="Выбранное кол-во лайков: ")
            self.Label.grid(row=1, column=0, padx=20, pady=(10, 10))

            # Frame для кнопки запуск
            self.run_button = ok.CTkFrame(self, width=1, corner_radius=0)
            self.run_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

            # Кнопка запуска
            self.run = ok.CTkButton(self.run_button, text="Запуууууск!!!!!", command=self.bot, width=220)
            self.run.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        def delete():
            if hasattr(self, "entry_frame"):
                self.entry_frame.grid_forget()

        delete()

        if a == "Стандартная авторизация":
            create()

            global choose_int
            choose_int = 1

        if a == "Авторизация через Google":
            create()

            choose_int = 2

        if a == "Ручная авторизация":
            delete()
            create_for_3()
            choose_int = 3

    def write_to_file(self):
        global line2, line1
        line1 = self.entry_gmail.get()
        line2 = self.entry_password.get()
        if line1 and line2 != "":
            self.boli = True
        else:
            self.boli = False

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ok.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ok.set_widget_scaling(new_scaling_float)

    def bot(self):
        
        {
            #раньше здесь был исполняющий код
        }


if __name__ == "__main__":
    app = App()
    app.mainloop()