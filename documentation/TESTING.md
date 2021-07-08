# The Growth Club Website - Testing details

[Main README.md file](README.md)

[View live version of website via Heroku](https://the-growth-club.herokuapp.com/)
___
<br>

## **Testing user stories from the UX section**
### **User Stories**
#### *Guest User*
1. As a Guest User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
- On the Home page landing section, it is clear what the site is about. In addition to this, the purpose of the site is in the Footer as well.
   - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
   - [Footer](documentation/images/test_screenshots/footer.png)
2. As a Guest User, I want to be met with a visually appealing and easy to read layout of created items;
- From the landing page and throughout the rest of the web app, the background is light and the text is darker for a modern and visually appealing site. The font is also large to ensure that the site is easy to read.
   - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
3. As a Guest User, I want to view the featured **resources posts** of the month to get a sense of the value if I sign up as a registered user and they don't have to search for it;
- On the Home page a Guest user can see the featured items added by the administrator
   - [Featured section on Home page](documentation/images/test_screenshots/featured_section_landing_page.png)
4. As a Guest User, I want to be able to sign-up to create and edit my own **resource posts**;
- The user can click on the signup button in the navbar which is indicated in orange. They will then be redirected to the Register page to sign up to view, add, search, edit, bookmark and delete resources. There is also a button on the bottom of the page that will take the user to the login page where they can log in or click on the registration link to be taken to the registration page. If the user successfully registers, they will see a confirmation message and be taken to their Profile page.
   - [Register Page](documentation/images/test_screenshots/register_page.png)
   - [Landing Page](documentation/images/test_screenshots/log_in_button_landing_page.png)
   - [New Registered User confirmation](documentation/images/test_screenshots/new_registered_user_confirmation.png)
5. As a Guest User, I want to be able to get in contact via social media if I like the site or have suggestions.
- The user can get in contact or follow the created or the site on social media as their social links are in the footer on every page of the website.
   - [Footer](documentation/images/test_screenshots/footer.png)

#### *Registered User*
1. As a Registered User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
- On the Home page landing section, it is clear what the site is about. In addition to this, the purpose of the site is in the Footer as well.
   - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
   - [Footer](documentation/images/test_screenshots/footer.png)
2. As a Registered User, I want to be met with a visually appealing and easy to read layout of created items;
- From the landing page and throughout the rest of the web app, the background is light and the text is darker for a modern and visually appealing site. The font is also large to ensure that the site is easy to read.
   - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
3. As a Registered User, I want to view the featured items of the month so that I don't have to search for them;
 - On the Home page a Registered user can see the featured items added by the administrator.
   - [Featured section on Home page](documentation/images/test_screenshots/featured_section_landing_page_registered_user.png)
4. As a Registered User, I want to be able to log back into the Growth Club with my initial latest credentials;
- The user can click on the login menu link in the navbar to be taken to the login page where they can use their credentials to log in to view the Club resources. The user will receive a login confirmation once they have logged in.
   - [Log In Page](documentation/images/test_screenshots/log_in_page.png)
   - [ Log In confirmation](documentation/images/test_screenshots/log_in_welcome_profile_page.png)
5. As a Registered User, I want to be able to view **resource posts** added by other members of the community;
- The user can go to the Resources page, either by clicking the button on the profile page or in the navbar. On the Resources page, the user can view all the current resources in the Growth Club library.
   - [Resources Page](documentation/images/test_screenshots/resources_page.png)
6. As a Registered User, I want to be able to create, edit and delete the **resource posts** I have added;
- On the Resources Page the user can click on the "Add Resource" button and will be taken to the Add Resources Page where they can fill in the form and add a resource. The form will have helper text to guide the user as well as validation.
   - [Resources Page](documentation/images/test_screenshots/resources_page.png)
   - [Add Resource Page](documentation/images/test_screenshots/add_resource_page.png)
   - [Resource Added Confirmation](documentation/images/test_screenshots/resource_added_confirmation.png)
- On the Resources Page the user can see an edit or delete button if they created the resource, otherwise, they will not be able to edit or delete a resource. If the resource is edited, the user will receive confirmation that the resource is edited & updated.
   - [Viewing Edit & Delete Buttons](documentation/images/test_screenshots/delete_edit_buttons.png)
   - [Edit Resource Page](documentation/images/test_screenshots/edit_resource_page.png)
   - [Edit Resource Confirmation](documentation/images/test_screenshots/edit_resource_confirmation.png)
- If the user clicks on the delete button, they are asked for confirmation before they delete it. If the resource is deleted, the user will receive confirmation that the resource is deleted
   - [Delete Modal](documentation/images/test_screenshots/delete_modal.png)
   - [Delete Resource Confirmation](documentation/images/test_screenshots/delete_resource_confirmation.png)
7. As a Registered User, I would like to be able to search the site so that I can easily find resources that I am looking for;
- On the Resources The user will be able to type text in the search input field and find resources that have keywords in their description. If no resources are found, then the user will see "No results found" and they can reset the search.
   - [Search Field](documentation/images/test_screenshots/resources_search.png)
   - [No search results](documentation/images/test_screenshots/no_results_search.png)
8. As a Registered User, I want to be able to bookmark resources I find interesting and remove a bookmark.
- On the Resources page, the user can bookmark a resource by clicking on the bookmark icon which will turn orange to show it was bookmarked. 
   - [Resource page: Bookmarked Resources](documentation/images/test_screenshots/bookmarked_resource_page.png)
- If the user has bookmarked resources, it will appear on their profile under the Bookmarks section.
   - [Profile page: Bookmarked Resources](documentation/images/test_screenshots/bookmarked_profile.png)
- If the user wants to remove the bookmark they can click on the "x" button and the resource will be removed, they will receive a confirmation message.
   - [Profile Page: Removed Bookmark confirmation](documentation/images/test_screenshots/bookmark_remove_confirmation.png)
9. As a Registered User, I want to be able to change my password on my profile;
- The user can change their password if they click on the "Change Password" button on the Profile page. If the user clicked on the Change password button, a modal will open and ask them to type in their new password. If they confirm to change their password, they will receive a confirmation message.
   - [Change Password Button](documentation/images/test_screenshots/change_password_delete_profile_buttons.png)
   - [Change Password Modal](documentation/images/test_screenshots/change_password_modal.png)
   - [Change Password Confirmation](documentation/images/test_screenshots/password_confirmation.png)
10. As a Registered User, I want to be able to delete my account and profile;
- The user can delete their profile from their profile page. If they click on the "Delete Profile" link a modal will appear where it asks for confirmation. The user needs to enter their password and click on the confirmation button which will delete their profile. If their account was successfully deleted, then they will receive a confirmation message and returned it to the Home Page.
   - [Delete Profile Button](documentation/images/test_screenshots/change_password_delete_profile_buttons.png)
   - [Delete ProfileModal](documentation/images/test_screenshots/delete_profile_modal.png)
   - [Deleted Profile Confirmation](documentation/images/test_screenshots/delete_profile_confirmation.png)
11. As a Registered User, I want to be able to log out of my account;
 - The user can click on the log out button in the Navbar to log out of their account. They will receive a confirmation message if they are logged out of their account successfully and be taken to the Home Page.
   - [Log Out Link](documentation/images/test_screenshots/log_out_link.png)
   - [Log Out Confirmation](documentation/images/test_screenshots/log_out_confirmation.png)
12. As a Registered User, I want to be able to get in contact via social media if I like the site or have suggestions.
 - The user can get in contact or follow the created or the site on social media as their social links are in the footer on every page of the website.
   - [Footer](documentation/images/test_screenshots/footer.png)

#### *Admin User*
The Admin user the same user stories as the Registered user above with the additional extras below:
1. As an Admin User, I would like the ability to **log in to an admin account** so that I can **create, edit and delete featured resources posts** for each month;
- The login features are similar to the above, but if the admin user is logged in, they can see the Manage Resources Admin Dashboard. From here they can add & edit feature resources.
   - [Admin Dashboard Page](documentation/images/test_screenshots/admin_dashboard.png)
- The admin user can add a featured resource by clicking on the "Add featured resource" button which will take them to the Add Featured Resource page where they can fill in the form and add a resource. The form will have helper text to guide the user as well as validation. The user will receive confirmation if the featured resource is added to the Home page Featured Section.
   - [Add Featured Resouces Page](documentation/images/test_screenshots/add_featured_resource.png)
   - [Add Featured Resource Confirmation](documentation/images/test_screenshots/add_featured_resource_confirmation.png)
- The admin user can click on the "Edit or Delete Featured Resource" button on the Admin Dashboard and will be taken to the Featured Resource section on the Home page where they will be able to view Edit & Delete buttons. 
   - [Featured Section on Home Page Admin View](documentation/images/test_screenshots/featured_resources_admin_view.png)
- If the edit button is clicked, the user will be taken to the Edit Featured Resource page. If the featured resource is successfully updated, they will receive a confirmation message.
   - [Edit Featured Resouces Page](documentation/images/test_screenshots/edit_featured_resource_page.png)
   - [Edit Featured Resource Confirmation](documentation/images/test_screenshots/edit_featured_resource_confirmation.png)
- If the delete button is clicked, a delete confirmation modal will display. If the featured resource is successfully deleted, they will receive a confirmation message.
   - [Delete Featured Resource Modal](documentation/images/test_screenshots/delete_featured_resource_modal.png)
   - [Delete Featured Resource Confirmation](documentation/images/test_screenshots/delete_featured_resource_confirmation.png)
2. As an Admin User, I want to be able to view all **resource posts** added by other members of the community as well as the ability to **edit or delete any resource posts** so that I can **maintain the site to stay updated**
- The admin user can view all resources and also the edit & delete buttons. They can edit or delete any resource regardless of who added the resource.
    -[Admin User View of Resource Page](documentation/images/test_screenshots/resource_page_view_admin.png)
___
<br>

##  **Testing and Validation of website**
### [Link Checker](https://validator.w3.org/checklink)
- To check that all links are working and not broken. 
- [Link Validation Test](documentation/images/validator_screenshots/linkchecker.png)
   - Issue with https://fonts.googleapis.com/ in the header of the base template but this directly copied and pasted from the Google Fonts website to use a font. Therefore this can be safely ignored.
   - Issue with Linkedin link was manually checked and resolved.
   - Issue with Instagram link was manually checked and resolved.
- Final version has no other link errors or warnings.

### Lighthouse (Google dev tool)
- To test the accessibility and performance of the website. 
- Final version: 
[Lighthouse report ]()

### [Responsinator](http://www.responsinator.com/)
- To test the responsiveness of the live website and functionalities on different size mobile devices.
- Final version: 
   - [Mobile view ](documentation/images/validator_screenshots/responsinator_mobile.png)
   - [Tablet view ](documentation/images/validator_screenshots/responsinator_tablet.png)

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
- Final version: [Am I Responsive ](documentation/images/validator_screenshots/am_i_responsive_design.png)

### JavaScript
- [JSHint](https://jshint.com/)
   - [Test JavaScript Validation](documentation/images/validator_screenshots/jshint_test.png)
   - [Final JavaScript Validation](documentation/images/validator_screenshots/jshint_final.png)
   - Final version - addressing errors and warnings: 
      - Warning for ''let' is available in ES6 (use 'esversion: 6'). Can be safely ignored. If add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored. 
- [JSEsprima](https://esprima.org/)
   - [Final JavaScript Validated](documentation/images/validator_screenshots/js_esprima_final.png)

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CCS code of the project pasting code in by direct input method.
- Final version - addressing errors and warnings: 
   - The Validator states there is an error with regards to the "text-decoration-thickness" but this is acceptable according to [w3.org](https://www.w3.org/TR/css-text-decor-4/#propdef-text-decoration-thickness) and [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-thickness). This property, sets the stroke thickness of underlines, overlines, and line-throughs specified on the element with text-decoration-line, and affects all decorations originating from this element even if descendant boxes specify a different thickness. Therefore, it can be safely ignored.
   - 8 warnings relating to custom colour variables. The W3C CSS validator cannot parse :root variables. Therefore it can be safely ignored.
   - Warnings for vendor extensions suggested by AutoPrefixer is valid to ensure CSS styles can work across multiple browsers, can be safely ignored.
- [Final CSS Validation](/documentation/images/validator_screenshots/CSS_validator_final.png)

### [HMTL: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- Final version: no errors or warnings
- Testing and Final results per page:
   - Error Pages - No Errors in testing and finally
      - [Error Pages Final](documentation/images/validator_screenshots/HTML_validator_404_page_test.png)
   - Add Category Page - No Errors in testing and finally
      - [Add Category Page - Final](documentation/images/validator_screenshots/HTML_validator_add_category_page_test.png)
   - Add Featured Resources Page - Some errors in testing and no errors finally
      - [Add Featured Resources Page - Test](documentation/images/validator_screenshots/HTML_validator_add_featured_resource_page_test.png)
      - [Add Featured Resources Page - Final](documentation/images/validator_screenshots/HTML_validator_add_featured_resource_page_final.png)
   - Add Resources Page - Some errors in testing and no errors finally
      - [Add Resources Page - Test](documentation/images/validator_screenshots/HTML_validator_add_resource_page_test.png)
      - [Add Resources Page - Final](documentation/images/validator_screenshots/HTML_validator_add_resource_page_final.png)
   - Add Resources Page - Some errors in testing and no errors finally
      - [Add Resources Page - Test](documentation/images/validator_screenshots/HTML_validator_add_resource_page_test.png)
      - [Add Resources Page - Final](documentation/images/validator_screenshots/HTML_validator_add_resource_page_final.png)
   - Add Topic Page - No Errors in testing and finally
      - [Add Topic Page - Final](documentation/images/validator_screenshots/HTML_validator_add_topic_page_test.png)
   - Add Admin Dashboard Page - Some errors in testing and no errors finally
      - [Add Admin Dashboard Page - Test](documentation/images/validator_screenshots/HTML_validator_admin_dashboard_page_test.png)
      - [Add Admin Dashboard Page - Final](documentation/images/validator_screenshots/HTML_validator_admin_dashboard_page_final.png)
   - Edit Category Page - No Errors in testing and finally
      - [Edit Category Page  - Final](documentation/images/validator_screenshots/HTML_validator_edit_category_page_test.png)
   - Edit Featured Resource Page - Some errors in testing and no errors finally
      - [Edit Featured Resource Page - Test](documentation/images/validator_screenshots/HTML_validator_edit_featured_resource_page_test.png)
      - [Edit Featured Resource Page - Final](documentation/images/validator_screenshots/HTML_validator_edit_featured_resource_page_final.png)
   - Edit Resource Page - Some errors in testing and no errors finally
      - [Edit Resource Page - Test](documentation/images/validator_screenshots/HTML_validator_edit_resource_page_test.png)
      - [Edit Resource Page - Final](documentation/images/validator_screenshots/HTML_validator_edit_resource_page_final.png)
   - Edit Topic Page - No Errors in testing and finally
      - [Edit Topic Page  - Final](documentation/images/validator_screenshots/HTML_validator_edit_topic_page_test.png)
   - Home Page - Some errors in testing and no errors finally
      - [Home Page - Test](documentation/images/validator_screenshots/HTML_validator_home_page_test.png)
      - [Home Page - Final](documentation/images/validator_screenshots/HTML_validator_edit_resource_page_final.png)
   - Log In Page - No Errors in testing and finally
      - [Log In Page - Final](documentation/images/validator_screenshots/HTML_validator_login_page_test.png)
   - Profile Page - Some errors in testing and no errors finally
      - [Profile Page - Test](documentation/images/validator_screenshots/HTML_validator_profile_page_final.png)
      - [Profile Page - Final](documentation/images/validator_screenshots/HTML_validator_profile_page_final.png)
   - Register Page - No Errors in testing and finally
      - [Register Page - Final](documentation/images/validator_screenshots/HTML_validator_register_page_test.png)
   - Resource Page - Some errors in testing and no errors finally
      - [Resource Page - Test](documentation/images/validator_screenshots/HTML_validator_resource_page_final.png)
      - [Resource Page - Final](documentation/images/validator_screenshots/HTML_validator_resource_page_test.png)

### Python
- [Extendsclass](https://extendsclass.com/python-tester.html) - No syntax errors
   - [Final Python Validated](documentation/images/validator_screenshots/python_extendsclass_final.png)
- [PEP8 Online](http://pep8online.com/) - Pythoon file is PEP8 compliant
   - [Final Python Validated](documentation/images/validator_screenshots/python_pep8online_final.png)

### Google Dev Tool 
- To check for errors in JavaScript code
- Final version: no errors or warnings 

### Browser Compatibility
To ensure a broad range of users can successfully use this site, I tested it across the 6 major browsers in both desktop and mobile configuration. See the [Browser Compatibility Table](documentation/images/validator_screenshots/browser_compatibility_table.png) for more detail. The following browsers were tested:
- Chrome
- Firefox 
- Safari
- Opera
- Edge

___
<br>

## **Manual testing of all elements and functionality on every page**
1. Logo - click on the logo, returns to the “Home” section on all pages.
2. Navbar 
   - if *any user* click on the Home link - go to the Home page on all pages
   - if *Guest user* click on Login link - got to Login page
   - if *Guest user* click on Sign Up link - go to Register page 
   - if *Registered user* click on Resource link - go to the Resources page
   - if *Registered user* click on Profile link - go to the Profile page
   - if *Registered user* click on the Log Out link - log the user out and go to the Home page
   - if *Admin user* click on Admin Dashboard link - go to Admin Dashboard page
3. Footer 
   - if *any user* click on the Instagram link - go to Franciska Du Toit's Instagram page
   - if *any user* click on the LinkedIn link - go to Franciska Du Toit's LinkedIn page
   - if *any user* click on the Twitter link - go to Franciska Du Toit's Twitter page
   - if *any user* click on the GitHub link - go to Franciska Du Toit's GitHub page
4. Floating to top button 
   - if click the float to top button, moves the view back up to the top of the page.
5. Landing Page
   - if *any user* click on the "View Featured Resources of Month" Button - go to the Featured section at the bottom of the Home page
   - if *any user* click on each Featured Resource card "Visit Resource" button - go to the correct Resource external page
   - if *Guest user* click on "Log In to View More Resources" button - got to Login page
   - if *Registered user* click on the "View More Resources" button - go to the Resources page
6. Registration & Sign Up Page
   - if *Guest user* type in "Username", "Email" and "Password" fields - validation is given if correct and feedback is given if incorrect.
      - if click on the "Sign Up" button" user is added to the database, go to the profile page and feedback is given to the user that they are registered
   - if *any user* click on the "Login Here" link - go to the Login page
7. Log in Page
   - if *Registered users* type in their user details in the "Username" and "Password" fields validation is given if correct and feedback is given if incorrect.
      - if click on the "Login" button" the user is logged in, go to the profile page and feedback is given to the user that they are now logged in.
   - if *any user* click on the "Create an account here!" link - go to the Registration page
8. Profile Page 
   - if *Registered user* clicks on the "View Club Resources" button - go to Resources Page
   - if *Registered user* clicks on the "View Featured Resources" button - go to Home Page
   - if *Registered user* clicks on the "Change Password" button - open modal to change the password
      - if type in a new password and click the "Change password" button - the password is changed in the database and a success message is given to the user
      - if click on "Cancel" go back to a Profile page
   - if *Registered user* clicks on the "Click here to delete your profile" link - open modal to delete the account
      - if type in the password and click the "Delete my account forever" button - the account is deleted in the database and a success message is given to the user.
      - if click on "Cancel" go back to a Profile page
9. Resources Page
   - if *Registered user* type text in the search field and click on the "Search" button", the relevant matching resource is shown. If there are no matching resources, the user is notified to try again. 
   - if click on the "Reset" button, the search field is reset.
   - if *Registered user* clicks on "Add Resource" - go to the Add Resource page 
   - if *Registered user* clicks on each Resource card "Visit Resource" button - go to the correct Resource external page
   - if *Registered user* created the resource view Edit & Delete buttons
      - if the user clicks on each Resource card "Delete" Button - open modal to confirm delete resource. If the user clicks on the "Delete" button, the resource is deleted, removed from the database and the user gets a confirmation. If the user clicks on the "Cancel" button the modal is closed.
      - if the user clicks on each Resource card "Edit" Button - go to the Edit Resource page
   - if *Registered user* clicks on the bookmark button, the resource is added to their profile, the button changes to orange and a feedback message is given
10. Add Resource Page
   - if *Registered user* click on "Choose Category" and "Choose Topic" they can select a current category or topic.
   - if *Registered user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Registered user* wants to select a date, a date picker opens with the current date and a date can be selected.
   - if *Registered user* click on the "Add Resource" button, a new resource is added to the database and a success message is given to the user.
   - if *Registered user* click on cancel - go to Resources Page
11. Edit Resource Page
   - view current details of resource
   - if click on "Choose Category" and "Choose Topic" they can select a current category or topic.
   - if type in text in fields, validation is given if correct and feedback is given if incorrect.
   - if want to select a date, a date picker opens with the current date and a date can be selected.
   - if click on the "Update Resource" button, the resource is updated in the database and a success message is given to the user.
   - if click on cancel - go to the Resources Page
12. Manage Resource Admin Dashboard Page
   - if *Admin user* click the "Add new Featured resource" button, go to Add Featured resource page. 
   - if *Admin user* click the "Delete or Edit Featured resource" button, go to the Home page.
   - if *Admin user* click the info button, open info modal about Featured resources
   - if *Admin user* click the "Add Category" button, go to Add Category page. 
   - if *Admin user* click the "Edit" button in the Category section, go Edit Category page.
   - if *Admin user* click the "Delete" button in the Category section, the delete modal opens.
   - if click on cancel - close modal
   - if click on the "Delete" button, the category is deleted and a success message appears.
   - if *Admin user* click the info button, open info modal about Categories.
   - if *Admin user* click the "Add Topic" button, go to Add Topic page. 
   - if *Admin user* click the "Edit" button in the Topic section, go to the Edit Topic page.
   - if *Admin user* click the "Delete" button in the Topic section, the delete modal opens.
   - if click on cancel - close modal
   - if click on the "Delete" button, the Topic is deleted and a success message appears.
   - if *Admin user* click the info button, open info modal about Topics.
13. Add Featured Resource Page 
   - if *Admin user* click on "Choose Category" and "Choose Topic" they can select a current category or topic.
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* wants to select a date, a date picker opens with the current date and a date can be selected.
   - if *Admin user* click on the "Add Featured Resource" button, a new featured resource is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page
14. Add New Category page
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* click on the "Add Category" button, a new category is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page
15. Edit Category page
   - view current details of category
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect. 
   - if *Admin user* click on the "Update Category" button, the category is updated in the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page
16. Add New Topic page
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* click on the "Add Topic" button, a new Topic is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page
17. Edit Topic page
   - view current details of category
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect. 
   - if *Admin user* click on the "Update Topic" button, the Topic is updated in the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page

## **Further testing** 
- Usability tests were done with two users to analyse the User Experience. The feedback from the users were very helpful to determine what works, what can be improved and determine future features.  
- Asked fellow students, friends and family to look at the site on their devices and report any issues they find.
- Viewed the website on several devices, no further issues found.
- Review all functionality and responsiveness on different desktop browsers and the website displayed correctly in all browsers including Safari, Chrome, Edge, Firefox and Opera browsers. (see Browser Compatibility section for detail)

## **Deployment**
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable in app.py file is set to False.
- Confirmed that there is no difference between the deployed version and the development version.