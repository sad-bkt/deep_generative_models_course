# ДЗ 3. Sampling в латентном пространстве StyleGAN



Для ДЗ надо взять **4-6 персонажей**, в наборе должны быть хотя бы 2 фото с разными поворотами головы помимо смотрящих прямо

[Ссылка на код](https://www.kaggle.com/code/anastasiiasemina1/stylegan-hw)

## Подготовительный этап
- Кадрировать изображения для соответствия данным из трейна, блок (Align images)
- Найти проекции изображений в пространстве StyleGAN, методами из ноутбука (советую добавить scheduler, поиграться с весами лоссов или использовать свои, если они улучшают качество)
- Результат представить как таблицу оригинал и проекция, написать каким образом были получены, encoder, оптимизация, лоссы и тд


![Table1](imgs/table1.jpg)

| Оригинал                                                                                                                                                     | Проекция1                                                         | Проекция2                                                              | Проекция3                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | num_steps = 150 <br> initial_lr = 0.05 <br> w_avg_samples = 10000 | num_steps = 300 <br> initial_lr = 0.1 <br> w_avg_samples = 10000       | Encoder&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| ![0.jpg](imgs%2F0.jpg)                                                                                                                                       | ![EmmaStone_0.jpg](imgs%2FEmmaStone_0.jpg)                        | ![EmmaStone_0 (1).jpg](imgs%2FEmmaStone_0%20%281%29.jpg)               | ![EmmaStone_encoder.jpg](imgs%2FEmmaStone_encoder.jpg)                    |
| ![0 (1).jpg](imgs%2F0%20%281%29.jpg)                                                                                                                         | ![AnyaTaylorJoy_0.jpg](imgs%2FAnyaTaylorJoy_0.jpg)                | ![AnyaTaylorJoy_0 (1).jpg](imgs%2FAnyaTaylorJoy_0%20%281%29.jpg)       | ![AnyaTaylorJoy_encoder.jpg](imgs%2FAnyaTaylorJoy_encoder.jpg)            |
| ![0 (2).jpg](imgs%2F0%20%282%29.jpg)                                                                                                                         | ![KeanuReeves_0.jpg](imgs%2FKeanuReeves_0.jpg)                    | ![KeanuReeves_0 (1).jpg](imgs%2FKeanuReeves_0%20%281%29.jpg)           | ![KeanuReeves_encoder.jpg](imgs%2FKeanuReeves_encoder.jpg)                |
| ![0 (3).jpg](imgs%2F0%20%283%29.jpg)                                                                                                                         | ![TimotheeChalamet_0.jpg](imgs%2FTimotheeChalamet_0.jpg)          | ![TimotheeChalamet_0 (1).jpg](imgs%2FTimotheeChalamet_0%20%281%29.jpg) | ![TimotheeChalamet_encoder.jpg](imgs%2FTimotheeChalamet_encoder.jpg)      |



## Style transfer


![Style transfer ](imgs/style.jpg)
- Изменяется цвет, свет, текстура, но человек должен остаться прежним
- Пробуем самый простой метод для трансфера стиля с одного лица на другой с помощью смешивания векторов, хватит трех стилей (еще три изображения помимо базовых, не забывайте, что стили тоже надо спроецировать в латентное пространство)
- Результат в виде таблицы с пояснениями, какие брали индексы из вектора W+

```
psi=0.1
индексы стиля [0, 8]
```

| Оригинал                             | Стиль1                                                                         | Стиль2                                                                         | Стиль3                                                                         |
|--------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
|                                      | ![style0.jpg](imgs%2Fstyle0.jpg)                                               | ![style1.jpg](imgs%2Fstyle1.jpg)                                               | ![style2.jpg](imgs%2Fstyle2.jpg)                                               |
| ![0.jpg](imgs%2F0.jpg)               | ![EmmaStone_with_style_0.jpg](imgs%2FEmmaStone_with_style_0.jpg)               | ![EmmaStone_with_style_1.jpg](imgs%2FEmmaStone_with_style_1.jpg)               | ![EmmaStone_with_style_2.jpg](imgs%2FEmmaStone_with_style_2.jpg)               |
| ![0 (1).jpg](imgs%2F0%20%281%29.jpg) | ![AnyaTaylorJoy_with_style_1.jpg](imgs%2FAnyaTaylorJoy_with_style_0.jpg)       | ![AnyaTaylorJoy_with_style_1.jpg](imgs%2FAnyaTaylorJoy_with_style_1.jpg)       | ![AnyaTaylorJoy_with_style_2.jpg](imgs%2FAnyaTaylorJoy_with_style_2.jpg)       |
| ![0 (2).jpg](imgs%2F0%20%282%29.jpg) | ![KeanuReeves_with_style_0.jpg](imgs%2FKeanuReeves_with_style_0.jpg)           | ![KeanuReeves_with_style_1.jpg](imgs%2FKeanuReeves_with_style_1.jpg)           | ![KeanuReeves_with_style_2.jpg](imgs%2FKeanuReeves_with_style_2.jpg)           |
| ![0 (3).jpg](imgs%2F0%20%283%29.jpg) | ![TimotheeChalamet_with_style_0.jpg](imgs%2FTimotheeChalamet_with_style_0.jpg) | ![TimotheeChalamet_with_style_1.jpg](imgs%2FTimotheeChalamet_with_style_1.jpg) | ![TimotheeChalamet_with_style_2.jpg](imgs%2FTimotheeChalamet_with_style_2.jpg) |


## Expression Transfer
![Expression Transfer](imgs/expression.jpg)
- Три любые эмоции по аналогии с предыдущими пунктами
- Результат в таблицу

```
psi=0.6
индексы стиля [0, 17]
```

| Оригинал                             | Улыбка                                                           | Возраст                                                      | Поворот                                                        |
|--------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------|
| ![0.jpg](imgs%2F0.jpg)               | ![EmmaStone_smile.jpg](imgs%2FEmmaStone_smile.jpg)               | ![EmmaStone_age.jpg](imgs%2FEmmaStone_age.jpg)               | ![EmmaStone_pose.jpg](imgs%2FEmmaStone_pose.jpg)               |
| ![0 (1).jpg](imgs%2F0%20%281%29.jpg) | ![AnyaTaylorJoy_smile.jpg](imgs%2FAnyaTaylorJoy_smile.jpg)       | ![AnyaTaylorJoy_age.jpg](imgs%2FAnyaTaylorJoy_age.jpg)       | ![AnyaTaylorJoy_pose.jpg](imgs%2FAnyaTaylorJoy_pose.jpg)       |
| ![0 (2).jpg](imgs%2F0%20%282%29.jpg) | ![KeanuReeves_smile.jpg](imgs%2FKeanuReeves_smile.jpg)           | ![KeanuReeves_age.jpg](imgs%2FKeanuReeves_age.jpg)           | ![KeanuReeves_pose.jpg](imgs%2FKeanuReeves_pose.jpg)           |
| ![0 (3).jpg](imgs%2F0%20%283%29.jpg) | ![TimotheeChalamet_smile.jpg](imgs%2FTimotheeChalamet_smile.jpg) | ![TimotheeChalamet_age.jpg](imgs%2FTimotheeChalamet_age.jpg) | ![TimotheeChalamet_pose.jpg](imgs%2FTimotheeChalamet_pose.jpg) |


## Face swap
- В блоке Homework в ноутбуке, уже написан Arcface лосс (веса модели по ссылке) добавить его в пайплайн оптимизации и попробовать с помощью оптимизации градиента перенести личность с одной фотографии на другую, сохраняя при этом угол поворота и цвет для исходного лица.
- Сделать табличку пересадки лиц каждого с каждым

