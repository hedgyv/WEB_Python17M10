from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from bson import ObjectId
from .models import Quote, Author
from .forms import QuoteForm


from .utils import get_mongodb

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    q_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes' : q_on_page})

def author_detail(request, author_id):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(author_id)})
    print(author)
    return render(request, 'quotes/author_detail.html', {'author': author})

def new_quote_form(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data['quote']
            author_name = form.cleaned_data['author']
            birthday = form.cleaned_data['birthday']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            
            db = get_mongodb()
            
            db.authors.insert_one({
                'fullname' : author_name,
                'born_date' : birthday,
                'born_location' : location,
                'description'  : description
            })
            
            
            new_author =  db.authors.find_one({'fullname': author_name})
            if new_author:
                db.quotes.insert_one({
                'quote' : quote_text,
                'tags' : '',
                'author' : ObjectId(new_author['_id'])
                })
            
            # try:
            #     author = Author.objects.get(name=author_name)
            # except Author.DoesNotExist:
            #     # Если автора с таким именем нет, создаем нового автора
            #     author = Author.objects.create(name=author_name)
            

            # Создание новой цитаты с ссылкой на автора
            # new_quote = Quote.objects.create(quote=quote_text, author=author)
            return redirect(to="quotes:root")
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})
