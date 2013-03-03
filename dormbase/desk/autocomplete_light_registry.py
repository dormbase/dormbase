import autocomplete_light

from dormbase.personal.models import Guest

autocomplete_light.register(
    Guest,
    autocomplete_light.AutocompleteModelTemplate,
    choice_template='desk/guest_choice.html',
    search_fields=('athena', 'fullname'),
    name="GuestSigninAutocomplete")
