import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("post_id, expected_title_contains", [
    (1, "sunt"),  # Пост 1 должен содержать "sunt"
    (2, "qui"),  # Пост 2 должен содержать "qui"
    (3, "ea molestias"),  # Пост 3 должен содержать "ea molestias"
])
def test_multiple_posts_content(post_id, expected_title_contains):
    """Проверяем несколько постов с разными ожиданиями"""

    print(f"Проверяем пост {post_id}...")
    response = requests.get(f"{BASE_URL}/posts/{post_id}")

    assert response.status_code == 200
    post_data = response.json()

    # Проверяем, что заголовок содержит ожидаемое слово
    assert expected_title_contains in post_data["title"].lower()
    print(f"Пост {post_id}: '{post_data['title'][:30]}...' содержит '{expected_title_contains}'")


# https://jsonplaceholder.typicode.com/posts/1
# https://jsonplaceholder.typicode.com/posts/2
# https://jsonplaceholder.typicode.com/posts/3