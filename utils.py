import json
URL = 'https://picsum.photos/200'


def json_load() -> list:
    """
    Загружает данные из файла candidates.json
    :return: список json
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        result = json.load(file)
    return result


def get_all_candidates() -> str:
    """Получает список всех кандидатов из файла candidates.json"""
    result = '<pre>\nНаши кандидаты:\n'
    for candidate in json_load():
        result += f"\n\tИмя кандидата: {candidate['name']}\n" \
                  f"\tПозиция кандидата: {candidate['position']}\n" \
                  f"\tНавыки кандидата: {candidate['skills'].lower()}\n"
    result += '</pre>'
    return result


def get_candidates_by_pk(pk) -> str:
    """Получает кандидата по уникальному 'pk'"""
    for candidate in json_load():
        if candidate['pk'] == pk:
            result = f'<pre>\tКандидат номер {pk}</pre>' \
                     f'<pre>\t<img src="{URL}"><pre>\n'
            result += f"\n\tИмя кандидата: {candidate['name']}\n" \
                      f"\tПозиция кандидата: {candidate['position']}\n" \
                      f"\tНавыки кандидата: {candidate['skills'].lower()}\n"
            result += '</pre>'
            return result


def get_candidate_by_skill(uid) -> str:
    """Получает кандидата по требуемому навыку"""
    result = '<pre>'
    for line in json_load():

        if uid in line['skills'].lower():
            result += f"\n\tИмя кандидата: {line['name']}\n" \
                      f"\tПозиция кандидата: {line['position']}\n" \
                      f"\tНавыки кандидата: {line['skills'].lower()}\n"
    result += '</pre>'
    return result
###############################################################################################
