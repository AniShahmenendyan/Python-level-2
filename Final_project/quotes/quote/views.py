from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from quote.forms import QuoteSearchForm, QuoteCreateForm
from quote.models import Quote, Author, Tag
from django.contrib import messages

def home(request):
    return render(request, 'home.html')


class QuoteListView(ListView):
    model = Quote
    paginate_by = 5

    # template_name = 'quote_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = QuoteSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        form = QuoteSearchForm(self.request.GET)
        if form.is_valid():
            text = form.cleaned_data['text']
            author_id = form.cleaned_data['author']
            tag = form.cleaned_data['tag']

            if text:
                qs = qs.filter(text__icontains=text)

            if author_id:
                qs = qs.filter(author_id=author_id)

            if tag:
                qs = qs.filter(tag=tag)


        return qs


class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'quote/quote_detail.html'


class QuoteMixin:
    model = Quote
    fields = '__all__'
    success_url = reverse_lazy('quote:quotes')


class QuoteCreateView(QuoteMixin, CreateView):
    fields = ('text', 'tag')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author.id = self.request.user.pk
        self.object.save()
        return super().form_valid(form)


@login_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            author = request.user.first_name
            text = form.cleaned_data['text']
            name = f'{request.user.first_name} {request.user.last_name}'
            author, _ = Author.objects.get_or_create(user_id=request.user.pk,
                                                     name=name)
            new_quote = Quote.objects.create(text=text, author=author)
            for tag in form.cleaned_data['tag']:
                tag = Tag.objects.filter(name=tag).first()
                new_quote.tag.add(tag)
                new_quote.save()
            return HttpResponseRedirect(reverse_lazy('quote:quotes'))

        else:
            messages.error(request, 'Something went wrong')
    else:
        form = QuoteCreateForm()
        return render(request, 'quote/quote_form.html', {'form': form})




class QuoteUpdateView(LoginRequiredMixin,QuoteMixin, UpdateView):
    fields = ('text', 'author', 'tag')
    template_name = 'quote/quote_update_form.html'

    def get_queryset(self):
        return Quote.objects.filter(author__user_id=self.request.user.pk)


class QuoteDeleteView(LoginRequiredMixin, QuoteMixin, DeleteView):

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()



    def get_queryset(self):
        return Quote.objects.filter(author__user_id=self.request.user.pk)
