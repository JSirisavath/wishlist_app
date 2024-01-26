# Travel Wishlist App

Developer: Jerry Sirisavath

Initial Commit To Github: 11-04-23

## Introduction

The Travel Wishlist is a Full-Stack app that allows users to document and note down places they have traveled to or make a wishlist of places they want to travel to! Additionally, users can have a customizable review for their traveled places with the ability to write down their thoughts, upload their favorite pictures, and add a start date traveled about that place. Users can also come back and edit that traveled place or delete it! This Full-Stack app uses Django Framework, Python, Javascript, HTML, and a simple predeveloped CSS framework, watercss. 


## Getting Started (Running app in development mode)

To run the Travel Wishlist App:
1. Clone this repository in a preferred code editor on your local machine.
2. Open the terminal on your editor and start up this repo's virtual environment.
3. Activate a virtual environment, run `source djangoVenv/bin/activate`.
- Activating Python's Venv on VSCode Stack Overflow: 
`https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code`

4. If activated virtual env correctly, in the same terminal, run the command, `python manage.py runserver` to run the app in your browser: `127.0.0.1:8000` is the link.
5. You will need to create a admin portal to access the app. On your browser where app is running, type in, `127.0.0.1:8000/admin` and follow the prompt to set up a new user.
6. After successfully setting up your account, go back to `127.0.0.1:8000` on the same or new tab, and then login with the same account you've created.
7. After logging in, you should now see the home page of the app. If you  want to stop the app running on your browser, on the terminal in your editor, run this command: 
- MacOS & Windows:`CTRL + C`



## Features

- **Add a travel place to a wishlist or visited:** Users can input a desired place in the textbox, and if the place has been visited, they can check visited box else, add it to the wishlist. User's are can also delete or edit a place.
- **Dynamic Data Management:** Utilizes Django's class models that are connected to the database. For example, after defining the Place class for models, we need to set up the migrations
- **User-Friendly Interface:** Designed with a focus on easier user experience and UI menu.


## Site Demo Screenshots
<img width="985" alt="Screenshot 2024-01-26 at 1 40 21 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/5b69a500-d960-4f8d-a782-784fbdcd8aa3">

<img width="986" alt="Screenshot 2024-01-26 at 1 44 54 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/04110ae5-9da8-40ba-9f7f-349e33375612">

<img width="985" alt="Screenshot 2024-01-26 at 1 44 47 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/876ac17c-f6ad-441d-9933-684641318228">

<img width="986" alt="Screenshot 2024-01-26 at 1 44 27 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/ff283283-2009-418d-bff4-31be2b9f60b2">


<img width="984" alt="Screenshot 2024-01-26 at 1 44 02 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/34e1bcb7-cc8c-42ad-8737-43f69818e8c2">

<img width="986" alt="Screenshot 2024-01-26 at 1 41 24 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/b50cc7a4-461c-4033-aa31-19439f3c5792">

<img width="989" alt="Screenshot 2024-01-26 at 1 42 57 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/89fa4524-d70e-482c-a199-49a937f5b819">

<img width="985" alt="Screenshot 2024-01-26 at 1 41 03 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/305d2f87-4e31-4b57-994e-6f80fb24b74c">



