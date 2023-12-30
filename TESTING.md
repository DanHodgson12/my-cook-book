# Testing

## Testing User Stories

## Tools Testing

- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome DevTools was used throughout the development process to test, explore and make changes to the HTML and CSS of the webpage.
  - Google Chrome DevTools was used throughout the development process to test, explore and make changes to the JavaScript controlling certain elements being utilised from Materialize.

- Responsiveness
  - [Responsive Design Checker](https://www.responsivedesignchecker.com/) was used to check responsiveness across a variety of devices and screen sizes.
  - [Am I Responsive?](https://ui.dev/amiresponsive) was used to check responsiveness across different screen sizes and generate the mockup final image.
  - [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to check responsiveness across different screen sizes during the development and testing phases.

## Compatibility Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail
--- | --- | ---
Google Chrome | No appearance, responsiveness or functionality issues | Pass
Safari | No appearance, responsiveness or functionality issues | Pass
Mozilla Firefox | No appearance, responsiveness or functionality issues | Pass
Microsoft Edge | No appearance, responsiveness or functionality issues | Pass
  
### Device Compatibility

The web application was tested across a wide variety of devices using [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) & [Responsive Design Checker](https://www.responsivedesignchecker.com/) - no appearance, responsiveness or functionality issues were found.

## Common Elements Testing

### Known Bugs

There are no known bugs with the web application.

## Code Validation

The [W3C Markup Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) services were used to check for any code errors or misuse of syntax/elements in the HTML & CSS.

The [JSHint](https://jshint.com/) service was used to check for any code errors or misuse of syntax in the JavaScript.

The [CI Python Linter](https://pep8ci.herokuapp.com/) service was used to check for any linting errors in the Python code.

### HTML

The W3C Markup Validator returned multiple errors and warnings with a lot of the Jinja templating language used. The developer chose to ignore these specific warnings, as this tool is primarily designed to validate static HTML and doesn't recognize server-side templating languages, including Jinja.

Other than the above, there were a few legitimate errors/warnings with the HTML on the following pages:

#### base.html

![base.html](static/images/html-validation-base-page.png)

- This section element contained the flashed messages provided using Jinja templating language. This warning was ignored as the flashed messages performed without issue.

#### add_recipe.html & edit_recipe.html

![add_recipe.html & edit_recipe.html](static/images/html-validation-add-edit-recipe.png)

- These errors showed up for both pages. The code targeted is being used in placeholder text for a text area - the `&#10` makes each piece of text appear on a new line. These errors were ignored as the code performed without issue.

### CSS

The W3C CSS Validator returned no errors in the code.
![CSS Validation](static/images/css-validation.png)

### JavaScript

The JSHint Validation returned a few errors in the code for undefined variables:

- `$` - This was ignored as it is required for functions using jQuery.
- `M` - This was ignored as it is used for initialisation whilst using Materialize.

![JSHint Validation](static/images/jshint-validation.png)

### Python

The CI Python Linter returned no errors in the code.
![Python Validation](static/images/python-validation.png)

## Lighthouse Report

Lighthouse in Google Chrome Dev Tools was used to test performance, accessibility, best practices and search engine optimisation of the webpage.

Suggestions were made to optimise SEO by adding 'meta' tags to each page. However, this was ignored as meta tags were included in the base template and were being duplicated via Jinja.

Page | Report
--- | ---
Home | ![Home Report](static/images/lighthouse-home.png)
Recipes | ![Recipes Report](static/images/lighthouse-recipes.png)
Add Recipe | ![Add Recipe Report](static/images/lighthouse-add-recipe.png)
Edit Recipe | ![Edit Recipe Report](static/images/lighthouse-edit-recipe.png)
Sign In | ![Sign In Report](static/images/lighthouse-sign-in.png)
Register | ![Register Report](static/images/lighthouse-register.png)
Profile | ![Profile Report](static/images/lighthouse-profile.png)