from django.shortcuts import render
from django.core.mail import send_mail
from BigMacIndexes.forms import CountryGraphForm, ContactUsForm
from BigMacIndexes.models import BigMacIndexes
import plotly.graph_objects as go


def home(request):
    return render(request, "home.html", {})


def team(request):
    return render(request, "team.html", {})


def calculator(request):
    if request.method == "POST":
        form = CountryGraphForm(request.POST)
        if form.is_valid():
            country1 = form.cleaned_data['country1']
            country2 = form.cleaned_data['country2']
        posted = True;
    else:
        form = CountryGraphForm()
        country1 = "Argentina"
        country2 = "Argentina"
        posted = False;

    i1 = BigMacIndexes.objects.filter(date="2020-07-01").filter(name=country1)[0].USD_raw
    i2 = BigMacIndexes.objects.filter(date="2020-07-01").filter(name=country2)[0].USD_raw
    result = (i1/i2 - 1) * 100
    return render(request, "calculator.html",
                  {'form': form, 'result': result, 'posted': posted, 'country1': country1, 'country2': country2})


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                'Contact Us',
                request.POST['text'],
                request.POST['email'],
                ['info@burgernomists.com'],
                fail_silently=False,
            )
            feedback = 'Mail Sent'

    else:
        form = ContactUsForm()
        feedback = ''

    return render(request, "contact_us.html", {'form': form, 'feedback': feedback})


def table(request):
    filter_by_type = request.GET.get('filter_by', '2020-07-01')
    order_by_type = request.GET.get('order_by', '-USD_raw')
    table_data = BigMacIndexes.objects.all().filter(date=filter_by_type).order_by(order_by_type)
    base_price = table_data.filter(name="United States")[0].USD_raw
    return render(request, "table.html", {'table_data': table_data, 'base_price': base_price,
                                          'f': filter_by_type, 'o': order_by_type})


def graph(request):
    if request.method == "POST":
        form = CountryGraphForm(request.POST)
        if form.is_valid():
            country1 = form.cleaned_data['country1']
            country2 = form.cleaned_data['country2']
    else:
        form = CountryGraphForm()
        country1 = "Argentina"
        country2 = "Argentina"

    selected_countries = [country1, country2]
    d1 = [i[0] for i in BigMacIndexes.objects.filter(name__in=selected_countries).values_list("name")]
    d2 = [i[0] for i in BigMacIndexes.objects.filter(name__in=selected_countries).values_list("date")]
    d3 = [i[0] for i in BigMacIndexes.objects.filter(name__in=selected_countries).values_list("USD_raw")]
    base = BigMacIndexes.objects.filter(name="United States")
    d3 = [val / base.filter(date=d2[idx])[0].USD_raw for idx, val in enumerate(d3)]
    trace = go.Scatter3d(x=d1, y=d2, z=d3, mode='markers',
                         marker=dict(
                             line=dict(width=0),
                         ), )
    layout = go.Layout(scene=dict(
        xaxis=dict(
            title='Country',
        ),
        yaxis=dict(
            title='Date'
        ),
        zaxis=dict(
            title='Big Mac Index'
        ),
    )
    )

    fig = go.Figure(layout=layout, data=[trace])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

    plot_html = fig.to_html()

    return render(request, "graph.html", context={'plot': plot_html, 'form': form})
