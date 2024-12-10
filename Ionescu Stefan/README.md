#tema_Python

 surname Ionescu x=7
 
 name  Stefan Alexandru  y=15
 
 1-------------------------
 
 Code:
 
     line 26--Manager class inheriting from Employee
     line 28--Made a counter for the managers
     line 30--Manager class has a new constructor inherited from base class employees: with arguments (self,name,department)
     line 35--Creating Employee objects  5x 
     line 35--Creating Manager objects   5x
     line 49--Printing the salary using the employee function display_emp_count which prints the salary as was requested 
     line 54-- Prints the number of objects from each class   
           employee nr=10
            
           manager nr=5
           
Run: To run this code you run this command in the terminal/cmd python3 employee.py
    
   2------------------------
Code: 

    This Python file polts the data from the CSV file  The first figure plots all the data
    
      then the second figure plots the first 5 lines with all the columns the third figure plots the first 15 lines
      
       with 2 columns (Puls and Durata)line 1--the import for the modules
    
    line 6--using the pandas function read_csv  i rad from the data.csv file into the variable df
    line 7--using the function .head I extracted the first 7 lines into the variable df_x   
    line 8--using the function .head i extracted the first 15 lines into the variable df_x 
     and also i selected the necessary columns
    line 9--plots all the data    
    line 10--plots the first 7 lines of the data
    line 11--plots the first 15 lines of the data from the selected necessary columns
    line 12--shows the plot on the screen
   
Necessary files: 

     This file needs 2 modules to run (pandas and matplotlib) 
     To make it easy you could make a virtual environment (venv) on your machine in the folder you should have python
      file and the data.cvs and the folder containing the modules. You can make this venv 
       by running these comands: in the terminal
         navigate to the folder where u have the files  and run this command :
         
For Windows: 



This will make a virtual environment folder
 
         
    python -m venv your_name_for_the_venv  
         
to activate the virtual environment  you have to run this command :
         
                  your_name_for_the_venv\Scripts\activate.bat
                  
                  
then to install pandas run this command :
        
            pip install pandas 
            
then to install matplotlib run this command :
        
           pip install matplotlib    
         
         
         
for mac/linux:



        python3 -m venv your_name_for_the_venv   
         
                 
to activate the virtual environment  you have to run this command :
         
                  source your_name_for_the_venv/bin/activate  
                  
                  
then to install pandas run this command :
        
            pip install pandas 
            
then to install matplotlib run this command :
        
           pip install matplotlib 
           
           
Run:
    To run this code you have to  run this command in the terminal/cmd

                  python ex2.py          
                   
The graph will appear on the screen    
                  
     

References:

    •    https://www.w3schools.com/python/pandas/default.asp
    •    https://www.w3schools.com/python/matplotlib_intro.asp 
    •    calp.python.extras de la Files > Class.Materials 
    •    https://code.visualstudio.com/docs/python/tutorial-flask
    •    https://github.com/microsoft/python-sample-vscode-flask-tutorial 
    •    https://github.com/crchende/ppyan2 
    •    https://code.visualstudio.com/docs/python/tutorial-django 
    •    https://www.w3schools.com/django/index.php 
    •    https://code.visualstudio.com/docs/python/testing
    •    https://www.tutorialspoint.com/pytest/index.htm
    •    https://matplotlib.org/stable/
    •    https://pandas.pydata.org/docs/getting_started/install.html 
