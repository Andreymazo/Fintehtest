Задача
·         Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
·         Django Модель Item с полями (name, description, price)
·         API с двумя методами:
·         GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
·         GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
Доп. Задания: 
·         Запуск используя Docker
·         Использование environment variables
·         Просмотр Django Моделей в Django Admin панели
·         Запуск приложения на удаленном сервере, доступном для тестирования
·         Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
·         Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
·         Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
·         Реализовать не Stripe Session, а Stripe Payment Intent.
Критерии оценки
Работоспособность
Чистота и структура куда
Гибкость и масштабируемость
Безопасность и обработка ошибок
Доп. плюсы за использование улучшающих архитектуру проекта, его читаемость, расширяемость и тестируемость паттернов и шаблонов проектирования,, использование более удобных библиотек и технологий, позволяющих ускорить разработку и сделать проект лучше.
 Также доп плюсы:
- скрипт или некий функционал для наполнения БД тестовыми данными
- типизация кода, докстринги
- написание readme по всем нюансам и способам запуска

<<<<<<< Updated upstream
[Screencast from 31.08.2024 12:51:14.webm](https://github.com/user-attachments/assets/37991401-da11-49cd-b03f-829fa595e74b)


=======
<!-- 
<body>
    <div class="container">
    <h1>Place an order here</h1>
     <button type="button" class="btn btn-lg btn-primary" id="checkout-button">Checkout</button>
    </div>
     <script type="text/javascript">
     // Create an instance of the Stripe object with your publishable API key
     var stripe = Stripe('pk_test_51IvESHSEJXkgN9eEfXq71htC7r3iPvFiOKqvRaBDNqxOVsDoN1keJQz4Ry8xWDQLYdS6MXC1CvHq4YD7jqwF8Cms00n5aUeFev');
     var checkoutButton = document.getElementById('checkout-button');
    
     checkoutButton.addEventListener('click', function() {
     // Create a new Checkout Session using the server-side endpoint you
     // created in step 3.
     fetch('/create-checkout-session/', {
     method: 'POST',
     })
     .then(function(response) {
     return response.json();
     })
     .then(function(session) {
     return stripe.redirectToCheckout({ sessionId: session.id });
     })
     .then(function(result) {
     // If `redirectToCheckout` fails due to a browser or network
     // error, you should display the localized error message to your
     // customer using `error.message`.
     if (result.error) {
     alert(result.error.message);
     }
     })
     .catch(function(error) {
     console.error('Error:', error);
     });
     });
     </script>
     </body>
    </html> -->
    
<!-- 
    <script type="text/javascript">
    
    
    let stripe = Stripe('pk_test_51PsjVH07pGox0kT4XEK6FPDiOOBKVaWr7KyvplADcTjJQDqMywkDywwvL8yPfCJ8f3XHYUWs5FgoUhtKEs4WFlBb00yZu0QbXA', {
    locale: 'ru'
                                                            });
    let checkoutButton = document.getElementById("checkout-button");
    checkoutButton.addEventListener("click", function () {

        fetch("{% url 'fintehtest:get_id_on_template' item.id %}", {
            method: "POST",
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
            
            .then(function (response) {
                return response.json();
            })
            .then(data => {
	    console.log(data);
            })
            .then(function (session) {
                stripe.redirectToCheckout({ sessionId: session.sessionId })

            })
            .then(function (result) {
                if (result.error) {
                    alert(result.error.message);
                }
            })
            .catch(function (error) {
                console.error("Error:", error);
            });
    });
    //  result = stripe.redirectToCheckout(session_id, line_items, {"mode":"payment"})
    //  console.log('result', result)
    //  document.getElementById("clickMe").onclick = stripe.redirectToCheckout({sessionId: session.sessionId}); -->
<!-- </script> -->


<!-- 







<script src="https://polyfill.io/v3/polyfill.min.js?version=3.52.1&features=fetch"></script>
<script src="https://js.stripe.com/v3/"></script>

<title>Buy cool new product</title>
<script src="https://js.stripe.com/v3/"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

<body>

    <form method="post">
        {% csrf_token %}
        {{form.as_p}}
        <p>
           item {{item}} 
        </p>
        <p>
            session_id  {{session_id}} 
        </p>
        <button type="submit" id="checkout-button">Buy</button>
    
    </form>

     <script type="text/javascript">
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let stripe = Stripe("{{ 'pk_test_51IvESHSEJXkgN9eEfXq71htC7r3iPvFiOKqvRaBDNqxOVsDoN1keJQz4Ry8xWDQLYdS6MXC1CvHq4YD7jqwF8Cms00n5aUeFev' }}");
        let checkoutButton = document.getElementById("checkout-button");
        checkoutButton.addEventListener("click", function () {
            fetch("{% url 'fintehtest:get_id_on_template' item.id%}", {
                method: "POST",
                headers: {
                    'X-CSRFToken': csrftoken
                }
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (session) {
                    return stripe.redirectToCheckout({sessionId: session.id});
                })
                .then(function (result) {
                    if (result.error) {
                        alert(result.error.message);
                    }
                })
                .catch(function (error) {
                    console.error("Error:", error);
                });
        });
    </script> -->
>>>>>>> Stashed changes
