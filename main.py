import file_operations
from faker import Faker
import random
import os


LITTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '}
OUTPUT_DIRECTORY = "output"
SKILLS_NAME = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"]
QUANTITY_CHARSHEET = 10


def generate_context():
    fake = Faker("ru_RU")
    first_name_male = fake.first_name_male()
    last_name_male = fake.last_name_male()
    city_name = fake.city()
    job_name = fake.job()
    strength = random.randint(1, 12)
    agility = random.randint(1, 12)
    endurance = random.randint(1, 12)
    intelligence = random.randint(1, 12)
    luck = random.randint(1, 12)
    three_random_skills = random.sample(SKILLS_NAME, 3)

    runic_skills = []

    for skill in three_random_skills:
        for letter in skill:
            for key, value in LITTERS_MAPPING.items():
                if letter == key:
                    skill = skill.replace(letter, value)
        runic_skills.append(skill)

    runic_skill_1, runic_skill_2, runic_skill_3 = runic_skills

    context = {
        "first_name": first_name_male,
        "last_name": last_name_male,
        "town": city_name,
        "job": job_name,
        "strength": strength,
        "agility": agility,
        "endurance": endurance,
        "intelligence": intelligence,
        "luck": luck,
        "skill_1": runic_skill_1,
        "skill_2": runic_skill_2,
        "skill_3": runic_skill_3}

    return context


def main():
    os.makedirs(OUTPUT_DIRECTORY, mode=0o777, exist_ok=True)

    for charsheet in range(QUANTITY_CHARSHEET):
        file_operations.render_template(
            "src/charsheet.svg",
            "{}/charsheet-{}.svg".format(OUTPUT_DIRECTORY, charsheet),
            generate_context())


if __name__ == '__main__':
    main()
