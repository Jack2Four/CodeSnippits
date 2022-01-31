#####################
#     Constants     #
#####################
global_image_location = 'matplotlib_images/'
image_location1 = f'{global_image_location}Graph1.png'

# matplotlib stuff

#############################
#          Graph 1          #
#############################
def Graph1():
    salesdata = pd.read_excel("Sales_csv.xlsx")
    plt.figure(figsize=(10,10))
    plt.bar(salesdata["Product"], salesdata["Profit"])
    plt.title('Tracking Groups Steps')
    plt.xlabel("Product")
    plt.ylabel("Profit")
    plt.xticks(rotation=90)
    plt.savefig(image_location1)
    plt.close()
    PictureGraph1.value = image_location1
    PictureGraph1.height = GraphSize
    PictureGraph1.width = GraphSize

#################################
#           Light Mode          #
#################################
def LightMode():
    # lighter theme for users with eyesight that means they cant look at a dark screen.
    app.bg = "#F4F4F4"
    CustomerLoginSignUpPage.bg = "#F4F4F4"
    CustomerLoginPage.bg = "#F4F4F4"
    CustomerSignUpPage.bg = "#F4F4F4"
    CustomerProductsPage.bg = "#F4F4F4"
    CustomerMessagingPage.bg = "#F4F4F4"
    EmployeeLoginPage.bg = "#F4F4F4"
    EmployeeDashboardPage.bg = "#F4F4F4"
    EmployeeProductsPage.bg = "#F4F4F4"
    EmployeeCustomersPage.bg = "#F4F4F4"
    EmployeeMessagingPage.bg = "#F4F4F4"

################################
#           Dark Mode          #
################################
def DarkMode():
    # creates a dark theme for users with bad eyesight or too bright for them
    app.bg = "#808080"
    CustomerLoginSignUpPage.bg = "#808080"
    CustomerLoginPage.bg = "#808080"
    CustomerSignUpPage.bg = "#808080"
    CustomerProductsPage.bg = "#808080"
    CustomerMessagingPage.bg = "#808080"
    EmployeeLoginPage.bg = "#808080"
    EmployeeDashboardPage.bg = "#808080"
    EmployeeProductsPage.bg = "#808080"
    EmployeeCustomersPage.bg = "#808080"
    EmployeeMessagingPage.bg = "#808080"

####################################
#      Create Account Button       #
####################################

def CreateAccountButton():
    global CustomerID
    # validation on signing up
    if CustomerSignUpUsernameTextbox.value == "":
        info("Error!", "You must enter a Username!")
    elif len(CustomerSignUpUsernameTextbox.value) <= 3:
        info("Error!", "Username must be larger than 3 characters!")
    elif len(CustomerSignUpUsernameTextbox.value) >= 15:
        info("Error!", "Username too large must be below 15 characters!")
    elif CustomerSignUpForenameTextbox.value == "":
        info("Error!", "You must enter a Firstname!")
    elif CustomerSignUpSurnameTextbox.value == "":
        info("Error!", "You must enter a Surname!")
    elif CustomerSignUpEmailTextbox.value == "":
        info("Error!", "You must enter a Email!")
    elif "@" and "." not in CustomerSignUpEmailTextbox.value:
        info("Error!", "'Email' must have @ and a '.'!")
    elif CustomerSignUpDeliveryTextbox.value == "":
        info("Error!", "You must enter a Delivery Address!")
    elif CustomerSignUpPasswordTextbox.value == "":
        info("Error!", "You must enter a Password!")
    elif len(CustomerSignUpPasswordTextbox.value) <= 3:
        info("Error!", "Password must be larger than 3 characters!")
    elif len(CustomerSignUpPasswordTextbox.value) >= 12:
        info("Error!", "Password too large must be below 12 characters!")
    elif CustomerTermsAndConditionsCheckbox.value == 0:
        info("Error!", "In order to contine you have to accept the terms and conditions.")
    elif CustomerSignUpPasswordTextbox.value == CustomerSignUpConfirmTextbox.value:
        #insert the data into the database
        # encrypt the password.
        InsertSQL = ("INSERT INTO Customer_Table(Username, Password, Forename, Surname, Email, DeliveryAddress) VALUES('"+ str(CustomerSignUpUsernameTextbox.value) + "','" + str(CustomerSignUpPasswordTextbox.value) + "','" + str(CustomerSignUpForenameTextbox.value) + "','" + str(CustomerSignUpSurnameTextbox.value) + "','" + str(CustomerSignUpEmailTextbox.value) + "','" + str(CustomerSignUpDeliveryTextbox.value)+ "')")
        print(InsertSQL)
        Insert_Data(database_file, InsertSQL)
        CustomerSignUpPage.hide()
        CustomerProductsPage.show()
        query = ("SELECT * FROM Customer_Table WHERE Forename = '" + str(CustomerSignUpForenameTextbox.value) + "' AND Surname = '" + str(CustomerSignUpSurnameTextbox.value) + "'")
        print(query)
        row = query_database(database_file, query)
        CustomerID = row[0][0]
    else:
        # if password != to confirm password then it will output an error.
        info("Sorry!","You need to enter your in password the same time twice!")

###########################
#      Login Button       #
###########################
def CustomerLoginButton():
    global CustomerID
    global CustomerFullName
    # validation for if null
    if CustomerUsernameTextbox.value =="":
        info("Error!", "You must enter a Username!")
    elif CustomerPasswordTextbox.value == "":
        info("Error!", "You must enter a Password!")
    else:
        # query to select all the usernames
        query = ("SELECT * from Customer_Table WHERE Username = "+ "'"+ str(CustomerUsernameTextbox.value) + "' AND Password = '" + str(CustomerPasswordTextbox.value) + "'")
        print(query)
        # gets that row 
        try:
            row = query_database(database_file, query)
        except sqlite3.Error:
            info("Error", "Dont do that again")
        if len(row) > 0:
            CustomerID = row[0][0]
            CustomerFullName = row[0][3] + " " + row[0][4]
            CustomerProductsPage.show()
            CustomerLoginPage.hide()
        else:
            info("Error!", "Your details are not in our database! Try again.")
###############################
#         Display app         #
###############################
app.display()

now = datetime.now()
formatted_now = now.strftime("%Y/%m/%d/%H/%M/%S")
