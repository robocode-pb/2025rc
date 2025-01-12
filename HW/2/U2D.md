Пригадайте, що таке [корутина](https://itproger.com/ua/spravka/unity/startcoroutine).

---

> Основні характеристики методу `StartCoroutine( назваФункції() )`
- Асинхронне виконання: Дозволяє розбивати виконання коду на частини, які виконуються через певні інтервали часу.
- Зручність управління часом: Використовується для виконання операцій із затримкою, наприклад, очікування кількох секунд перед виконанням наступного кроку.
- Робота з `IEnumerator`: Метод запускає функцію, яка повертає IEnumerator, що є основою для роботи з корутинами.

---

> Що робить наступний скрипт? Чи можна його спростити?

``` cs

// JewelSpawn.cs
using UnityEngine;
using System.Collections;

public class JewelSpawn : MonoBehaviour
{
  public GameObject jewelPrefab;   // Префаб коштовності, яка буде створюватися
  public float spawnInterval = 1f; // Інтервал між створенням коштовностей

  void Start(){
    // Запускаємо корутину для створення коштовностей
    StartCoroutine(SpawnJewels());
  }

  IEnumerator SpawnJewels(){
    while (true){
      // Визначаємо межі екрана у світових координатах
      Vector2 screenBounds = Camera.main.ScreenToWorldPoint(
        new Vector2(Screen.width, Screen.height)
      );

      // Створюємо коштовність у випадковій позиції
      Instantiate(jewelPrefab,
        new Vector2(
          Random.Range(-screenBounds.x, screenBounds.x),
          Random.Range(-screenBounds.y, screenBounds.y)
        ),
        Quaternion.identity);

      // Очікуємо вказаний інтервал перед створенням наступної коштовності
      yield return new WaitForSeconds(spawnInterval);
    }
  }

}


```