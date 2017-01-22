def strip_name(uri):
    return uri.split('/')[-1]


def convert_to_internal_wikipedia_link(uri):
    entity_name = strip_name(uri)
    return '/wiki/' + entity_name


def convert_to_wikipedia_uri(uri):
    entity_name = strip_name(uri)
    return 'https://en.wikipedia.org/wiki/' + entity_name


def strip_cleaned_name(uri):
    """
    http://dbpedia.org/resource/Alain_Connes -> 'Alain Connes'
    """
    entity_name = strip_name(uri)
    entity_name = entity_name.replace('_', ' ')
    # return clean_input(entity_name)
    return entity_name