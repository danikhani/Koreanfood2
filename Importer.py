from pathlib import Path


def get_food_image(food_name):
    base_path = Path(__file__)
    file_path = (base_path / f"../images/{food_name}.png").resolve()
    return file_path


