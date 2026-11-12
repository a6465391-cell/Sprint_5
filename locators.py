BASE_URL = "https://stellarburgers.education-services.ru"

REG_INPUT_NAME = "//label[contains(text(), 'Имя')]/following-sibling::input"
REG_INPUT_EMAIL = "//label[contains(text(), 'Email')]/following-sibling::input"
REG_INPUT_PASSWORD =  "//input[@type='password']"
BTN_REGISTER = '//button[contains(text(), "Зарегистрироваться")]'
ERROR_PASSWORD = "//p[text()='Некорректный пароль']"

INPUT_LOGIN_EMAIL = '//input[@placeholder="Email"]' 
INPUT_LOGIN_PASSWORD = '//input[@placeholder="Пароль"]'
BTN_LOGIN = "//button[contains(text(), 'Войти')]"
LINK_REGISTER = '//a[contains(text(), "Зарегистрироваться")]'
LOGIN_LINK_RECOVER = "//a[contains(., 'Восстановить пароль')]"
REG_LINK_LOGIN = "//a[contains(., 'Войти')]"

INPUT_LOGIN_EMAIL1 = "//form//input[@type='text']"
INPUT_LOGIN_PASSWORD1 = "//input[@type='password']"
 
BTN_PROFILE = '//a[contains(text(), "Личный кабинет")]'

BTN_LOGOUT = "//button[contains(text(), 'Выход')]"

TAB_BUNS = "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab')]"
TAB_SAUCES = "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab')]"
TAB_FILLINGS = "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab')]"
TAB_BUNS_ACTIVE     = "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(., 'Булки')]]"
TAB_SAUCES_ACTIVE   = "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(., 'Соусы')]]"
TAB_FILLINGS_ACTIVE = "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(., 'Начинки')]]"
BTN_LOGIN_ON_HOME = "//button[contains(., 'Войти в аккаунт')]"
LINK_PROFILE = "//a[@href='/account']"
LINK_CONSTRUCTOR = "//p[text()='Конструктор']"
LOGO_STELLAR = "//div[contains(@class, 'AppHeader_header__logo')]//a"

MODAL_OVERLAY = "//div[contains(@class, 'Modal_modal_overlay')]"
MODAL_CLOSE = "//button[contains(@class, 'Modal_close')]"
