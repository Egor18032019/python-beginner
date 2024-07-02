#  задание
#  напишите сортировку с лямбдой, которая вернёт минимальный элемент из списка `people`,
#  сортировка должна быть
#  сначала по возрасту, а потом по имени


people = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 20, "work": "true"},
    {"name": "B ", "age": 20, "work": "true"},
    {"name": "Diana", "age": 30},
]


def min_person(people: list[dict]) -> dict:
    return min(people, key=lambda x: (x["age"], len(x["name"])))


sort_by_len_lambda = min(people, key=lambda x: (x["age"], len(x["name"])))
print(sort_by_len_lambda)
