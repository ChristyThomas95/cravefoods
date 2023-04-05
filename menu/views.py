from django.shortcuts import render
from django.db import connection

# Create your views here.
cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table_name WHERE your_column_name LIKE '%[^ -~]%'")
result = cursor.fetchall()