from django.shortcuts import render
from .models import TableField, CsvFile
import csv


# Create your views here.
def table_view(request):
    csv_file = CsvFile.objects.all()
    if csv_file.count() > 0:
        csv_filename = csv_file.first().get_path()
    else:
        csv_filename = None

    table_fields = TableField.objects.order_by('number')
    columns = list()
    for t_f in table_fields:
        columns.append({'name': t_f.name, 'width': t_f.width, 'num': t_f.number})

    with open(csv_filename, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

    context = {
        'columns': columns,
        'table': table,
        'csv_file': csv_filename
    }
    return render(request, 'table.html', context)
