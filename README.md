# Travel Wishlist App

Developer: Jerry Sirisavath

Initial Commit To Github: 11-04-23

## Introduction

The Travel Wishlist is a Full-Stack app that allows users to document and note down places they have traveled to or make a wishlist of places they want to travel to! Additionally, users can have a customizable review for their traveled places with the ability to write down their thoughts, upload their favorite picture, and add a start date traveled about that place. Users can also come back and edit that traveled place or delete it! This Full-Stack app uses Django Framework, Python, Javascript, HTML, and a simple predeveloped CSS framework, watercss. 


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
7. After logging in, you should now see the home page of the app. If you  want to stop the app running on your browser, on terminal in your editor, run this command: 
- MacOS & Windows:`CTRL + C`



## Features

- **Add a travel place to a wishlist or visited:** Users can input a desired place in the textbox, and if the place has been visited, they can check visited box else, add it to the wishlist. User's are can also delete or edit a place.
- **Dynamic Data Management:** Utilizes djangos class models that are connected to the database. For example, after defining the Place class for models, we need to set up the migrations (create/modifying an instructions on how to create DB table to handle this information) to do so, run 'python manage.py makemigrations' and run 'python manage.py migrate' to ask the db to create that table
- **User-Friendly Interface:** Designed with a focus of easier user experience and UI menu.


## Screenshots 




## Technical Insights



## Personal Development



## Future Enhancements


## Conclusion


Thank you for your interest in the Travel Wishlist App. Feedback and contributions are highly appreciated!
