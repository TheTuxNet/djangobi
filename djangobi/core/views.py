from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from apps.olist.models import *
from django.db import connection
import pandas as pd
import matplotlib.pyplot as plt
import core.viz_utils as viz
from django.contrib import messages
from core.utils import get_chart
import plotly.express as px
from plotly.offline import plot



# Create your views here.
@login_required()
def index(request):
    order_status_qs = Order.objects.all().values('order_status').annotate(total=Count('order_status')).order_by('total')

    for x in order_status_qs:
        print(x)

    projects_data = [
        {
            'Status': x['order_status'],
            'Qty': x['total'],
        } for x in order_status_qs
    ]
    df = pd.DataFrame(projects_data)
    fig = px.bar(df, x="Status", y="Qty", color ="Status", title="Lorem Ipsum Dolor", barmode='relative', log_y=True)
    fig.update_layout(xaxis_title='Stato Ordine', yaxis_title='Log Qty')
    plt_bar = plot(fig, output_type="div")
    # fig.show()

    context = {
        'PageTitle': 'Dashboard',
        'NumOrders': Order.objects.all().count(),
        'NumCustomers': Customer.objects.all().count(),
        'NumOrderItems': OrderItem.objects.all().count(),
        'OrderStatuses': order_status_qs,
        'plot_div': plt_bar
    }

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
