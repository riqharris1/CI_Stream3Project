Issue tracker
what the project does and the need that it fulfils:
This project allows users to submit requests for bug fixes and new features.

Description of the functionality of the project, as well as the technologies used: 
The project has an issue tracker login page,a new features page and a user profile page.
It uses Python,Django framework,HTML and a database.
Django is a python framework that allows access to libraries.  
The database was created by using django models and migrated to SQL on the local machine before being migrated to Heroku(ClearDB). 

Links 
Issue tracker login page-
allows users to login and create issues(issue type:task,history,bug,new feature)/requests to be submitted and viewed.
once,logged in,click view site to view other pages.

New features page-
allows users to view and pay for new features selected for further development .

Profile page-
show's username,stripe id,subscription details.

How the project was deployed, what was kept and what was changed to fit requirements:
The working project is deployed on Heroku and project code on Github and is based on code from the code institute sample project,Django apps such as accounts and products were kept and some python modules were upgraded to ensure compatability with the hosting site.



Installation requirements:
Required python modules:
alabaster==0.7.11
api==0.0.7
appdirs==1.4.3
arrow==0.10.0
astroid==2.0.4
Babel==2.6.0
beautifulsoup4==4.6.0
certifi==2018.4.16
chardet==3.0.4
codegen==1.0
colorama==0.3.9
disqus==0.0.4
dj-database-url==0.5.0
Django==2.1.2
django-bugtracker==1.1.0
django-core==1.4.1
django-cors-headers==2.4.0
django-debug-toolbar==1.9.1
django-disqus==0.5
django-documentation==1.1
django-emoticons==1.2
django-filter==2.0.0
django-forms-bootstrap==3.0.1
django-patterns==0.0.3
django-paypal==0.5.0
django-registration==2.2
django-rest-framework==0.1.0
django-rest-framework-docs==0.1.7
django-tinymce==2.7.0
django-views==1.0.1
djangorestframework==3.6.3
djangorestframework-jwt==1.11.0
documentation==0.0.1
docutils==0.14
ez-setup==0.9
funcsigs==1.0.2
gunicorn==19.7.1
idna==2.7
imagesize==1.0.0
isort==4.3.4
Jinja2==2.10
jsonpickle==0.9.6
lazy-object-proxy==1.3.1
MarkupSafe==1.0
mccabe==0.6.1
mock==2.0.0
nose==1.3.7
olefile==0.45.1
packaging==17.1
patterns==0.3
pbr==3.1.1
Pillow==4.1.1
psycopg2==2.7.5
Pygments==2.2.0
PyJWT==1.6.4
pylint==2.1.1
pyparsing==2.2.0
python-dateutil==2.6.0
pytz==2017.2
requests==2.14.2
reusable-blog-app==1.0.0
six==1.10.0
snowballstemmer==1.2.1
South==1.0.2
Sphinx==1.7.7
sphinxcontrib-websupport==1.1.0
sqlparse==0.2.4
stripe==1.55.2
typed-ast==1.1.0
urllib3==1.23
views==0.3
virtualenv==16.0.0
wrapt==1.10.11

# UnicornAttractor issues tracker

UnicornAttractor is an awesome service with million of user used to attract unicorns.
This project is an issue tracker to report bugs or new features the platform users. 

## Build An Issue Tracker

Now that you’re a full fledged web developer you’ve decided it’s probably time for you 
to start your very own cool, modern startup, offering the extremely awesome UnicornAttractor
webapp to your users. It’s really really amazing, but we don’t care about it at all in this
project. The interesting thing is the business model that you’ve decided upon – 
you chose to offer the service and bug fixes for free, but ask for money from your users to
develop additional features.

To manage the tracking of bugs and feature requests, you decided to create an Issue Tracker that will allow your users to submit and track any issues (bugs or feature requests) related to using the UnicornAttractor.

The basic entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, you should allow users to create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do’, ‘doing’, or ‘done’). As mentioned, issues come in two varieties – ‘bugs’ (which you’ll fix for free, eventually), and ‘features’ which you’d only develop if you’re offered enough money. To help you prioritise your work, your users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’). While upvoting bugs is free, to upvote a feature request, users would need to pay some money (with a minimum amount of your choice) to pay for your time in working on it. In turn, you promise to always spend at least 50% of your time working on developing the highest-paid feature.

To offer transparency to your users, you decide to create a page that contains some graphs showing how many bugs and features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.

Add any additional pages that would help you attract users to the Issue Tracker (and have them pay you well). To make the users participate as much as possible in your online community, make sure that your UI/UX is sublime. Feel free to add additional features, such as a blog, additional perks for active participants, etc…

If you want to have some more fun with this, feel free to also add pages describing your fictional UnicornAttractor application ??

And of course, as this project is going to be lifeblood of your company, it’s important that new developers that join the company will be able to get up and running as quickly as possible. Documentation is the best way to achieve this.


    Build a web app that fulfills some actual (or imagined) real-world need. This can be of your own choosing and may be domain specific.
    The project must be a brand new Django project, composed of multiple apps (an app for each reusable component in your project).
    The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. E.g. a user would have to register in order to persist their shopping cart between sessions (otherwise it would be lost).
    At least one of your Django apps should contain some kind of e-commerce functionality using Stripe and/or Paypal. This may be a shopping, or subscriptions, or single payments, etc.
    Include at least one form with validation, that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
    The project will need to connect to an SQL database using Django’s ORM, or to a Document-Oriented database (e.g. MongoDB) using pymongo.
    The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.
    As well as having a responsive UI, the app should have a great user experience.
    The frontend should contain some JavaScript logic to enhance the user experience.
    Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Disqus, Django Rest Framework, etc. Strive to choose the best tool for each purpose and avoid reinventing the wheel, unless your version of the wheel is shinier (and if so, consider also releasing your wheel as a standalone open source project).
    Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to the users, in any circumstances. Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests.
    Write a README.md file for your project (in Markdown format) that explains what the project does and the need that it fulfils. It should also describe the functionality of the project, as well as the technologies used. Detail how the project was deployed and tested and if some of the work was based off other code, explain what was kept and/or how it was changed to fit your need. A project submitted without a README.md file will FAIL.
    In addition to the README.md file, you may include in your repository supplementary documentation and/or other relevant supporting material for the assessor in any format that is automatically handled by web browsers, such as html, pdf, jpg, etc. Files in proprietary formats such as Microsoft doc/docx will be ignored; but this is generally not a hindrance, since the vast majority of formats can be easily exported to PDF.
    Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
    Deploy the final version of your code to a hosting platform such as Heroku.

Additional Advice

    We advise that you create wireframes before embarking on full blown development (you can use Balsamiq or any other tool, including just pen and paper)..
    Incorporate as much as you have learned in our lessons.
    The site can also make use of CSS, Javascript and Python libraries/frameworks, just make sure you maintain a clear separation between the library code and your own code
    Please refer back to your mentor to get constant feedback as you progress
    Don’t forget to use your mentor’s help. Your mentor can act as:
        Your client
        Your technical consultant
