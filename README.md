# Django CRM

This is a Django project that uses Chart.js to display various types of charts based on the data from the `Product` model.

## Features

- Display all products in a table format on the index page.
- Add new products through a form on the index page.
- View a line chart representation of the product data.
- View a pie chart representation of the product data.
- View a doughnut chart representation of the product data.
- View a polar area chart representation of the product data.

## Installation

### Prerequisites

- Python 3.x
- Django
- Virtualenv (recommended)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/AflaxCade/Django-with-chart.js.git
```

2. Navigate to the project directory:

```bash
cd Django-with-chart.js
```


3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:

- For Windows:

```bash
env\Scripts\activate
```

- For macOS and Linux:

```bash
source env/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Apply Migrations:

```bash
python manage.py migrate
```

7. Create Superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

8. Run the Development Server:

```bash
python manage.py runserver
```

The server will start on `http://localhost:8000` or `http://127.0.0.1:8000`.

## Application Snapshots

![Django Chartjs Snapshot](https://github.com/AflaxCade/Django-with-chart.js/blob/main/Screenshot%201.png)

![Django Chartjs Snapshot](https://github.com/AflaxCade/Django-with-chart.js/blob/main/Screenshot%202.png)

![Django Chartjs Snapshot](https://github.com/AflaxCade/Django-with-chart.js/blob/main/Screenshot%203.png)

![Django Chartjs Snapshot](https://github.com/AflaxCade/Django-with-chart.js/blob/main/Screenshot%204.png)

![Django Chartjs Snapshot](https://github.com/AflaxCade/Django-with-chart.js/blob/main/Screenshot%205.png)


Above is a snapshot of the Django with chartjs interface showcasing its features and layout.
