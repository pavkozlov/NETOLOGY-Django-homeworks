from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    context = dict()
    template = "app/calc.html"
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            context['result'] = int((form.cleaned_data['initial_fee'] + form.cleaned_data['initial_fee'] *
                                     (form.cleaned_data['rate'] / 100)) / form.cleaned_data['months_count'])
            context['common_result'] = form.cleaned_data['initial_fee'] + context['result']
    else:
        form = CalcForm()

    context['form'] = form

    return render(request, template, context)