## Technical Insights
- **Database and Django's Model Creation:** After defining the Place class for models, I needed to set up the migrations to create/modify instructions on how to create a DB table to handle this information. To do so, for each change for the model class, users inherit those special attributes. After creating and modifying those models which is connected to the instructions of the DB table, we would then run `python manage.py makemigrations` and run `python manage.py migrate` to ask the DB to create that table. So now, when users create a new place, that place will inherit those attributes of a Place model class, which is also reflected in the Place table in DB.
- **Routes Handling and Fetches From Users:** I would create and use the URL patterns both in the app(Travel_wishlist folder), and the URL paths in the root folder (wishlist folder). The main URL paths in the wishlist folder are given routes to when requests are made, the main app knows how to handle them. The path to where the app directs to the main homepage where our content is, this line: `path('', include('travel_wishlist.urls'))`. Within those URL's, they would direct us to the different content of the page such as places visited, about, etc. An example line that would direct us to a place detail page users inputted would be: `path('place/<int:place_primary_key>/',
         views.place_details, name='place_details')` . When users input a place, we store that place in a database, where each place they store also has a built-in unique ID that auto-increments for each new place. Place is also assigned to that user which allows for a security check if the request is not the original user of that place, then we give an `HTTPResponseForbidden()` which is a forbidden response back to the unauthorized user. What was interesting about how I handled getting that place's primary key/id and all the necessary data stored for that place in the database, was getting the object of that place and storing in a separate variable. The function used 
 to get that specific place was called, `get_object_or_404()` from Djanogo's shortcuts library. Where the arguments are the Place model class, and the primary key that the users is requesting. For example, when a user requests a URL like /place/3/, the number 3 is passed to my place_details view as place_primary_key. The `get_object_or_404` function then tries to find a Place object in my database where the primary key (id) is 3. If it finds this object, it is returned and can be used in your view; if not, a 404 page is shown to the user. Now that I've fetched the correct place based on users request for that specific place, I can send that place data to html to render for users to see, using Jinja2 syntax
- **Django's Forms For Users Data Input:** When users want to add a place to a wishlist or visited, I would use Django's forms which would be directed to the Place models, and would allow the user's customized data to be inputted to save to that specific place in the database. For example, to make a new place and initially store it's name and if visited, `class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')`

Screenshot of how the database looks with a few places stored in SQLite3 DB: 

<img width="805" alt="Screenshot 2024-01-26 at 12 36 48 PM" src="https://github.com/JSirisavath/wishlist_app/assets/122318778/388cafa3-5369-4cda-be4f-289fc50a9ef0">
The Meta class inside the ModelForm class is where I specify this relationship and configure certain aspects of the form. So the forms know what models it is working with, in this case, the place model class.

- **Unit and Functional Tests** I decided to add unit tests to test out different key functions in the view and also functional tests within the browser using the Selenium web driver Chrome. However, few tests does not work or function such as the functional tests. There are a few issues that I would need to review and revise.

## Personal Development
- **Data Flow:** In this project, I was able to create something unique to any project I have done, where we allowed users to store information such as details, photos, dates, etc about their favorite places. And being able to handle what to do with users' requests. This involved a lot of planning on how users' data flowed, stored, and retrieved. This helped me gauge how to set up a new MVC project using different technologies, where handling the 
backend and connecting the front end in a structured manner.
- **Project Structure Awareness**  Using the MVC structure for this project, this structure can be carried over in other projects in different technologies, using the same concepts to initially start.

## Future Enhancements
- **Users Own Customizable Profile Section:** I would like to add a section for users to make their own profile where users are able to add their favorite places, a customizable folder to store places they made, and other really neat features. This would mean creating a signup page using few middlewares to handle each unique user.
- **Improve Page Styles and Display:** Improve on UI/UX styles. Integrate Tailwind to HTML pages, adding animations, etc.
- **Add an API Integration To Grab The Most Recommended Places to Visit, YT Vids, Featured Pictures of Places To Visit:** To make the app more unique besides the current functions of the app, integrate a few APIs to the main page to cover more content for users. One example is adding an API to the most top recommended places to visit, and sectioning them by this week, month, year, all time, etc. In addition to adding this API, maybe have an API to be able to find hotels, cheap flights to book, etc so it could be an all-in-one package to book that flight to that place they wished to see. Add a YT API for YT videos, on top 10 places, etc.
- **Add More Features to The Detail Memo Section:** Users can add more details of the traveled place in a separate note section. They can date the details and add more while they are traveling to that place!


## Conclusion
Overall, my experience in developing this app has been immensely educational, providing me with valuable insights into data flow management and the structuring of a project according to the MVC model. The process of learning and implementing Django's framework was both challenging and rewarding. With further refinements and enhancements, I believe this app could evolve into an even more engaging and user-friendly tool, particularly for travelers seeking a seamless and enjoyable experience.

Thank you for your interest in the Travel Wishlist App. Feedback and contributions are highly appreciated!
