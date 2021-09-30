# Консольное приложение автоматизирующее процессы предприятия, которое занимается изготовлением мебели под заказ.

## Описание предприятия
Мебельный центр занимается изготовлением мебели на заказ. Дизайнер
приезжает к клиенту, замеряет необходимые параметры будущей мебели и
составляет предварительную смету. Клиент вносит предоплату для закупки
необходимых материалов. После изготовления мебели рассчитывается
окончательная стоимость заказа, осуществляется доставка и сборка,
происходит полный расчет за заказ.

Данные используемые программой хранятся в json формате в директории [repo](repo).

## Для запуска приложения:

```
python main.py
```

## Данные для входа:
- Логин: vverma0
- Пароль: passwd 

## Инструкция по программе

### Команды, которые можно использовать для взаимодействия с программой:
| | |
|-------------|---------------------|
| help        | cправка по программе |
| clients     | перейти в меню для работы с информацией о клиентах |
| employees   | перейти в меню для работы с информацией о сотрудниках |
| furnitures  | перейти в меню для работы с информацией о мебели |
| orders      | перейти в меню для работы с информацией о заказах |
| home        | вернуться в главное меню |
| q           | выход |

### Команды, которые можно использовать для управления информацией о клиентах:

| | |
|-------------|---------------------|
|help        | справка по подсистеме клиентов|
|getall:     |  вывести список всех клиентов|
|get id      | вывести информацию об определенном клиенте (id - это ИД клиента)|
|add         | добавить клиента в список|
|del id      | удалить клиента по ИД (id - это ИД клиента)|
|edit id     | изменить информацию о клиенте (id - это ИД клиента)|
|home        | вернуться в главное меню|
|q           | выход|

### Команды, которые можно использовать для управления информацией о сотрудниках:

| | |
|-------------|---------------------|
|help        | справка по подсистеме сотрудников|
|getall      | вывести список всех сотрудников|
|get id      | вывести информацию об определенном сотруднике (id - это ИД |сотрудника)|
|add         | добавить сотрудника в список|
|del id      | удалить сотрудника по ИД (id - это ИД сотрудника)|
|edit id     | изменить информацию о сотруднике (id - это ИД сотрудника)|
|home        | вернуться в главное меню|
|q           | выход|

### Команды, которые можно использовать для управления информацией о мебели:

| | |
|-------------|---------------------|
|help        | справка по подсистеме мебели|
|getall      | вывести список всей мебели|
|get id      | вывести информацию об определенной мебели (id - это ИД мебели)|
|add         | добавить мебель в список|
|del id      | удалить мебель по ИД (id - это ИД мебели)|
|edit id     | изменить информацию о мебели (id - это ИД мебели)|
|home        | вернуться в главное меню|
|q           | выход|

### Команды, которые можно использовать для управления информацией о заказах:

| | |
|-------------|---------------------|
|help        | справка по подсистеме заказов|
|getall      | вывести список всех заказов|
|get id      | вывести информацию об определенном заказе (id - это ИД заказа)|
|add         | добавить новый заказ|

| | |
|-------------|---------------------|
|fur id      | добавить мебель в заказ (id - это ИД заказа)|
|delfur id   | удалить мебель из заказа (id - это ИД заказа)|
|designer id | изменить дизайнера заказа (id - это ИД заказа)|
|manager id  | изменить менеджера заказа (id - это ИД заказа)|
|courier id  | изменить курьера заказа (id - это ИД заказа)|

| | |
|-------------|---------------------|
|prepay id   | внести предоплату по заказу (id - это ИД заказа)|
|made id     | присвоить заказу статус "Изготовлен" (id - это ИД заказа)|
|delivery id | перенести заказ в стадию доставки (id - это ИД заказа)|
|done id     | завершить заказ (id - это ИД заказа)|

| | |
|-------------|---------------------|
|del id      | удалить заказ по ИД (id - это ИД заказа) (id - это ИД заказа)|
|edit id     | изменить информацию о заказе (id - это ИД заказа)|

| | |
|-------------|---------------------|
|home        | вернуться в главное меню|
|q           | выход|