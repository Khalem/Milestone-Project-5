# Milestone Project 5

For my final Milestone Project, I decided to stray away from the brief and create something new! I went with a fictional charitable organisation known as 'Praesidio'. I got this name by simply
translating the word 'protect' to Latin. I created the logo myself, using two different fontawesome icons in photoshop.

I created this site with HTML, CSS, JavaScript and Python using Django. The main focus of the site, is to get payments from users to help save endangered species from becoming extinct. This is 
consistently being mentioned in the site. I also created a community page where users can interact with eachother or get help from staff. Because it was my first time using Django, I wanted to
make sure the site was functional while maintaining a pleasing aesthetic.

## UX
Because of the size of this site, I wanted to ensure that I kept everything a simple as possible while still looking good. Materialize helped a lot with achieving this goal. The users on this site may just be visiting, and curious 
to know what this site does. So having multiple ways to reach the endangered animals while explaining what we do was a must. Of course, the main goal of the site is for the user to purchase something, this meant I needed to keep the
payment process familiar with what the user would be used to, as not to frustrate the user. On the community page, I wanted to make it very clear which posts were made by staff and which posts were made by the user. This was done
with seperate pagination, making it easy for users to read important posts.

**User Stories:**
* **As a user I want to** be able to view endangered animals and adopt them.
* **As a user I want to** be able to create an account.
* **As a user I want to** be able to edit my profile.
* **As a user I want to** be able to post to a community forum.
* **As a user I want to** comment on animals and posts.
* **As a user I want to** be able to like posts or comments.
* **As a user I want to** see other users profiles.

I have left both a .xd and .pdf file of my wireframe in my [cloud9 workspace](https://ide.c9.io/khalemc/milestone-project-5) in the "wireframes" folder.

## Features
#### Existing Features
* **Animal Cards** - users can click on the card to view an animal and adopt one.
* **Login/Register Form** - users can create an account or log back in.
* **Posts** - users can view posts they made on their profile, or view all of them in the community.
* **Post/Comment Form** - allows users to create a post or comment.
* **Tabs** - users can view different parts of an animal without taking up all of their screen.
* **Search Bar** - contains a select and text input. Users can search based on status or name.
* **Pagination** - users can navigate through posts without taking up all their screen.
* **Like Button** - users can like a post or comment.
* **Nav** - users can navigate the site.
* **Forgot Password Link** - users recieve an email allowing them to reset their password.

#### Features Left to Implement
* **Search Bar for Posts** - Upon finishing, I realised it would have been good to have a search bar in the community so users can search for a specific post.

## Technologies Used
* **HTML**
* **CSS**
  * [Materialize](https://materializecss.com/) - used for layout of site and for the many components of the site(forms, modals, etc..).
  * [Font Awesome](https://fontawesome.com/) - used for the icons of the site.
  * [Custom Bootstrap](https://getbootstrap.com/) - made a custom version of bootstrap to contain only their grid system. Used for Data.html.
* **JavaScript**
  * [jQuery](https://jquery.com/) - used to simplify DOM manipulation.
  * [Materialize](https://materializecss.com/) - used for components of the site.
  * [Chart.js](https://www.chartjs.org/) - used for graphs on data.html
* **Python**
  * [Django 1.11](https://www.djangoproject.com/) - used for the whole site.
* **Storage**
  * [AWS S3](https://aws.amazon.com/s3/) - used to host static files and images.
 
## Testing
For the testing of this site, I used Travis CI for automated tests, and did extensive manual testing.

**Travis CI test:**
[![Build Status](https://travis-ci.org/Khalem/Milestone-Project-5.svg?branch=master)](https://travis-ci.org/Khalem/Milestone-Project-5)

**Manual Testing**
Manual testing began with testing the functionality of each app. This was done by myself, but my meeting with my mentor also helped as he was able to point out some bugs within the site. I also
gave the site to my family and got them to act as a normal user, to see if they could come across any bugs.

I will split the testing into two categories, logged in and logged out.

**Logged Out:**
* **Adopt an Animal** - I tested to see if you could adopt an animal while logged out, when you try to checkout, you get redirected to the login page.
* **Create a Post** - I tested to see if you could write a post while logged out, you get redirected to the login page.
* **Create a Comment** - I tested to see if you could write a comment while logged out, you get redirected to the login page.
* **Like a Post/Comment** - You get redirected to the login page.

**Logged In:**
* **Leaving Quantity Blank:** - My mentor actually found this bug, I simply put required at the end of the input.
* **Trying to checkout with no items** - I tested to see if you could checkout while having 0 items. The button does not appear.
* **Inputting a number less than 1 in the quantity field** - I tested to see if you could put an invalid number in. Does not work.
* **Posting a blank comment** - upon testing this, I found that django-comments has their own way of handling invalid comments. I fixed this by adding some javascript to add required to the input field.
* **Leaving payment details blank** - the user will recieve an error above the form.
* **Trying to create an account with the same email or username** - django actually takes care of that.

**Responsive Testing**
To test the responsiveness of the site, I used chrome developer tools, my own phone, laptop and [Responsinator](https://www.responsinator.com/). I am quite pleased with the results and I am confident a user using any device,
will be able to use the site with ease.

## Changes I Would Like to Make
Although I am happy with this site, I would be lying if I said there wouldn't be anything I would change. Firstly, I would like to change the adoption plan models. I feel the way I did it was a hacky way, this is mostly due to the fact
that it was one of the first apps I created on the site. I feel as if I learned a lot from the project and in the future I know I could do it a better way. Secondly, I would add some javascript to handle the like events. For example, if 
a user likes a post, I would use a function to get data from the backend and update the site when the response is a success. I feel this would have given a much better user experience and I will definitely add this next time! Finally,
I would like to change the way the comments are structured. I feel as if they take up way too much space and could've been handled better.

## Deployment
To begin my deployment, I first transferred all my static files to AWS S3. This was done by creating a bucket and adding some code to my project. To begin my deployment on Heroku, I first added all my environment variables to the 
config vars. I then created a requirements.txt and Procfile. I also had to install gunicorn for the deployment to work. Within my settings.py file, I changed debug to False and commented out the "import env" as that wouldn't be necessary
anymore. I connected my app to my github repository and created a new branch. The build was a success.

To run this code locally, I use Visual Studio 2017.

[**You can view the deployed site here!**](https://khalem-milestone-5.herokuapp.com/)

## Credits
**Photos and Information** - I am thankful for the [WWF](https://www.worldwildlife.org/), without their images or data this site would not be possible.