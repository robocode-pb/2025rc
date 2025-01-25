
### 1. **Змінні**
Змінні використовуються для зберігання значень різних типів даних.
```csharp
int x = 5;
float y = 3.14f;
string name = "John";
```
- `int` — ціле число.
- `float` — число з плаваючою комою.
- `string` — рядок.

### 2. **Умовний оператор if**
Цей оператор дозволяє виконувати певний блок коду, якщо умова істинна.
```csharp
if (x > 10)
{
    Console.WriteLine("x більше 10");
}
else
{
    Console.WriteLine("x менше або рівне 10");
}
```

### 3. **Цикл for**
Цикл `for` дозволяє повторювати блок коду певну кількість разів.
```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```
Цей цикл виведе числа від 0 до 4.

### 4. **Цикл while**
Цикл `while` продовжує виконувати код, поки умова є істинною.
```csharp
int counter = 0;
while (counter < 5)
{
    Console.WriteLine(counter);
    counter++;
}
```

### 5. **Масиви**
Масиви дозволяють зберігати кілька значень одного типу.
```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
Console.WriteLine(numbers[2]); // Виведе 3
```

### 6. **Методи**
Методи використовуються для виконання певних операцій, які можуть бути викликані з іншого місця в програмі.
```csharp
void Greet(string name)
{
    Console.WriteLine($"Привіт, {name}!");
}

Greet("Микола");
```

### 7. **Конструктори класів**
Конструктор — це спеціальний метод, який викликається при створенні нового об'єкта класу.
```csharp
class Person
{
    public string Name;
    public int Age;

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

Person p = new Person("Андрій", 30);
Console.WriteLine(p.Name);  // Виведе "Андрій"
```

### 8. **Оператори порівняння**
Ці оператори використовуються для порівняння значень.
```csharp
int a = 10;
int b = 20;

if (a == b)
{
    Console.WriteLine("a дорівнює b");
}
else if (a > b)
{
    Console.WriteLine("a більше b");
}
else
{
    Console.WriteLine("a менше b");
}
```

### 9. **Switch**
Оператор `switch` дозволяє вибирати блок коду залежно від значення змінної.
```csharp
int day = 3;
switch (day)
{
    case 1:
        Console.WriteLine("Понеділок");
        break;
    case 2:
        Console.WriteLine("Вівторок");
        break;
    case 3:
        Console.WriteLine("Середа");
        break;
    default:
        Console.WriteLine("Невірний день");
        break;
}
```

### 10. **Підготовка до обробки виключень (try-catch)**
Це дозволяє обробляти помилки в програмі без її аварійного завершення.
```csharp
try
{
    int result = 10 / 0; // Це спричинить помилку ділення на нуль
}
catch (DivideByZeroException)
{
    Console.WriteLine("Не можна ділити на нуль!");
}
```

---

Ось 10 простих конструкцій програмування для Unity на C# з поясненнями, які допоможуть вам почати роботу в цьому середовищі:

### 1. **MonoBehaviour: базовий клас для скриптів**
Всі скрипти в Unity зазвичай успадковуються від класу `MonoBehaviour`. Це дозволяє використовувати спеціальні методи Unity для керування поведінкою об'єкта.
```csharp
using UnityEngine;

public class MyScript : MonoBehaviour
{
    void Start()
    {
        // Цей метод викликається один раз при запуску гри
        Debug.Log("Гра почалася!");
    }

    void Update()
    {
        // Цей метод викликається кожен кадр
        transform.Rotate(0, 1, 0);
    }
}
```
- `Start()` викликається один раз на початку.
- `Update()` викликається кожен кадр.

### 2. **Переміщення об'єкта**
Ви можете змінювати позицію об'єкта в світі за допомогою `transform`.
```csharp
using UnityEngine;

public class MoveObject : MonoBehaviour
{
    void Update()
    {
        // Переміщаємо об'єкт вправо по осі X
        transform.Translate(Vector3.right * Time.deltaTime);
    }
}
```
- `Time.deltaTime` використовується для того, щоб об'єкт рухався з однаковою швидкістю незалежно від частоти кадрів.

### 3. **Використання фізики (Rigidbody)**
Якщо об'єкт має фізику, ви можете використовувати компонент `Rigidbody` для застосування сил або руху.
```csharp
using UnityEngine;

public class AddForce : MonoBehaviour
{
    Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.AddForce(Vector3.up * 5, ForceMode.Impulse);
        }
    }
}
```
- `AddForce` додає силу до об'єкта, викликаючи рух.

### 4. **Обробка введення користувача (Input)**
Unity надає потужний інструмент для обробки вводу з клавіатури, миші чи геймпада.
```csharp
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        transform.Translate(new Vector3(horizontal, 0, vertical) * Time.deltaTime);
    }
}
```
- `Input.GetAxis` дозволяє отримати введення по осях для руху (стрілки або WASD).

### 5. **Використання подій для обробки колізій (OnCollision)**
Unity дозволяє визначити поведінку об'єктів при зіткненнях за допомогою методів `OnCollisionEnter`, `OnCollisionStay`, `OnCollisionExit`.
```csharp
using UnityEngine;

public class CollisionExample : MonoBehaviour
{
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Player"))
        {
            Debug.Log("Сталося зіткнення з гравцем!");
        }
    }
}
```
- `OnCollisionEnter` викликається, коли відбувається перше зіткнення.

### 6. **Визначення тегів**
В Unity можна призначити тег об'єкту і використовувати його для порівняння.
```csharp
using UnityEngine;

public class CheckTag : MonoBehaviour
{
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Enemy"))
        {
            Debug.Log("Ви зіткнулися з ворогом!");
        }
    }
}
```
- `CompareTag` дозволяє перевіряти, чи має об'єкт певний тег.

### 7. **Використання анімацій**
Анімації можна керувати через компонент `Animator`.
```csharp
using UnityEngine;

public class AnimationControl : MonoBehaviour
{
    Animator anim;

    void Start()
    {
        anim = GetComponent<Animator>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.W))
        {
            anim.SetTrigger("Walk");
        }
    }
}
```
- `anim.SetTrigger("Walk")` активує анімацію ходьби, якщо вона задана в Animator.

### 8. **Завантаження сцени**
Для перемикання між сценами в Unity використовується клас `SceneManager`.
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneSwitcher : MonoBehaviour
{
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Return))
        {
            SceneManager.LoadScene("NextScene");
        }
    }
}
```
- `SceneManager.LoadScene` завантажує нову сцену.

### 9. **Керування камерою (Camera)**
В Unity ви можете змінювати положення камери для створення ефектів або відстеження об'єктів.
```csharp
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public Transform player;

    void Update()
    {
        transform.position = new Vector3(player.position.x, transform.position.y, player.position.z - 10);
    }
}
```
- Камера слідує за об'єктом (наприклад, гравцем) з певним відстанню.

### 10. **Просте спаунування об'єктів**
Щоб створити об'єкт в грі, можна використати метод `Instantiate`.
```csharp
using UnityEngine;

public class ObjectSpawner : MonoBehaviour
{
    public GameObject prefab;

    void Start()
    {
        Instantiate(prefab, new Vector3(0, 1, 0), Quaternion.identity);
    }
}
```
- `Instantiate` створює новий екземпляр об'єкта з префабом.

