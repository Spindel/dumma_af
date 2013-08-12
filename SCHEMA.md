User 
ID (UUID) (pri key) |  email-address (VARCHAR) (unique) |  Name (varchar something) | Free Will (BOOL)  | CV (Text)


Empty CV is not allowed.  
// CV
// User.ID (UUID, pri key, unique) |  CV (Textfield)




Corporation
ID (UUID) | Name (VARCHAR) | Description (VARCHAR)


Subscriber
User.ID (UUID)  | Corporation.ID (UUID)
Unique constraint( User.ID,Corporation.ID)

FormMail
ID (pri key) | Corporation.ID | Text (templated, text)

Log
ID (pri key) | Date (date) | Name(Copy of User.Name, Varchar) | Email (Copy of User.Email, Varchar) | Status | FormMail.ID

