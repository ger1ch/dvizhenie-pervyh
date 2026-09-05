import sys
from pathlib import Path
import qrcode

if len(sys.argv) < 2:
    print("Использование:")
    print("python generate_qr.py https://USERNAME.github.io/dvizhenie-pervyh/")
    raise SystemExit

base = sys.argv[1].rstrip("/") + "/"

pages = [
("01_Образование_и_знания", "education.html"),
("02_Наука_и_технологии", "science.html"),
("03_Труд_профессия_и_свое_дело", "career.html"),
("04_Культура_и_искусство", "culture.html"),
("05_Волонтерство_и_добровольчество", "volunteer.html"),
("06_Патриотизм_и_историческая_память", "memory.html"),
("07_Спорт", "sport.html"),
("08_Здоровый_образ_жизни", "health.html"),
("09_Медиа_и_коммуникации", "media.html"),
("10_Дипломатия_и_международные_отношения", "diplomacy.html"),
("11_Экология_и_охрана_природы", "ecology.html"),
("12_Туризм_и_путешествия", "tourism.html"),
]

out = Path("qr_codes")
out.mkdir(exist_ok=True)

for name, page in pages:
    url = base + page
    img = qrcode.make(url)
    img.save(out / f"{name}.png")
    print(name, "->", url)

print("\\nГотово. QR-коды находятся в папке qr_codes.")
