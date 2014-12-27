from django import template

register = template.Library()

@register.filter(name='dollar_amount')
def dollar_amount(amount):
  amount = float(amount)
  if amount >= 0:
    return "$" + str(amount)
  else:
    return ("-$") + str(-amount)
