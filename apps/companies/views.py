from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .forms import CompanyForm, PositionForm
from .models import Company, Position
from addresses import gmaps
from addresses.forms import AddressForm

def company_detail(request, company_id):
    company_list = Company.objects.all()
    positions = Position.objects.select_related().filter(company=company_id)

    company = Company.objects.get(pk=company_id)
    company_json = gmaps.create_company_infos(company, as_json=True)
    
    return object_detail(request, queryset=company_list, object_id=company_id, extra_context={'positions':positions, 'company_json':company_json})

def company_add(request):

    if request.method == 'POST' :
        company_form = CompanyForm(request.POST)
        address_form = AddressForm(request.POST)
        if company_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            address.save()
            company = company_form.save(commit=False)
            company.address = address
            company.save()
            return redirect('companies-detail', company_id=company.id)
    else:
        company_form = CompanyForm()
        address_form = AddressForm()
    
    return render_to_response('companies/company_form.html',{'form':company_form, 'address_form':address_form}, context_instance=RequestContext(request))

def company_list_map(request):
    company_list = Company.objects.all()  
    markers = gmaps.create_company_markers(company_list)  
    return render_to_response('companies/company_map.html', {'company_markers':markers}, context_instance=RequestContext(request))

def company_list_alphabetical(request, first_letter=None):    
    companies_for_browse = Company.objects.none()
    companies_for_filter = Company.objects.all()
    
    if first_letter:
        companies_for_browse = Company.objects.filter(name_slug__istartswith=first_letter).order_by('name')
    
    context = {'companies_for_filter':companies_for_filter, 'first_letter_in':first_letter}

    return object_list(request, queryset=companies_for_browse, extra_context=context, paginate_by=20)

def position_add(request):
    if request.method == 'POST' :
        form = PositionForm(request.POST)
        if form.is_valid() :
            position = form.save()
            position.profile = request.user.profile
            error = False
            
            # rule that should be in form clead but meh :|
            if position.date_end and (position.date_end < position.date_start):
                error = True
                form.errors['end_date'] = "Must be greater than start date"

            # can't create position is a current position is held or if submitted position overlap with another
            positions = Position.objects.filter(profile=request.user.profile)
            for p in positions:
                if p.date_end == None and position.date_end == None:    
                    form.errors['end_date'] = "You are already holding a position at " + p.company.name +". Only one current position is allowed."
                    error = True
                    break
                elif p.date_end != None and ((position.date_start < p.date_end) and (position.date_end > p.date_start)) :
                    form.errors['end_date'] = "This position dates are overlapping with your position at " + p.company.name
                    error = True
                    break
                
            if not error:
                position.save()
                return redirect('companies-detail', company_id=position.company.id)
    
    else:
        form = PositionForm()
    
    context = {'form':form}
    return render_to_response('companies/position_form.html', context, context_instance=RequestContext(request))

def position_manage(request):
    positions = Position.objects.filter(profile=request.user.profile.id_booster)
    return object_list(request, queryset=positions)

def position_delete(request):
    obj = request.POST['delete']
    get_object_or_404(Position, pk=obj, profile=request.user.profile.id_booster)
    return delete_object(request, Position, reverse('companies-positions-manage'), object_id=obj)
