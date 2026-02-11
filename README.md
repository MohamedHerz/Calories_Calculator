
# Calories Claculator
#### Date 11-Feb-26
#### By: x

***
#### [GitHub](https://github.com/MohamedHerz/Calories_Calculator) | [Render](https://calories-calculator-5dct.onrender.com/) | [Trello](https://trello.com/b/H8X4jvEi/calories-calculator)
***
### ***Description***
#### A food calculator site allows users to instantly track daily nutritional intake, including calories and #### searching a comprehensive food database.


***
### **Getting started**
#### The website loads Home page rendering a short description about the site it will give the option to guests to sign up or sign in then it will redirect them to home page after signing in, on nav bar there is taps for food where user could see the available food in database, a button to add food. next tap is meals where user is able to add any food from the food list, at goal page users are able to set a daily calories to consume a progress bar will show the amount of calories they have consumed / their log also it register it by dates.
***

### ***Technologies used***
* Utilizing EJS for charts
* SQL database
* python - django framework
* Git

***
### Database ERD

![](Calories_Calculator\Screenshot 2026-01-21 182154.png)

### ***QA***
- [x] Users cannot delete/edit/read other users logs or meal details
- [x] Anyone can delete or edit or add food in food model as it is a community managed app
- [x] Authentication implemented
- [x] App's navigation responds to user login status

***
### Future enhancement
- Enabling super user to give more permission to certain users to maintain the app database
- More detailed chart on food details
- Send a warning to users if they have vitamin deficiency
- Providing option for users to enable receiving notifications on their email if they missed a day on the site

***

#### [screenshot of deployed site](Calories_Calculator\image.png)


### **Resources**

#### [1](https://stackoverflow.com/questions/3294889/iterating-over-a-dictionary-using-a-for-loop-getting-keys)
#### [2](https://stackoverflow.com/questions/67504450/django-how-to-restrict-staff-user-to-edit-or-delete-others-staff-user-post-from)
#### [3](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.has_delete_permission)
#### [4]((https://www.reddit.com/r/django/comments/ebbsrn/how_to_limit_users_to_only_edit_their_own_posts/))
#### [5](https://ccbv.co.uk/projects/Django/1.9/django.contrib.auth.mixins/UserPassesTestMixin/)

