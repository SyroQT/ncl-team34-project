
# Testing Documentation

<br>

>##**Test No. 1**
>>**Description**: Enter an invalid Email or/and an invalid Password on the Login Page.

>>**Expected Outcome**: It should prompt an error message stating that the login credentials are invalid.

>>**Actual Outcome**: Although it does not login the user if the login credentials are invalid, <br> 
> it does not show an error message. Instead, the login page is shown again for the user to enter valid credentials.

>>**Pass?**: Partially

>>**Comments**: Fixed by Titas Janušonis on 10/01/2022. The following messages now appear: <br> 'EMAIL_NOT_FOUND' or 'INVALID_PASSWORD'

<br>
<br>

>##**Test No. 2**
>>**Description**: Enter a valid registered Email and Password on the Login page.

>>**Expected Outcome**: The user will be logged in and the user page will appear on the screen.

>>**Actual Outcome**: The user is logged in and the user page appears on the screen.

>>**Pass?**: Yes

>>**Comments**:

<br>
<br>

>##**Test No. 3**
>>**Description**: Register button on Login page clicked.

>>**Expected Outcome**: A registration form must appear for a user to register.

>>**Actual Outcome**: A registration form appears so that a user can register.

>>**Pass?**: Yes

>>**Comments**:

<br>
<br>

>##**Test No. 4**
>>**Description**: Next button on Register page clicked.

>>**Expected Outcome**: A newly registered user is logged in and the user page must appear.

>>**Actual Outcome**: The registered user is logged in and the user page appears.

>>**Pass?**: Yes

>>**Comments**:

<br>
<br>

>##**Test No. 5**
>>**Description**: Logout button clicked.

>>**Expected Outcome**: The user will be logged out and the Login page should appear.

>>**Actual Outcome**: The user is logged out and is redirected to the Login page.

>>**Pass?**: Yes

>>**Comments**:

<br>
<br>

>##**Test No. 6**
>>**Description**: Visiting the admin page as a user.

>>**Expected Outcome**: A normal user who is not an admin must not be able <br> to access the admin page.

>>**Actual Outcome**: A non-admin user who tries to access the admin <br> page sees a message saying ‘Unauthorized.’ 

>>**Pass?**: Yes

>>**Comments**:

<br>
<br>

>##**Test No. 7**
>>**Description**: While registering, input an integer in the first name <br>
> or the last name and click next after filling all the other details in the form.

>>**Expected Outcome**: A user will not be registered and will be <br> 
> prompted to reenter their first name or last name since a name <br>
> cannot contain an integer as it is not an alphabet.

>>**Actual Outcome**: A user is prompted back to the register form <br>
> and is not allowed to register with an invalid name.

>>**Pass?**: Yes

>>**Comments**:

<br>
<br>

>##**Test No. 8**
>>**Description**: Try to register without filling the <br> 
> entire registration form, i.e leaving at least one field blank.

>>**Expected Outcome**: The user will be asked to fill <br> 
> the field before continuing, since all the fields are required to be filled.

>>**Actual Outcome**: The user is asked to fill the field before continuing.

>>**Pass?**: Yes

>>**Comments**:


<br>
<br>

>##**Test No. 9**
>>**Description**: Enter an invalid URL by manually <br> 
> typing the URL.

>>**Expected Outcome**: URL will not be found and an <br> 
> error message will be shown.

>>**Actual Outcome**: The URL was not found and the following <br>
> error message appeared: "The requested URL was not found on the server. <br> 
> If you entered the URL manually please check your spelling and try again."

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 10**
>>**Description**: Visit the admin page as an admin.

>>**Expected Outcome**: The admin page will appear and the admin <br>
> will be able to access the admin rights i.e viewing admin tools.

>>**Actual Outcome**: The admin page appears and the admin can view issues, <br>
> delete issues as well as click and view admin tools.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 11**
>>**Description**: Try deleting an issue as an admin.

>>**Expected Outcome**: The issue will be deleted and removed <br>
> from the map.

>>**Actual Outcome**: The issue was deleted and removed from the map.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 12**
>>**Description**: Register with an already registered email address.

>>**Expected Outcome**: An error message will appear telling the user <br>
> that the email is already in use.

>>**Actual Outcome**: An error message appears which states "EMAIL_EXISTS" <br>
> and the register page is shown for the user to register with a different email.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 13**
>>**Description**: Register with a weak password i.e a password <br>
> which contains only one character or no special characters.

>>**Expected Outcome**: An error message will appear telling the user <br>
> that the password they entered is weak or invalid.

>>**Actual Outcome**: An error message appears which states <br>
> "Password must be between 6 and 12 characters in length. <br>
> Password must contain at least 1 small letter, 1 capital letter, 1 digit and 1 special character."
> and the register page is shown for the user to register with a different password.

>>**Pass?**: Yes

>>**Comments**:

 
<br>


##**Test No. 14**
>>**Description**: While registering, enter passwords that <br>
> do not match i.e enter two different passwords and try to register.

>>**Expected Outcome**: An error message will appear telling the user <br>
> that the passwords do not match.

>>**Actual Outcome**: An error message appears which states: <br>
> "Both password fields must be equal!"

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 15**
>>**Description**: Register with an invalid phone number <br>
> by entering a phone number of an invalid length i.e only one or two digits.

>>**Expected Outcome**: An error message will appear telling the user <br>
> that the phone number is invalid.

>>**Actual Outcome**: The user is registered and the user page appears.

>>**Pass?**: No

>>**Comments**:
 
<br>


##**Test No. 16**
>>**Description**: Enter a character that is not a digit <br>
> in the phone number field on the register page i.e enter a letter.

>>**Expected Outcome**: Either an error message will appear or the user <br>
> cannot enter any invalid characters.

>>**Actual Outcome**: The user is not allowed to type an invalid character <br>
> in the phone number field.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 17**
>>**Description**: On the user page, click on a part of the map.

>>**Expected Outcome**: The user will be able to create an issue.

>>**Actual Outcome**: A 'Create a new issue' pop up appears, allowing <br>
> the user to create an issue with the description. The user can also choose <br>
> the category of the issue.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 18**
>>**Description**: Create a new issue and submit.

>>**Expected Outcome**: The created issue should appear on the map.

>>**Actual Outcome**: The created issue appears on the map.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 19**
>>**Description**: Up vote or down vote an issue on the map.

>>**Expected Outcome**: The vote will be counted and the new <br>
> number of votes will be shown on the issue.

>>**Actual Outcome**: The vote was counted and the new number <br>
> of votes was shown on the issue.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 20**
>>**Description**: As an admin, check if the new issue <br>
> created by the new user is visible.

>>**Expected Outcome**: The new issue will appear <br>
> on the admin page.

>>**Actual Outcome**: The new issue appears and the admin <br>
> can see the issue description and the votes.

>>**Pass?**: Yes

>>**Comments**:
 
<br>


##**Test No. 21**
>>**Description**: As an admin, go through the admin tools.

>>**Expected Outcome**: The admin can check every category <br>
> and view issues from each category.

>>**Actual Outcome**: The admin is able to check every category <br>
> and all the issues from each of the category are visible to the admin.

>>**Pass?**: Yes

>>**Comments**: