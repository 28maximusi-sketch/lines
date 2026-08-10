🧩 Головоломка «Линии» (ежедневные задания)
Версия: 1.0.0 | Лицензия: MIT | Статус: ✅ Активная разработка

https://img.shields.io/github/repo-size/yourusername/lines-puzzle https://img.shields.io/github/last-commit/yourusername/lines-puzzle https://img.shields.io/github/languages/count/yourusername/lines-puzzle

🧠 Описание
Головоломка «Линии» — это консольная программа, генерирующая ежедневные задания для популярной головоломки «Соедини точки» (Flow Free). Каждый день генерируется новая уникальная головоломка на основе даты, которую можно решать прямо в терминале.

Программа позволяет:

✅ Генерировать поле с парами цветных точек (размер 6×6, 8×8 и др.)

✅ Показывать решение (скрытый режим)

✅ Проверять правильность введённых линий (интерактивный режим)

✅ Использовать ежедневный «seed» для повторяемости

✅ Отображать поле с цветными символами (ANSI)

✨ Возможности
Функция	Описание
Генерация головоломки	Случайное размещение пар точек с гарантированным решением
Ежедневное задание	Фиксированный seed на основе даты → одинаково для всех
Интерактивный режим	Пошаговое построение линий (клавиатура)
Авто-решение	Показать готовое решение (клавиша s)
Проверка	Автоматическая верификация завершённого решения
Кроссплатформенность	Работает в любом терминале
📦 Установка и запуск
Каждая реализация находится в отдельной папке. Для запуска требуется соответствующий компилятор/интерпретатор.

Язык	Файл	Зависимости	Команда запуска
Python	lines.py	нет	python3 lines.py [--size 6] [--show-solution]
Go	lines.go	нет	go run lines.go [--size 6] [--show-solution]
Rust	lines.rs	clap, rand	cargo run -- [--size 6] [--show-solution]
C++	lines.cpp	нет (C++17)	g++ -std=c++17 -o lines lines.cpp && ./lines [--size 6] [--show-solution]
Java	Lines.java	нет	javac Lines.java && java Lines [--size 6] [--show-solution]
C#	lines.cs	нет (.NET Core)	dotnet run [--size 6] [--show-solution]
Ruby	lines.rb	нет	ruby lines.rb [--size 6] [--show-solution]
Node.js	lines.js	yargs, chalk	npm install yargs chalk && node lines.js [--size 6] [--show-solution]
Примечание: Все версии поддерживают общие опции: --size N (размер поля, по умолчанию 6), --show-solution (показать решение), --date YYYY-MM-DD (задать дату для ежедневного задания).

📂 Структура репозитория
text
.
├── README.md
├── python/
│   └── lines.py
├── go/
│   └── lines.go
├── rust/
│   ├── Cargo.toml
│   └── src/
│       └── main.rs
├── cpp/
│   └── lines.cpp
├── java/
│   └── Lines.java
├── csharp/
│   └── lines.cs
├── ruby/
│   └── lines.rb
└── javascript/
    ├── package.json
    └── lines.js
🎮 Использование
bash
# Сгенерировать ежедневную головоломку (размер 6)
lines

# Указать размер поля
lines --size 8

# Показать решение сразу
lines --show-solution

# Задать конкретную дату
lines --date 2025-01-01

# Интерактивный режим (ввод с клавиатуры)
lines --interactive
🛠️ Особенности реализаций
Python – простота и читаемость, алгоритм генерации с возвратом.

Go – высокая производительность, встроенный math/rand.

Rust – безопасность и скорость, rand и clap.

C++ – классика, STL, std::random.

Java – объектно-ориентированный подход, java.util.Random.

C# – современный синтаксис, LINQ.

Ruby – выразительный код, встроенный Random.

Node.js – асинхронный ввод, библиотеки chalk и yargs.

🤝 Вклад
PR и issues приветствуются. Добавляйте новые размеры, улучшайте алгоритмы, расширяйте функциональность.

📄 Лицензия
MIT License.

