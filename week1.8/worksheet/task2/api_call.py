import json
from typing import Any

import httpx

BASE_URL = "https://dummyjson.com/"


def send_api_request(content: str) -> tuple[int, Any]:
    """Send API request and return status code, response json."""

    url = BASE_URL + content  # API request
    response = httpx.get(url)  # API call

    return response.status_code, response.json()


def get_difficulties() -> None:
    status_code, response_json = send_api_request(content="recipe/meal-type/snack")

    print(
        f"[1] difficulties: {', '.join(recipe.get('difficulty') for recipe in response_json.get('recipes'))}"
    )


def count_products_containing_apple() -> None:
    status_code, response_json = send_api_request(content="products/search?q=apple")

    print(f"[2] Number of apple products: {len(response_json.get('products'))}")


def count_likes_for_post_five() -> None:
    status_code, response_json = send_api_request(content="posts/5")
    print(f"[3] Likes for post 5: {response_json['reactions']['likes']}")


def main():
    get_difficulties()
    count_products_containing_apple()
    count_likes_for_post_five()


if __name__ == "__main__":
    main()


# print(json.dumps(content, indent=2))
