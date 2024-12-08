   TurboTasks Documentation  body { padding: 20px; font-family: Arial, sans-serif; } h1, h2 { color: #2c3e50; } .section-header { background-color: #f1f1f1; padding: 10px; margin-top: 30px; border-radius: 5px; } pre { background-color: #f8f9fa; padding: 10px; border-radius: 5px; } /\* Smooth scrolling \*/ html { scroll-behavior: smooth; }

TurboTasks Task Manager Application Documentation
=================================================

The **TurboTasks** is a simple, yet powerful task management system built using Django. It allows users to add, edit, view, mark tasks as completed, and delete tasks. The app provides a user-friendly interface with interactive features such as dynamically updating task status, date and time creation, and the ability to filter tasks based on their completion status.

This documentation will cover the installation, configuration, features, and usage of the application, along with information on how to contribute to its development.

Table of Contents
-----------------

*   [Features](#features)
*   [Installation](#installation)
*   [Configuration](#configuration)
*   [Running the Application](#running-the-application)
*   [Features Overview](#features-overview)

*   [Task Management](#task-management)
*   [Task Completion](#task-completion)
*   [Task Editing](#task-editing)
*   [Task Deletion](#task-deletion)
*   [Task Status](#task-status)

*   [Testing](#testing)
*   [Contributing](#contributing)
*   [License](#license)

Features
--------

*   **Add Tasks**: Users can add new tasks with a title and description.
*   **View Tasks**: Users can view all tasks along with their creation date and status.
*   **Edit Tasks**: Users can edit the title and description of an existing task.
*   **Mark as Completed**: Users can mark tasks as completed using a circular checkbox. Completed tasks are visually differentiated.
*   **Task Status**: Each task displays its current status, with a dynamically updating status pill that changes color based on completion.
*   **Responsive UI**: The app is built to be mobile-responsive and user-friendly.

Installation
------------

### Prerequisites

To use this app, you need the following:

*   Python 3.x
*   Django 4.x
*   SQLite (default database) or any other relational database (e.g., PostgreSQL, MySQL)
*   Git (optional for version control)

### Step-by-Step Installation

1.  **Clone the Repository** (if using Git):
    
    git clone https://github.com/yourusername/task-manager.git
    cd task-manager
    
2.  **Create a Virtual Environment** (Optional but recommended):
    
    python3 -m venv venv
    source venv/bin/activate  # On Windows use \`venv\\Scripts\\activate\`
    
3.  **Install Dependencies**: Install the necessary Python packages listed in \`requirements.txt\`:
    
    pip install -r requirements.txt
    
4.  **Set Up Database**: Run the following command to apply migrations and set up the database:
    
    python manage.py migrate
    
5.  **Create a Superuser** (for admin access):
    
    python manage.py createsuperuser
    
    Follow the prompts to create an admin user.

Configuration
-------------

*   **Database Configuration**: By default, the app uses SQLite. For production, you can configure other databases such as PostgreSQL or MySQL by modifying the \`DATABASES\` setting in \`settings.py\`.
*   **Static and Media Files**: Static and media files are configured to be served during development. For production, make sure to set up a static file server (e.g., Nginx or a cloud service like AWS S3).

Running the Application
-----------------------

1.  **Start the Development Server**:
    
    python manage.py runserver
    
2.  **Access the Application**: Open your web browser and navigate to:
    
    http://127.0.0.1:8000
    
3.  **Admin Interface**: Access the Django admin interface at:
    
    http://127.0.0.1:8000/admin
    
    Log in with the superuser credentials you created earlier.

Features Overview
-----------------

### Task Management

*   **Adding a Task**: The user can add a task by clicking the "Add Task" button. A form will appear where they can provide the task title and description.
*   **Viewing Tasks**: All tasks are displayed in a list with their title, creation date, and status.

### Task Completion

*   **Mark as Completed**: A circular checkbox appears next to each task. When clicked, it marks the task as completed and the task is visually updated (e.g., a strikethrough on the title and a change in the task's status pill color).
*   **Completed Tasks**: Display a light green pill with the text "Completed" next to the task.
*   **Open Tasks**: Display a light purple pill with the text "Open".

### Task Editing

*   **Edit Task**: Tasks can be edited by clicking the "Edit" button next to a task. This opens the task details in a form, allowing the user to update the task's title and description.

### Task Deletion

*   **Delete Task**: Tasks can be deleted using the "Delete" button. Once deleted, the task is removed from the task list.

### Task Status

*   **Status Pill**: Each task displays a pill indicating its status: open or completed. The pill color changes dynamically when the task is marked as completed.

Testing
-------

This application includes comprehensive unit and integration tests to ensure its functionality. The tests cover models, views, task creation, editing, deletion, and task status updates.

### Running Tests

To run the tests, execute the following command:

python manage.py test tasks

Contributing
------------

We welcome contributions to improve the Task Manager application! If you'd like to contribute, please follow these steps:

1.  **Fork the Repository**: Fork this repository to your GitHub account.
2.  **Create a Branch**: Create a new branch for your feature or fix.
    
    git checkout -b my-feature
    
3.  **Make Changes**: Implement your feature or fix.
4.  **Commit Changes**:
    
    git commit -m "Description of my feature/fix"
    
5.  **Push Changes**:
    
    git push origin my-feature
    
6.  **Create a Pull Request**: Open a pull request on the main repository.

License
-------

This project is Unlicensed - see the [LICENSE](LICENSE) file for details.

Conclusion
----------

This documentation provides all the necessary information to understand, set up, and contribute to the Task Manager Application. The app offers a clean and simple user experience for task management with modern features like status indicators, AJAX updates, and responsive design.

If you encounter any issues or need further assistance, feel free to open an issue in the repository or contribute improvements!
