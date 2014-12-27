from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from groups.models import Group, Person
from transactions.models import Transaction

# Create your views here.
def new(request, group_id):
  group = get_object_or_404(Group, pk=group_id)

  return render(request, 'new_transaction.html', {
    'group_id': group_id,
    'members': group.member_set.all()
  })

def create(request, group_id):
  owes = request.POST.getlist('owes')
  paid = request.POST.getlist('paid')
  group = get_object_or_404(Group, pk=group_id)

  has_error = False
  amount_error = ''
  name_error = ''

  print(owes);
  print(paid);

  try:
    amount = float(request.POST['amount'])

    if amount <= 0:
      has_error = True
      amount_error = "Amount must be larger than 0. "
  except ValueError:
    has_error = True
    amount_error = "Invalid amount. "

  name = request.POST['name']

  if len(owes) == 0 or len(paid) == 0:
    has_error = True
    amount_error = 'Someone must owe/pay. '

  if len(name) < 2:
    has_error = True
    name_error = "Name must be at least 2 chars long. "

  if has_error:
    return render(request, 'new_transaction.html', {
      'group_id': group_id,
      'name_error': name_error,
      'amount_error': amount_error,
      'name': request.POST['name'],
      'amount': request.POST['amount'],
      'owes': owes,
      'paid': paid,
      'members': group.member_set.all()
    })
  else:
    pay_amount = amount / len(paid)
    owe_amount = -(amount / len(owes))

    for o in owes:
      m = get_object_or_404(Person, pk=o)
      m.transaction_set.create(amount=owe_amount)

    for p in paid:
      m = get_object_or_404(Person, pk=p)
      m.transaction_set.create(amount=pay_amount)

    return HttpResponseRedirect(reverse('show_group', kwargs={'group_id': group_id}))
