 row = 5
 for i in range(0, len(row)):
            CustomerFirstName = row[i][3]
            CustomerSecondName = row[i][4]
            CustomerID = row[i][0]
            CustomerFullName = CustomerFirstName + " " + CustomerSecondName
            CustomerListbox.append(CustomerFullName)
