
# Testing Documentation

<br>

>##**Test No. 1**
>>**Description**: Enter an invalid Email and an invalid Password on the Login Page.

>>**Expected Outcome**: It should prompt an error message stating that the login credentials are invalid.

>>**Actual Outcome**: Although it does not login the user if the login credentials are invalid, <br> 
> it does not show an error message. Instead, the login page is shown again for the user to enter valid credentials.

>>**Pass?**: Partially

>>**Comments**: Fixed by Titas Janušonis on 10/01/2022. The message now appears.

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