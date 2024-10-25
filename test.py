from typing import Dict, List, Optional, Union


def add_numbers(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


def process_list(items: List[int]) -> List[int]:
    return [item * 2 for item in items]


def get_user_info(user_id: int) -> Dict[str, Union[str, int]]:
    return {"id": user_id, "name": "John Doe", "age": 30}


def find_user(users: List[Dict[str, str]], name: str) -> Optional[Dict[str, str]]:
    for user in users:
        if user["name"] == name:
            return user
    return None


result1 = add_numbers(5, 3)
result2 = greet("Alice")
result3 = process_list([1, 2, 3, 4, 5])
result4 = get_user_info(123)
users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
]
result5 = find_user(users, "Alice")

print(result1, result2, result3, result4, result5)
