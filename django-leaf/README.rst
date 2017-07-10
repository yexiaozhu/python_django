=====<br/>
Leaf<br/>
=====<br/>

Leaf is a simple Django app to conduct Web-based leaf. For each<br/>
question, visitors can choose between a fixed number of answers.<br/>

Detailed documentation is in the "docs" directory.<br/>

Quick start<br/>
-----------<br/>

1. Add "leaf" to your INSTALLED_APPS setting like this::<br/>

    INSTALLED_APPS = [<br/>
        ...<br/>
        'leaf',<br/>
    ]<br/>

2. Include the leaf URLconf in your project urls.py like this::<br/>

    url(r'^leaf/', include('leaf.urls')),<br/>

3. Run `python manage.py migrate` to create the leaf models.<br/>

4. Start the development server and visit http://127.0.0.1:8000/admin/<br/>
   to create a leaf (you'll need the Admin app enabled).<br/>

5. Visit http://127.0.0.1:8000/leaf/ to participate in the leaf.<br/>