from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os


def main():
    os.makedirs('characters', exist_ok=True)
    cards_count=int(input("Введите количетсво карточек: "))
    for item in range(cards_count):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('template.html')
        clases_base = {
            'Маг': {
                'skills': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                'strength': random.randint(1,3),
                'agility': random.randint(1,3),
                'intelligence': 15,
                'luck': random.randint(1,3),
                'temper': random.randint(1,3),
                'image': '../images/wizard.png'
            },
            'Солдат': {
                'skills':  ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                'strength': 15,
                'agility': random.randint(1,3),
                'intelligence': random.randint(1,3),
                'luck': random.randint(1,3),
                'temper': random.randint(1,3),
                'image': '../images/warrior.png'
            },
            'Охотник': {
                'skills':  ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                'strength':  random.randint(1,3),
                'agility': 15,
                'intelligence': random.randint(1,3),
                'luck': random.randint(1,3),
                'temper': random.randint(1,3),
                'image': '../images/archer.png'
            },
            'Ассасин': {
                'skills': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'], 
                'strength':  random.randint(1,3),
                'agility': random.randint(1,3),
                'intelligence': random.randint(1,3),
                'luck': 15,
                'temper': random.randint(1,3),
                'image': '../images/assasin.png'
            },
            'Бард': {
                'skills': ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                'strength':  random.randint(1,3),
                'agility': random.randint(1,3),
                'intelligence': random.randint(1,3),
                'luck': random.randint(1,3),
                'temper': 15,
                'image': '../images/bard.png'        
            } 
        }
        character_name = input("Введите имя персонажа: ")
        character_rases = [
            'Орки',
            'Гном',
            'Эльф',
            'Человек'
        ]

        character__classes = [
            'Охотник',
            'Ассасин',
            'Бард',
            'Солдат',
            'Маг'
        ]

        character_class = int(input("""Выберите класс:
        1 - Охотник
        2 - Ассасин
        3 - Бард
        4 - Солдат
        5 - Маг
        Ваш выбор: """))

        character_rase = int(input("""Выберите рассу:
        1 - Орк
        2 - Гном
        3 - Эльф
        4 - Человек
        Ваш выбор: """))

        skills = random.sample(clases_base[character__classes[character_class -1]]["skills"], 3)

        rendered_page = template.render(
            name=character_name,
            race=character_rases[character_rase -1],
            character_class=character__classes[character_class -1],
            strength=clases_base[character__classes[character_class -1]]["strength"],
            agility=clases_base[character__classes[character_class -1]]["agility"],
            intelligence=clases_base[character__classes[character_class -1]]["intelligence"], 
            luck=clases_base[character__classes[character_class -1]]["luck"], 
            temper=clases_base[character__classes[character_class -1]]["temper"],
            image=clases_base[character__classes[character_class -1]]["image"],
            first_skill= skills[0],
            second_skill= skills[1],
            third_skill= skills[2]
        )


        with open(f'characters/index{item + 1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ =="__main__":
    main()