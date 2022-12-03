from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'home/index.html', {
        'page_title': 'Головна'
    })


def about(request):
    return render(request, 'home/about.html', {
        'page_title': 'Про сайт'
    })


def news(request):
    return render(request, 'home/news.html', {
        'page_title': 'Новини'
    })


def contacts(request):
    admin_email = 'uaa2uaa@gmail.com'
    if request.method == 'GET':
        return render(request, 'home/contacts.html', {
            'page_title': "Контакти"
        })
    elif request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        #
        subject_in = 'Повідомлення від користувача!'
        body_in = f"""
                <h1>Повідомлення від користувача!</h1>
                <hr />
                <h2>
                   E-mail користувача:
                    <span style="color: darkcyan">
                        {email}
                    </span>
                </h2>
                <h2>
                   Повідомлення від користувача:
                    <span style="color: gray">
                        {message}
                    </span>
                </h2>
            """
        #
        subject_out = 'Повідомлення про Ваше звернення в OnlineShop!'
        body_out = f"""
                 <hr />   
                 <h1>Повідомлення про Ваше звернення в OnlineShop!</h1>
                 <hr />
                 <h2>
                    Ми отримали Ваше повідмлення з E-mail: <br />
                    <span style="color: darkcyan">
                        {email}
                    </span>
                 </h2>
                 <h2 style="color: gray">
                    Наш менеджер з Вами зв'яжеться протягом найближчої години!
                </h2>
                <hr />
          """

        success = send_mail(subject_in, '', 'OnlineShop', [admin_email], fail_silently=False, html_message=body_in)
        feedback = send_mail(subject_out, '', 'OnlineShop', [email], fail_silently=False, html_message=body_out)
        if success:
            color = 'red'
            return render(request, 'home/report.html', {
                'page_title': "Звіт про отримання звернення!",
                'email': email,
                'result_color': color,
                'status': 1
            })
        else:
            color = 'red'
            return render(request, 'home/report.html', {
                'page_title': "Помилка відправлення звернення!",
                'result_color': color,
                'status': 2
            })

