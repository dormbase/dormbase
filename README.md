# Create accounts
* You need a Github account for making pull requests
* You need a Launchpad account for bug tracking

# Fork Dormbase
* If you've never used Github before, read https://help.github.com/categories/56/articles
* Visit https://github.com/dormbase/dormbase
* Click "fork" at the top right
* To download the code, run `git@github.com:USERNAME/dormbase.git` on your laptop (and it will download the code to a directory called `dormbase`)
* If you've never used a Github fork before, read https://help.github.com/categories/63/articles

# Set up your dev environment
* Make sure you have python-dev (`sudo apt-get install python-dev`)
* Install all packages in `requirements.txt`
  * Install each one manually (`sudo pip install packagename`)
  * Or install all at once (`sudo pip install -r requirements.txt`)
* cd into `dormbase` before running any of the following commands
* Create and populate database tables:
  * `python manage.py syncdb` (you can answer no to the superuser prompt)
  * `python manage.py migrate`
  * `python manage.py shell`, then (inside the shell) `import populate`
* Set up photologue:
  * `python manage.py plinit` and use sizes 130x175 for thumbnails, 323x475 for display (as width x height, answers to other questions don't matter)
* Run the server:
  * `python manage.py runserver`
  * Visit http://localhost:8000/ in your web browser

# Setting up search locally
You should almost certainly skip this step. If for some reason you need search to work locally, set up Whoosh.

* Edit `dormbase/settings.py` to comment out:

~~~
#HAYSTACK_SEARCH_ENGINE = 'solr'
#HAYSTACK_SOLR_URL = 'http://127.0.0.1:8088/solr'
~~~

And right below, add these two lines:

~~~
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = 'whoosh_index/'
~~~

But (until we figure things out better) make sure not to commit this change!

* Then run `python manage.py rebuild_index`

# Suggested workflow
* Claim a bug at https://launchpad.net/dormbase
* Create a new branch for each ticket you're working on (`git checkout -b branchname`)
* Commit your fix, and push to Github (`git push -u origin branchname`)
* Visit your forked repo on Github, and click the "pull request" button
* Someone will review your pull request and may ask you to update your commit, if necessary

