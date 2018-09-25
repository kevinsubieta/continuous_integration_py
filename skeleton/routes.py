def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_jinja2_search_path('templates')

    config.add_route('home', '/')
    config.add_route('people', '/people')
    config.add_route('person', '/person')
    config.add_route('add_person', '/add_person')
    config.add_route('delete_person', '/delete_person')
