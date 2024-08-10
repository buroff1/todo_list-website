# Import necessary modules and classes from Flask and SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for  # Import Flask framework and required utilities
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database operations
from sqlalchemy.orm import DeclarativeBase  # Import DeclarativeBase to create a custom base class

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Set the database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for better performance


# CREATE DB

# Define a base class for model definitions using SQLAlchemy's DeclarativeBase
class Base(DeclarativeBase):
    pass


# Initialize SQLAlchemy with the custom base class
db = SQLAlchemy(model_class=Base)  # Create a new SQLAlchemy object with Base as the model class
db.init_app(app)  # Initialize the app with the SQLAlchemy object


# Define a model class for To-do items
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define an integer column for the primary key
    title = db.Column(db.String(100))  # Define a string column for the title of the to-do item
    complete = db.Column(db.Boolean)  # Define a boolean column for completion status


# Create the database tables
with app.app_context():  # Ensure we have an application context for database operations
    db.create_all()  # Create all tables in the database defined by the models


# Define the route for the home page
@app.route('/', methods=["POST", "GET"])  # Define a route for both POST and GET requests
def home():
    todo_list = Todo.query.all()  # Query all to-do items from the database
    if request.method == "POST":  # Check if the request method is POST
        title = request.form.get("title")  # Get the 'title' field from the form data
        if title:  # Check if the title is not empty
            new_todo = Todo(title=title,
                            complete=False)  # Create a new To-do object with the title and default complete status
            db.session.add(new_todo)  # Add the new to-do item to the session
            db.session.commit()  # Commit the session to save the item to the database
            return redirect(url_for('home'))  # Redirect to the home page after adding the item
    return render_template('index.html', todo_list=todo_list)  # Render the index.html template with the to-do list


# Define the route to update a to-do item's completion status
@app.route('/update/<int:todo_id>')  # Define a route with a variable part for the to-do item's ID
def update(todo_id):
    task = Todo.query.get(todo_id)  # Query the to-do item by ID
    task.complete = not task.complete  # Toggle the completion status
    db.session.commit()  # Commit the change to the database
    return redirect(url_for('home'))  # Redirect to the home page


# Define the route to delete a to-do item
@app.route('/delete/<int:todo_id>')  # Define a route with a variable part for the to-do item's ID
def delete(todo_id):
    task = Todo.query.get(todo_id)  # Query the to-do item by ID
    db.session.delete(task)  # Delete the to-do item from the session
    db.session.commit()  # Commit the deletion to the database
    return redirect(url_for('home'))  # Redirect to the home page


# Run the Flask application
if __name__ == "__main__":  # Check if the script is run directly (not imported)
    app.run(debug=True, port=5001)  # Run the app in debug mode on port 5001
