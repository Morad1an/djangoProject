from django.db.models import ExpressionWrapper, F, IntegerField
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Quote
import random


def home(request):
    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        action = request.POST.get('action')
        quote = Quote.objects.get(id=quote_id)
        if action == 'like':
            quote.likes += 1
        elif action == 'dislike':
            quote.dislikes += 1
        quote.save()
        return redirect('home')

    quotes = Quote.objects.all()
    if quotes:
        total_weight = sum(quote.weight for quote in quotes)
        weights = [quote.weight / total_weight for quote in quotes]
        selected_quote = random.choices(quotes, weights=weights, k=1)[0]
        selected_quote.views += 1
        selected_quote.save()
        return render(request, 'main/index.html', {'quote': selected_quote})
    return render(request, 'main/index.html', {'quote': None})


def add(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        source = request.POST.get('source')
        try:
            weight = float(request.POST.get('weight', 1.0))
        except ValueError:
            messages.error(request, 'Вес должен быть числом!')
            return redirect('add')

        if Quote.objects.filter(text=text).exists():
            messages.error(request, 'Эта цитата уже существует!')
            return redirect('add')

        if Quote.objects.filter(source=source).count() >= 3:
            messages.error(request,
                           'Нельзя добавить больше трех цитат от одного источника!')
            return redirect('add')

        if not (0 <= weight <= 10):
            messages.error(request, 'Вес должен быть от 0 до 10!')
            return redirect('add')

        Quote.objects.create(text=text, source=source, weight=weight)
        messages.success(request, 'Цитата успешно добавлена!')
        return redirect('home')

    return render(request, 'main/add.html')


def top(request):
    top_quotes = Quote.objects.annotate(
        popularity=ExpressionWrapper(F('likes') - F('dislikes'),
                                     output_field=IntegerField())
    ).order_by('-popularity')[:10]
    return render(request, 'main/top.html', {'quotes': top_quotes})
