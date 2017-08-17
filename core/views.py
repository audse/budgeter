from django.shortcuts import render, redirect
from .models import Total, Entry, Category
from chartit import PivotDataPool, PivotChart
from django.db.models import Avg

# Create your views here.


	# budgetdata = DataPool(series = [{'options': {
 #    				'source': Entry.objects.filter(positive=False)},
 #    				'terms': ['date','amount']
 #    			}
 #    		])

	# chart = Chart(
 #            datasource = budgetdata,
 #            series_options = [{'options':{
 #            	'type': 'line',
 #            	'stacking': False},
 #            	'terms': {'date': ['amount']}
 #            }],
 #            chart_options = {'title': {'text': 'Expenses'}, 'xAxis': {'title': {'text': 'Month number'}}}
 #            )

def home_page(request):
	total = Total.objects.all().first()
	entries = Entry.objects.all().order_by('-date')
	categories = Category.objects.all()

	chartdata = PivotDataPool(series=[{
            'options': {
                'source': Entry.objects.filter(positive=False),
                'categories': ['category'],
                'legend_by': 'category',
                'top_n_per_cat': 8,
            },
            'terms': {
                'avg_amount': Avg('amount'),
            }
        }]
    )

	chart = PivotChart(datasource=chartdata, series_options=[{'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_amount']
        }],
        chart_options={
            'title': {
                'text': 'Average Spending by Category'
            },
            'xAxis': {
                'title': {
                    'text': 'Month'
                }
            }
        }
    )

	return render(request, 'home_page.html', {'total':total, 'entries':entries, 'categories':categories, 'chart':chart})

def add_entry(request):
	positive = request.POST.get("positive")
	amount = request.POST.get("amount")
	category = request.POST.get("category")
	notes = request.POST.get("notes")

	if positive == "yes":
		positive = True
	else:
		positive = False

	amount = float(amount)
	category = Category.objects.get(pk=category)

	entry = Entry.objects.create(amount=amount, category=category.name, notes=notes, positive=positive)
	total = Total.objects.all().first()
	if positive:
		total.amount += entry.amount
		total.save()
	else:
		total.amount -= entry.amount
		total.save()

	return redirect(home_page)

def about_page(request):
	return render(request, 'about_page.html')









