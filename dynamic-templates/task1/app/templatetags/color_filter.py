from django import template

register = template.Library()


@register.filter
def pick_color(i):
    try:
        res = float(i)
        if res < 0:
            return "green"
        else:
            if 1.0 < res < 2.0:
                return "#FCD3D3"
            elif 2.0 < res < 5.0:
                return "#F98C8C"
            elif res > 5.0:
                return "#FF0000"
            else:
                return ""
    except ValueError:
        return i


