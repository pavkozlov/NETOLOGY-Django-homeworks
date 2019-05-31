from django import template

register = template.Library()


@register.filter
def pick_color(i):
    try:
        res = float(i)
        if res < 0:
            return f'<td style="background:green">{res}</td>'
        else:
            if 1.0 < res < 2.0:
                return f'<td style="background:#FCD3D3">{res}</td>'
            elif 2.0 < res < 5.0:
                return f'<td style="background:#F98C8C">{res}</td>'
            elif res > 5.0:
                return f'<td style="background:#FF0000">{res}</td>'
            else:
                return f'<td>{res}</td>'
    except ValueError:
        return f'<td>{i}</td>'


