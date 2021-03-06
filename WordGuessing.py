import random


class Word:
    def __init__(self, n_guess, pack_words):
        if n_guess < 1 or pack_words is None:
            print('Wrong inputs.')
            return
        self.n_guess = n_guess
        self.pack_words = pack_words

    def generate_word(self):
        pack = self.pack_words
        words = pack.split(' ')
        word = random.choice(words)
        return word, len(word)


class WordsPacks:
    countries_pack = "Афганистан Индонезия Ирландия Канада Ливан Марокко Перу Судан Турция Финляндия Бельгия Болгария " \
                     "Грузия Индонезия Кения Ливия Малайзия Марокко Тунис Эстония Албания Андорра Ботсвана Бруней Гамбия " \
                     "Кувейт Либерия Мозамбик Непал Словакия Польша Украина"
    cities_pack = "Абиджан Анкара Бангкок Железногорск Монровия Мытищи Пятигорск Сидней Фейсалабад Ханьдань Бангкок " \
                  "Джибути Индаур Иокогама Пинду Смоленск Цзинань Чжэньцзян Элиста Анталья Браззавиль Дуала " \
                  "Калоокан Кальян Киншаса Коломбо Тайчжоу Ханьдань Чанша Астрахань Вэйфан Леон Любляна Могадишо Мурманск" \
                  "Оттава Рубцовск Читтагонг Шаосин Наленчув Варшава Киев Одесса Черноморск Берлин"
    profession_pack = "Аграрий Блогер Калькулятор Кочегар Лесоруб Музыкант Писатель Портной Терапевт Фальцовщик" \
                      "Географ Герольд Кинопродюсер Композитор Копирайтер Нейробиолог Педагог Радиофизик Скрипач Сыродел" \
                      "Актёр Биофизик Медиапланер Оптик Официант Прислуга Референт Телефонистка Торседор Фотокорреспондент" \
                      "Программист Арматурщик Астролог Генеалог Инфекционист Матадор Мореплаватель Охотник Педагог " \
                      "Электрогазосварщик Юрисконсульт"
