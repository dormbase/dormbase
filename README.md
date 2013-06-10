# Welcome to Dormbase.
Dormbase is a web-based system that provides MIT
dormitories with the tools and services they need for daily operation. It is
an open source software project that was started by Simmons Tech in response
to their and the resident's need for reliable, modern, and user-friendly
online services. Dormbase means a consistent user experience across all of
MIT's dorms, accessible to residents, desk workers, and administration. It is
a community project that solves a community problem.

# Learn About GitHub
* If you've never used GitHub before, read about [how to authenticate](https://help.github.com/categories/56/articles)
* If you've  never used a GitHub fork before, read about [pull requests](https://help.github.com/categories/63/articles)

# Get Started
* RECOMMENDED: Create a python virtualenv environment, by
  running `virtualenv DIR`, and then activate it by running `source DIR/bin/activate`.
* [Install the dependencies](https://github.com/dormbase/dormbase/wiki/Dependencies)
* Finish following the [Dev Server Setup](https://github.com/dormbase/dormbase/wiki/Dev-Server-Setup) -
  and take the shortcut, if you can!
* Run the server:
  * `python manage.py runserver`
  * Visit http://localhost:8000/ in your web browser

# Setting up search locally
You should almost certainly skip this step. If for some reason you need search
to work locally, set up Whoosh.

* Edit `dormbase/local_settings.py` to comment out:

~~~
#HAYSTACK_SEARCH_ENGINE = 'solr'
#HAYSTACK_SOLR_URL = 'http://127.0.0.1:8088/solr'
~~~

And right below, add these two lines:

~~~
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = 'whoosh_index/'
~~~

* Then run `python manage.py rebuild_index`

# License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
