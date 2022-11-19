### Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы. Обязательно наличие внешнего хранилища информации в виде или текстового файла или файла .json.

# Информационная система по работе с учениками школы:

## Архитектура информационной системы:
## 1. Модуль графического интерфейса взаимодействия с пользователем
## 2. Модуль обработки информации
## 3. База данных учеников

![img_1](https://user-images.githubusercontent.com/107861149/197413870-1ddc3993-b68b-4477-a7af-548aa7d63266.jpg)

Наполнение базы данных по ученикам (файл .json):
1. ФИО
2. Дата рождения
3. Класс
4. ФИО классного руководителя
5. Адрес
6. Номер телефона родителя
7. Средняя успеваемость

Графичкский интерфейс выполнен через библиотеку easygui.

![img_2](https://user-images.githubusercontent.com/107861149/197413940-6fb375b6-fcf8-45a5-ae24-cc87611ff732.jpg)

Функции информационной системы:
1. Добавить ученика в БД

![img_3](https://user-images.githubusercontent.com/107861149/197484207-30722e51-9fde-4edc-9fb7-fdb1568c6577.jpg)
![img_4](https://user-images.githubusercontent.com/107861149/197484226-cc1399a7-1566-426d-aae0-65dca2bb22f7.jpg)

2. Удалить ученика из БД

![img_5](https://user-images.githubusercontent.com/107861149/197414139-f0aa1807-3858-4a09-822c-a6a93e024480.jpg)

3. Редактировать данные ученика в БД

![img_6](https://user-images.githubusercontent.com/107861149/197414188-01ba2c69-1f85-4b24-9635-9e84448ddec4.jpg)
![img_7](https://user-images.githubusercontent.com/107861149/197414215-cb065699-c544-433d-9584-1534cba77759.jpg)

4. Вывести список учеников конкретного класса

![img_8](https://user-images.githubusercontent.com/107861149/197414228-d08bdd95-e9e5-4b59-93a3-739c95961914.jpg)
![img_9](https://user-images.githubusercontent.com/107861149/197414235-6751498e-6cb7-4102-870d-dc77cc0eefcf.jpg)
![img_10](https://user-images.githubusercontent.com/107861149/197414238-2de413af-8fb8-4290-8804-bbe920be7d64.jpg)
![img_11](https://user-images.githubusercontent.com/107861149/197414242-3b3cc26f-7631-4bc2-b3af-d3b1f76f96e1.jpg)

5. Вывести информацию одного ученика по его фамилии

![img_12](https://user-images.githubusercontent.com/107861149/197414250-4af47ba0-7d58-4017-8f16-0d3fd28b2b84.jpg)
![img_13](https://user-images.githubusercontent.com/107861149/197414254-be03056e-b5ad-4c23-83d3-9eee92a9eec7.jpg)

6. Вывести ФИО классного раководителя по фамилии ученика

![img_14](https://user-images.githubusercontent.com/107861149/197414264-7dea47e1-3211-441d-b433-47fc88128def.jpg)
![img_15](https://user-images.githubusercontent.com/107861149/197414267-db4a5e50-f6d3-4d44-8556-e21ca364e9eb.jpg)

7. Вывести номер телефона родителя по фамилии ученика

![img_16](https://user-images.githubusercontent.com/107861149/197414271-5697369c-eeba-4168-a14a-a73051a6c5c8.jpg)
![img_17](https://user-images.githubusercontent.com/107861149/197414272-1a507cfe-5088-4d88-bee1-ab10a36b68f2.jpg)

8. Вывести список именинников месяца по школе (можно вводить как численное значение месяца, так и название)

![img_18](https://user-images.githubusercontent.com/107861149/197414282-8c0ea667-f773-4822-bc59-81da35d81222.jpg)
![img_19](https://user-images.githubusercontent.com/107861149/197414284-3b9a8068-e672-4774-935a-a65ea31263f7.jpg)

9. Вывести списки отличников, хорошистов и ударников школы

![img_21](https://user-images.githubusercontent.com/107861149/197414288-715d9a60-5d63-40c5-ae50-fd3ad4d674ec.jpg)
![img_22](https://user-images.githubusercontent.com/107861149/197414289-b5a9d8bf-c199-4b54-aa2d-51a44db86f06.jpg)


Work team:
1. Корчагин Дмитрий - control.py; main.py
2. Соловьев Ярослав - control.py; main.py
3. Нестерова Дарья - student_data_base.json; README.md