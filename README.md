# Create accounts
* You need a Github account for making pull requests
* You need a Launchpad account for bug tracking

# Fork Dormbase
* If you've never used Github before, read https://help.github.com/categories/56/articles
* Visit https://github.com/dormbase/dormbase
* Click "fork" at the top right
* To download the code, run `git@github.com:USERNAME/dormbase.git` on your laptop
* If you've never used a Github fork before, read Read https://help.github.com/categories/63/articles

# Set up your dev environment
* Install all packages in `requirements.txt`
  * Install each one manually (`sudo pip install packagename`)
  * Or install all at once (`sudo pip install -r requirements.txt`)
* Create and populate database tables:
  * `python manage.py syncdb`
  * `python manage.py migrate`
  * `python manage.py shell`, then (inside the shell) `import populate`
* Set up photologue:
  * `python manage.py plinit` and use sizes 130x175 for thumbnails, 323x475 for display
* Set up Whoosh:
  * If you need search to work locally, edit `dormbase/settings.py` as described below
  * Then run `python manage.py rebuild_index`

If you need search to work locally, then in `dormbase/settings.py` comment out:

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

* Run the server:
  * `python manage.py runserver`
  * Visit http://localhost:8000/ in your web browser

# Suggested workflow
* Claim a bug at https://launchpad.net/dormbase
* Create a new branch for each ticket you're working on (`git checkout -b branchname`)
* Commit your fix, and push to Github (`git push -u origin branchname`)
* Visit your forked repo on Github, and click the "pull request" button
* Someone will review your pull request and may ask you to update your commit, if necessary

