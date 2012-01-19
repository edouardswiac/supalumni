from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.simple import direct_to_template

from .models import Profile
from .models import Bookmark
from companies.models import Position

def profile_detail(request, profile_id):
    profiles = Profile.objects.all()
    positions = Position.objects.filter(profile=profile_id)
    
    bookmark = Bookmark.objects.filter(from_profile=request.user.username, to_profile=profile_id).exists()
        
    if bookmark:
        is_bookmarked = True
    else:
        is_bookmarked = False
        
    context = {'positions':positions, 'is_bookmarked': is_bookmarked}
    return object_detail(request, queryset=profiles, object_id=profile_id, extra_context=context)

def list_alphabetical(request, first_letter=None):
    profiles_for_browse = Profile.objects.none()
    profiles_for_filter = Profile.objects.all().order_by('last_name_slug')
    
    if first_letter:
        profiles_for_browse = Profile.objects.all().filter(last_name_slug__istartswith=first_letter).order_by('user__last_name')
    
    positions_dict = get_positions_dict(profiles_for_browse);

    context = {'positions':positions_dict, 'profiles_for_filter':profiles_for_filter, 'first_letter':first_letter, 'alpha':True}
    
    return object_list(request, queryset=profiles_for_browse, extra_context=context, paginate_by=20)

def list_promotions(request, promotion=None):
    profiles_for_browse = Profile.objects.none()
    profiles_for_filter = Profile.objects.all().order_by('promotion')
    
    if promotion:
        profiles_for_browse = Profile.objects.all().filter(promotion=promotion).order_by('promotion', 'last_name_slug')        
    
    positions_dict = get_positions_dict(profiles_for_browse);
    
    context = {'positions':positions_dict, 'profiles_for_filter':profiles_for_filter, 'promotion':promotion, 'promo':True}
    
    return object_list(request, queryset=profiles_for_browse, extra_context=context, paginate_by=20)
    
def get_positions_dict(profiles_qs):
    profiles_id = profiles_qs.values('id_booster');
    positions_qs = Position.objects.select_related().filter(profile__in=profiles_id, date_end=None)
    
    position_dict = {}
    for e in positions_qs:
        meta = {}
        meta['company_name'] = e.company.name
        meta['company_flag'] = e.company.address.country.flag
        position_dict[e.profile_id] = meta
    return position_dict
    