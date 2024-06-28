# Odoo eLearning Dependencies

This Odoo module adds a new feature to the existing eLearning module, allowing you to set prerequisites for courses. With this module, you can ensure that learners complete the required courses before enrolling in a specific course.

## Features

- Define prerequisite courses for each course
- Prevent learners from enrolling in a course if they haven't completed the prerequisites
- Display prerequisite courses in the course form view
- Show prerequisite courses in the course kanban view

## Installation

1. Clone the repository or download the source code.
2. Copy the `dh_elearning_dependencies` folder into the `addons` directory of your Odoo installation.
3. Update the addon path in the Odoo configuration file (e.g., `odoo.conf`) to include the directory containing the `dh_elearning_dependencies` module.
4. Start or restart the Odoo server.
5. Log in to the Odoo web interface and go to **Apps** > **Update Apps List**.
6. Search for "Odoo eLearning Dependencies" and install the module.

## Usage

1. Go to **Website** > **Courses** and open a course.
2. In the course form view, you'll see a new field called "Prerequisites" under the "Options" section.
3. Select the courses that should be completed before enrolling in the current course.
4. When a learner tries to enroll in a course, the system will check if they have completed the prerequisite courses. If not, an error message will be displayed, and the enrollment will be prevented.
5. In the course kanban view, you'll see the prerequisite courses listed under each course.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Credits

This module was developed by _dinoherlambang_.
