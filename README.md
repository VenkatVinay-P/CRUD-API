# CRUD-API
# **About Project** 
This is a backend application for managaing requested tasks.This task is developed to perform **CRUD operations** given by user.For managing requests the application used is **POSTMAN**.
# **Technologies Used**
 -Python  
 -Flask  
 -SQLAlchemy  
 -SQLite  
# **Set up**
## 1.**Cloning repository**  
          git clone https://github.com/VenkatVinay-P/CRUD-API.git
## 2.**pip requirements**  
          pip install flask flask_sqlalchemy
## 3.**run the application in cmd**  
          python app.py(change the directory where your file is located)
# **Database**
The database model consists of a single table Persons with the following columns:  
   - **id**(Integer,Primary key):unique identifier for the persons
   - **name**(type,string)
   - **mobile**(type,integer)
   - **email**(type,varchar)
   - **country**(type,string)
# **API ENDPOINTS**
## GET ALL PERSONS
- **url**: '/persons'
- **method**: 'GET'
## GET PERSON BY ID
- **url**: '/persons/<person_id>(here we should mention the unique identifer(id) for particular person).
- **method**: 'GET'
## CREATE A NEW PERSON DETAILS
1. For creating a new detail we have to go to body and choose raw file in mentioned options.And then choose JSON file.Then enter the details.
- **url**: '/persons'
- **method**: 'POST'
## UPDATE DETAILS OF THE PERSON
- **url**: '/personss/<persons_id>'
- **method**: 'PUT'
## DELETE DETAILS OF THE PERSON
- **url**: '/persons/<persons_id>'
- **method**: 'DELETE'
# **TESTING API's**
- The Testing is done by using **POSTMAN** Application.Create new collection in postman and give collection name and then request a url.Before requesting the URL check whether you followed the step-3 in set up.The requesting url is https://localhost:5000/tasks
# **CONTACT**
- **E-Mail**: 'venkatkissan143@gmail.com'
- **Mobile**: '+918143736617'
