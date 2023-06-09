# counter_using_postgresql
Didtributer databases, Task 1, Counter using PostgreSQL

1) Lost update алгоритм реалізований у файлі lost_update.py і як результат виконання повернув значення counter 10264 за майже 79 секунд.

![Lost update algorithm](results/counter_postgresql_lost_update.png)

2) In place алгоритм реалізований у файлі inplace_update.py і як результат повернув значення counter 100001 (значення повністю правильне так як початково в базу записується значення counter = 1) за трохи більше ніж 137 секунд. Виконалося досить швидко так як інкрементація counter відбувалася безпосередньо на базі даних на додачу без запиту діставання інформації безпосередньо у виконувану программу.

![Inplace algorithm](results/counter_postgres_inplace.png)

3) Row level locking алгоритм реалізований в файлі row_level_locking.py і як результат виконання повернув корректне значення 100001 за майже 185 секунд. Реалізація дуже схожа на lost update але значно довше виконується через те що при кожному селекті рядок блокується до оновлення данних.

![Row level locking](results/counter_postgresql_row_level_locking.png)

4) Optimistic concurrrency control алгоритм реалізавний у файлі optimistic_concurrency_control.py і повернув корректний результат 100001 за більш ніж 607 секунд. Такий великий час виконання пов'язаний з селектом і оновленням відразу значень counter і version.

![Optimistic concurrency algorithm](results/counter_postgresql_optimistic_cuncurrency_control.png)


В цілому чистий розподілениий підхід реалізований в першому алгоритмі, але рівень втрати данних дуже високий. Інші 3 алгоритми реалізовують за розподулених звертань послідовну зміну значення counter для корректності інформації. Далі вже вибір конкретного алгоритму для реалізації на конкретній інфраструктурі в залежності від можливостей цієї архітектури і завдань.
