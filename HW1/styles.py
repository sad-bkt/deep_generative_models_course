import itertools
import math
import random

styles = {
    'прическа': [
        'нет волос',
        'длинные в пучок',
        'длинные волнистые',
        'длинные прямые',
        'короткая волнистые',
        'короткая прямые',
        'короткая курчавые'
    ],
    'цвет волос': [
        'черный',
        'блонд',
        'каштановый',
        'пастельный розовый',
        'рыжий',
        'серебристо серый',
    ],
    'аксессуар': [
        'нет очков',
        'круглые очки',
        'солнцезащитные очки',
    ],
    'одежда': [
        'худи',
        'комбинезон',
        'футболка с круглым вырезом',
        'футболка с V-вырезом',
    ],
    'цвет одежды': [
        'черный',
        'синий',
        'серый',
        'зеленый',
        'оранжевый',
        'розовый',
        'красный',
        'белый'
    ],
}

styles_count = {
    'прическа': [
        7,
        0,
        1,
        23,
        1,
        11,
        7
    ],
    'цвет волос': [
        7,
        6,
        2,
        3,
        8,
        24,
    ],
    'аксессуар': [
        11,
        22,
        17,
    ],
    'одежда': [
        7,
        18,
        19,
        6,
    ],
    'цвет одежды': [
        4,
        5,
        6,
        8,
        6,
        8,
        7,
        6
    ],
}


def generate_style():
    styles_prob = {i: [j + 1 for j in styles_count[i]] for i in styles_count.keys()}
    divider = math.prod(sum(styles_prob[i]) for i in styles_prob.keys())
    keys, values = zip(*styles.items())
    permutations = list(dict(zip(keys, v)) for v in itertools.product(*values))
    keys, values = zip(*styles_prob.items())
    prob = list(math.prod(v)/divider for v in itertools.product(*values))
    res = random.choices(permutations, cum_weights=prob)[0]
    return res, prob[permutations.index(res)]
