# BankWidget

Краткое описание проекта, его цели и задачи.
Проект работает с банковскими операциями клиентов. Позволяет наглядно работать с данными.
...

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/olgapythonwq/BankWidget.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd ваш_проект
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

## Вклад

Если вы хотите внести свой вклад, пожалуйста, создайте форк репозитория и отправьте пул-реквест.
