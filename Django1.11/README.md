Remember to do this at the start of a new Django project before you run any migrations. If you have run
any migrations you might be able to just delete them but look up more about that before you do.

1) Create an 'App' with a name of your choice
2) Copy and paste the code from models.py into your new 'App', replacing anything you don't need
3) Copy and paste the code from forms.py into your new 'App', you're gonna have to create a forms.py to paste into
4) Copy and paste the code from admin.py into your new 'App', replacing anything you don't need
5) Then in your settings.py file make your AUTH_USER_MODEL point to your new custom user model

Example: AUTH_USER_MODEL = App.CustomUser

Note: A) You don't have to specify the models.py file cause for some reason it will just 
automatically look in there, so App.CustomUser is sufficient

Note: B) If there is no AUTH_USER_MODEL then just write it in, :]

6) Make sure to update your 'INSTALLED_APPS' setting(variable) in your settings.py file
7) Run migrations and you are done

You now have a custom user, more like a custom admin-compliant authentication user model. 
The django docs recommend always instituting a custom user at the beginning of a project 
just in case later on down the road the user needs to be modified. Way less hassle, 
waaaaaaaaaaaaaaaaaaaaaaaay less.


__ Frank __

