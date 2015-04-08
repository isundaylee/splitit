from django.shortcuts import render, get_object_or_404, redirect
from groups.models import Group, Person
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views.decorators.http import require_http_methods

# Create your views here.

def show(request, group_id):
  group = get_object_or_404(Group, pk = group_id)

  print(group.member_set.all())

  return render(request, 'show.html', {
    'group_id': group_id,
    'name': group.name,
    'people': list(map(lambda m: {'name': m.name, 'balance': m.balance(), 'id': m.pk}, group.member_set.all()))
  })

def show_person(request, group_id, person_id):
  person = get_object_or_404(Person, pk = person_id)

  return render(request, 'show_person.html', {
    'person_id': person.pk,
    'name': person.name,
    'transactions': list(map(lambda t: {'name': t.name, 'amount': t.amount}, person.transaction_set.all())) + [{'name': 'Total balance', 'amount': person.balance()}],
  })

def new(request):
  members = [{'name': ''} for i in range(10)]
  return render(request, 'new.html', locals())

@require_http_methods(["POST"])
def create(request):
  name = request.POST['name']
  members = request.POST.getlist('members')

  name_error = ''
  if len(name) < 2:
    name_error = 'Name is too short. '

  members = list(map(lambda x: {'name': x, 'error': ("Name is too short." if len(x) > 0 and len(x) < 2 else "")}, members))
  member_errors = list(map(lambda x: x['error'], members))

  if name_error or any(member_errors):
    return render(request, 'new.html', locals())
  else:
    group = Group.objects.create(name=name)
    for member in members:
      if member['name']:
        group.member_set.create(name=member['name'])

    return redirect('groups.views.show', group_id=group.pk)


  print(member_errors)

  return HttpResponse(members)

def index(request):
  return render(request, 'groups.html', {'groups': Group.objects.all()})