# The Growth Club Website - Testing details

[Main README.md file](README.md)

[View live version of website via GitHub Pages](http://the-growth-club.herokuapp.com/)

## Testing user stories from the UX section
### **User Stories**
*Guest User*
1. As a Guest User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
    - On the Home page landing section, it is clear what the site is about. In addition to this, the purpose of the site is in the Footer as well.
        - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
        - [Footer](documentation/images/test_screenshots/footer.png)
2. As a Guest User, I want to be met with a visually appealing and easy to read layout of created items;
    - From the landing page and throughout the rest of the web app, the background is light and the text is darker for a modern and visually appealing site. The font is also large to ensure that the site is easy to read.
        - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
3. As a Guest User, I want to view the featured **resources posts** of the month to get a sense of the value if I sign up as a registered user and they don't have to search for it;
    - On the Home page a Guest user is able to see the featured items added by the administrator
        - [Featured section on Home page](documentation/images/test_screenshots/featured_section_landing_page.png)
4. As a Guest User, I want to be able to sign-up to create and edit my own **resource posts**;
    - The user is able to click on the sign up button in the navbar which is clearly indicated in organge. They will then be redirected to the Register page to sign up to view, add, search, edit, bookmark and delete resources. There is also a button on the bottom of the page that will take the user to the log in page where they can log in or click on the registration link to be taken to the registration page. If the user succesfully register, they will see a confirmation message and be take to their Profile page.
        - [Register Page](documentation/images/test_screenshots/register_page.png)
        - [Landing Page](documentation/images/test_screenshots/log_in_button_landing_page.png)
        - [New Registered User confirmation](documentation/images/test_screenshots/new_registered_user_confirmation.png)
5. As a Guest User, I want to be able to get in contact via social media if I like the site or have suggestions.
    - The user is able to get in contact or follow the created or the site on social media as their social links are in the footer on every page of the website.
        - [Footer](documentation/images/test_screenshots/footer.png)

*Registered User*
1. As a Registered User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
    - On the Home page landing section, it is clear what the site is about. In addition to this, the purpose of the site is in the Footer as well.
        - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
        - [Footer](documentation/images/test_screenshots/footer.png)
2. As a Registered User, I want to be met with a visually appealing and easy to read layout of created items;
    - From the landing page and throughout the rest of the web app, the background is light and the text is darker for a modern and visually appealing site. The font is also large to ensure that the site is easy to read.
        - [Landing section on Home page](documentation/images/test_screenshots/landing_section_landing_page.png)
3. As a Registered User, I want to view the featured items of the month so that I don't have to search for them;
    - On the Home page a Registered user is able to see the featured items added by the administrator.
        - [Featured section on Home page]()
4. As a Registered User, I want to be able to log back into the Growth Club with my initial latest credentials;
    - The user can click on the Log In menu link in the navbar to be taken to the log in page where they can use their credentials to log in to view the Club resources. The user will receive a log in confirmation once they have logged in.
        - [Log In Page](documentation/images/test_screenshots/log_in_page.png)
        -[ Log In confirmation](documentation/images/test_screenshots/log_in_welcome_profile_page.png)
5. As a Registered User, I want to be able to view **resource posts** added by other members of the community;
    - The user can go to the Resources page, either by clicking the button on the profile page or in the navbar. On the Resources page the user is able to view all the current resources in the Growth Club library.
        - [Resources Page](documentation/images/test_screenshots/resources_page.png)
6. As a Registered User, I want to be able to create, edit and delete the **resource posts** I have added;
    - On the Resources Page the user is able to click on the "Add Resource" button and will be taken to the Add Resources Page where they can fill in the form and add a resource. The form will have helper text to guide the user as well as validation.
        - [Resources Page](documentation/images/test_screenshots/resources_page.png)
        - [Add Resource Page](documentation/images/test_screenshots/add_resource_page.png)
        - [Resource Added Confirmation](documentation/images/test_screenshots/resource_added_confirmation.png)
    - On the Resources Page the user is able see and edit or delete button if they created the resource, otherwise they will not be able to edit or delete a resource. If the resource is edited, the user will receive confirmation that the resource is edited & updated.
        - [Viewing Edit & Delete Buttons](documentation/images/test_screenshots/delete_edit_buttons.png)
        - [Edit Resource Page](documentation/images/test_screenshots/edit_resource_page.png)
        - [Edit Resource Confirmation](documentation/images/test_screenshots/edit_resource_confirmation.png)
    - If the user clicks on the delete button, they are asked for confirmation before they delete it. If the resource is deleted, the user will receive confirmation that the resource is deleted
        - [Delete Modal](documentation/images/test_screenshots/delete_modal.png)
        - [Delete Resource Confirmation](documentation/images/test_screenshots/delete_resource_confirmation.png)
7. As a Registered User, I would like to be able to search the site so that I can easily find resources that I am looking for;
    - On the Resources The user will be able to type text in the search input field and find resources that have key words in their description. If no resources are found, then the user will see "No results found" and they can reset the search.
        - [Search Field](documentation/images/test_screenshots/resources_search.png)
        - [No search results](documentation/images/test_screenshots/no_results_search.png)
8. As a Registered User, I want to be able to bookmark resources I find interesting;
    - On the Resources pahe, the user is able to bookmark a resource by clicking on the bookmark icon which will turn orange to show it was bookmarked. 
        - [Resource page: Bookmarked Resources](documentation/images/test_screenshots/bookmarked_resource_page.png)
    - If the user has bookmarked resources, it will appear on their profile under the Bookmarks section.
        - [Profile page: Bookmarked Resources](documentation/images/test_screenshots/bookmarked_profile.png)
9. As a Registered User, I want to be able to change my password on my profile;
    - The user is able to change their password if they click on the "Change Password" button on the Profile page. If the user clicked on the Change password button, a modal will open and ask them to type in their new password. If the confirm to change their password, they will recieve a confimration message.
        - [Change Password Button](documentation/images/test_screenshots/change_password_delete_profile_buttons.png)
        - [Change Password Modal](documentation/images/test_screenshots/change_password_modal.png)
        - [Change Password Confirmation](documentation/images/test_screenshots/password_confirmation.png)
10. As a Registered User, I want to be able to delete my account and profile;
    - The user is able to delete their profile from their prodile page. If they click on the "Delete Profile" link a modal will appear where it asks for confimation. The user needs to enter their password and click ont confirmation button which will delete their profile. If their account was successfully deleted, then they will receive a confirmation message and returned to the Home Page.
        - [Delete Profile Button](documentation/images/test_screenshots/change_password_delete_profile_buttons.png)
        - [Delete ProfileModal](documentation/images/test_screenshots/delete_profile_modal.png)
        - [Deleted Profile Confirmation](documentation/images/test_screenshots/delete_profile_confirmation.png)
11. As a Registered User, I want to be able to log out of my account;
    - The user can click on the log out button in the Navbar to log out of their account. They will receive a confirmaiton message if they are logged out of their account successfully and be taken to the Home Page.
    - [Log Out Link](documentation/images/test_screenshots/log_out_link.png)
    - [Log Out Confirmation](documentation/images/test_screenshots/log_out_confirmation.png)
12. As a Registered User, I want to be able to get in contact via social media if I like the site or have suggestions.
    - The user is able to get in contact or follow the created or the site on social media as their social links are in the footer on every page of the website.
        - [Footer](documentation/images/test_screenshots/footer.png)

*Admin User*
- As an Admin User, I would like the ability to **log in to an admin account** so that I can **create, edit and delete featured resources posts** for each month;
    - The log in features are similar to the above, but if the admin user is log in, the are able to see the Manage Resources Admin Dashboard. From here they are able to add & edit feature resources.
        - [Admin Dashboard Page](documentation/images/test_screenshots/admin_dashboard.png)
    - The admin user can add a featured resource by clicking on the "Add featured resource" button which will take them to the Add Featured Resource page where they can fill in the form and add a resource. The form will have helper text to guide the user as well as validation. The user will recieve confirmation if the featured resource is added to the Home page Featured Section.
        - [Add Featured Resouces Page](documentation/images/test_screenshots/add_featured_resource.png)
        - [Add Featured Resource Confirmation](documentation/images/test_screenshots/add_featured_resource_confirmation.png)
    - The admin user can click on the "Edit or Delete Featured Resource" button on the Admin Dashboard and will be taked to the Featued Resource section on the Home page where they will be able to view Edit & Delete buttons. 
        - [Featured Section on Home Page Admin View]()
    - If the edit button is clicked, the user will be taken to the Edit Featured Resource page. If the featured resource is successfully update, they will receive a confirmation message.
        - [Edit Featured Resouces Page](documentation/images/test_screenshots/edit_featured_resource_page.png)
        - [Edit Featured Resource Confirmation](documentation/images/test_screenshots/edit_featured_resource_confirmation.png)
    - If the delete button is clicked, a delete confirmation modal will display. If the featured resource is successfully deleted, they will receive a confirmation message.
        - [Delete Featured Resource Modal](documentation/images/test_screenshots/delete_featured_resource_modal.png)
        - [Delete Featured Resource Confirmation](documentation/images/test_screenshots/delete_featured_resource_confirmation.png)
- As an Admin User, I want to be able to view all **resource posts** added by other members of the community;
- As an Admin User, I would like the ability to **edit or delete any resource posts** so that I can **maintain the site to stay updated**;



##  Testing and Validation of website

### [Link Checker](https://validator.w3.org/checklink)
To check that all links are working and not broken.
* **Result**
   
* **Fix**  


### Lighthouse (Google dev tool)
To test the accessibility and performance of the website.
* **Result**
    
* **Fix** 
    
    
- Final version: 
![Lighthouse report ]()

### [Responsinator](http://www.responsinator.com/)
To test the responsiveness of the live website and functionalities on different size mobile devices.
* **Result**
    
* **Fix** 
   
- Final version: [To view site on Responsinator ]()

### [Am I Responsive](http://ami.responsivedesign.is/)
To view images of the website on different devices.
* **Result**

- Final version: ![Am I Responsive ]()

### [JSHint](https://jshint.com/)
To detect errors and potential problems in your JavaScript code.
* **Result**
    
* **Fix** 
    
- Final version: no errors for () if add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.

### [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
To validate the CCS code of the project.
* **Result**
    
* **Fix** 
- Final version: 
- ![CSS Validation]()

### [W3C Markup Validation](https://validator.w3.org/)
To validate the HTML code of the project.
* **Result**
    
* **Fix** 
   
- Final version: no errors or warnings for )
- ![HTMl Validation]()

### Google Dev Tool 
To check for errors in JavaScript code
* **Result**

* **Fix** 

- Final version: no errors or warnings 
- ![Google Dev Tool]()

## Manual testing of all elements and functionality on every page

## Further testing: 
