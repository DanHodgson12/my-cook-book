# My CookBook

![My CookBook Final Design]()

Visit the deployed site [here]().

---

# User Experience (UX)

## Project Goals

## User Stories

## Colour Scheme

## Typography

## Wireframes

# Features

# Technologies Used

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks, Libraries & Programs

- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used to add icons/images to the computer and player tiles.

- [Codeanywhere](https://app.codeanywhere.com/)
  - Codeanywhere was used for writing, committing and pushing the code to GitHub.

- [Materialize](https://materializecss.com/)
  -Materialize was used to develop a responsive mobile-first design using an assortment of templates.

- [jQuery](https://jquery.com/)
  - jQuery was used as the preferred JavaScript library for HTML document traversal and manipulation, event handling and animation.

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
  - Chrome DevTools was used throughout the development of the website to test ideas and responsiveness, as well as test functionality of the application and debug issues that arose.

- [W3C Markup Validator](https://validator.w3.org/)
  - W3C Markup Validator was used to validate the HTML code.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - W3C CSS Validator was used to validate the CSS code.

- [JSLint](https://www.jslint.com/)
  - JSLint was used to validate the JavaScript.

- [Favicon.io](https://favicon.io/)
  - Favicon.io was used to create the site favicon.

# Testing

A large amount of testing was undertaken throughout the project in order to assess if the application was working as expected.

Friends and family also participated in testing the application's functionality and expressed any concerns or ideas they had with function, layout and user experience.

Please see a detailed breakdown of the testing carried out for this application in [TESTING.md]().

# Finished Product

# Deployment

This website was developed using [Codeanywhere](https://codeanywhere.com/solutions/collaborate), then committed and pushed to GitHub using the Codeanywhere terminal.

## Heroku Deployment

The project was deployed to Heroku using the following steps:

1. Create a `requirements.txt` file using the terminal command:

   ```bash
   pip freeze > requirements.txt
   ```

2. Create a `Procfile` with the terminal command:

   ```bash
   echo web: python app.py > Procfile
   ```

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.
4. Create a new app on the [Herkou website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and assign the region to Europe.
5. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment Method" and select GitHub.
6. Confirm the linking of the Heroku app to the correct GitHub repository.
7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:

    | KEY | VALUE |
    | :-- | :-- |
    | IP | 0.0.0.0 |
    | PORT | 5000 |
    | SECRET_KEY | ANY_SECRET_KEY* |
    | MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>.hrljbrx.mongodb.net/<database_name>?retryWrites=true&w=majority` |
    | DEBUG | TRUE** |

    - *Denotes a value that is specific to your app.

    - **This is set to true to enable us to see any bugs on the live site. __Please change to FALSE after deployment.__

    - To get your MONGO_URI read the MongoDB Atlas documentation [here](https://www.mongodb.com/docs/atlas/getting-started/).

9. In the Heroku dashboard, click "Deploy".
10. In the "Manual Deployment" section of this page, make sure the "Master Branch" is selected and then click "Deploy Branch".

## Local Development

### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [My CookBook](https://github.com/DanHodgson12/my-cook-book).
3. Click the Fork button in the top right corner.

### Making a Local Clone

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [My CookBook](https://github.com/DanHodgson12/my-cook-book).

3. In the "Clone with HTTPs" section, copy the clone URL for the repository.

4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.

5. Type `git clone`, then paste the URL you copied in Step 3, the press Enter:

    ```bash
    git clone https://github.com/DanHodgson12/my-cook-book.git
    ```

6. Install the packages from the requirements.txt file by running the following command in the Terminal:

    ```bash
    pip3 install -r requirements.txt
    ```

7. Your local clone will now be created.

# Credits

## Content

- All content was written by the developer.

## Media

- [Font Awesome](https://fontawesome.com/icons) was used for providing the icons used in the application.
- All other styling and media was created by the developer.

## Code

- [Materialize](https://materializecss.com/getting-started.html) was used throughout to help with responsiveness and styling purposes.
- [W3Schools](https://www.w3schools.com/) & [Stack Overflow](https://stackoverflow.co/teams/) were consulted on a regular basis to help overcome roadblocks in the developer's coding knowledge.

# Acknowledgements

- My family, for their valuable opinions and unconditional support.
- My mentor, Marcel, for his encouraging feedback and patience during my learning journey.
- Code Institute, for its wonderful learning platform and supportive community.
