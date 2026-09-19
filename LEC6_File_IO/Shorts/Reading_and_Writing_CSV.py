import csv
import numpy as np    # module
from PIL import Image


def main():
    with open("views.csv", "r", encoding="utf-8") as views, open("analysis.csv", "w", encoding="utf-8", newline="") as analysis:    # 2개의 파일을 각각의 모드로 동시에 open, comma로 구분
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
            # views.csv와 analysis.csv의 header가 동일하고, reader의 fieldnames에 header가 list로 저장되어 있으므로, '+' operator를 이용해서 새로운 header를 list 형태로 추가

        writer.writeheader()
        
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"], 
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2)
                }
            )
            
            """
            # 다른 방법: dict row에 brightness라는 새로운 key를 추가하여 파일에 씀
            row["brightness"] = round(calculate_brightness(f"{row["id"]}.jpeg"), 2)
            writer.writerow(row)
            """


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255    # 밝기를 0~1 사이의 값으로 표현하기 위해 255로 나눔
    return brightness


main()