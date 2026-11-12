BASE_URL = "https://stellarburgers.education-services.ru"

# Регистрация (страница https://stellarburgers.education-services.ru/register)

# Поле "Имя"
REG_INPUT_NAME = "//label[contains(text(), 'Имя')]/following-sibling::input"
# Поле "Email"
REG_INPUT_EMAIL = "//label[contains(text(), 'Email')]/following-sibling::input"
# Поле "Пароль"
REG_INPUT_PASSWORD =  "//input[@type='password']"
# Кнопка "Зарегистрироваться"
BTN_REGISTER = '//button[contains(text(), "Зарегистрироваться")]'
# Ошибка для некорректного пароля
ERROR_PASSWORD = "//p[text()='Некорректный пароль']"

# Вход (страница https://stellarburgers.education-services.ru/login) 

# Поле "Email"
INPUT_LOGIN_EMAIL = '//input[@placeholder="Email"]' 
# Поле "Пароль"
INPUT_LOGIN_PASSWORD = '//input[@placeholder="Пароль"]'
# Кнопка "Войти"
BTN_LOGIN = "//button[contains(text(), 'Войти')]"
# ссылка "Зарегистрироваться" на странице входа
LINK_REGISTER = '//a[contains(text(), "Зарегистрироваться")]'
# ссылка "Восстановить пароль" на странице входа
LOGIN_LINK_RECOVER = "//a[contains(., 'Восстановить пароль')]"
# ссылка "Войти" на странице входа
REG_LINK_LOGIN = "//a[contains(., 'Войти')]"

INPUT_LOGIN_EMAIL1 = "//form//input[@type='text']"
INPUT_LOGIN_PASSWORD1 = "//input[@type='password']"

# Личный кабинет (страница https://stellarburgers.education-services.ru/account/profile) 
BTN_PROFILE = '//a[contains(text(), "Личный кабинет")]'

# Кнопка "Выход"
BTN_LOGOUT = "//button[contains(text(), 'Выход')]"


# Навигация (страница https://stellarburgers.education-services.ru)

# Раздел "Булки"
TAB_BUNS = "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab')]"
# Раздел "Соусы"
TAB_SAUCES = "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab')]"
# Раздел "Начинки"
TAB_FILLINGS = "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab')]"
# Раздел "Булки" активен
TAB_BUNS_ACTIVE     = "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(., 'Булки')]]"
# Раздел "Соусы" активен
TAB_SAUCES_ACTIVE   = "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(., 'Соусы')]]"
# Раздел "Начинки" активен
TAB_FILLINGS_ACTIVE = "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(., 'Начинки')]]"
# Кнопка "Войти в аккаунт"
BTN_LOGIN_ON_HOME = "//button[contains(., 'Войти в аккаунт')]"
# Ссылка "Личный кабинет"
LINK_PROFILE = "//a[@href='/account']"
# Ссылка "Конструктор"
LINK_CONSTRUCTOR = "//p[text()='Конструктор']"
# Логотип "Stellar Burgers"
LOGO_STELLAR = "//div[contains(@class, 'AppHeader_header__logo')]//a"


MODAL_OVERLAY = "//div[contains(@class, 'Modal_modal_overlay')]"
MODAL_CLOSE = "//button[contains(@class, 'Modal_close')]"
