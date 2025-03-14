# Event Trigger Platform

## Features

### Scheduled Triggers
- Create triggers that fire at a specific time or at regular intervals.
- Supports one-time and recurring triggers.

### API Triggers
- Create triggers that fire when a specific API endpoint is called with a predefined payload.

### Event Logging
- Logs all triggered events with details such as trigger type, time, and payload.
- Events are retained for 48 hours (2 hours active, 46 hours archived).

### Simple UI
- Swagger UI for easy API testing and exploration.

### Deployment
- Ready for deployment to Render or any other cloud platform.

## Technologies Used
- **Backend:** Flask (Python)
- **Database:** PostgreSQL
- **Scheduler:** APScheduler
- **API Documentation:** Swagger UI
- **Deployment:** Render

## Qualities
- **Scalable:** Designed to handle multiple triggers efficiently.
- **Reliable:** Ensures event execution even under high loads.
- **Secure:** Implements authentication and access control for API triggers.
- **User-Friendly:** Provides an intuitive interface for managing triggers and viewing logs.

## Getting Started

### Prerequisites
- Python 3.9 or higher
- PostgreSQL database
- Docker (optional, for local development)

### Installation

#### Clone the Repository:
```bash
git clone https://github.com/yasasvi2004/event_trigger.git
cd event_trigger
```

#### Set Up a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables:
Create a `.env` file in the root directory and add the following:
```plaintext
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/event_trigger_db
```

#### Run Database Migrations:
```bash
flask db init
flask db migrate
flask db upgrade
```

#### Run the Application:
```bash
python run.py
```

## API Endpoints

### Create a Trigger
- **URL:** `/triggers`
- **Method:** `POST`
- **Request Body:**
```json
{
  "type": "scheduled",
  "details": {
    "time": "2025-03-13T10:00:00Z", 
     "interval": 30,                   
    "recurring": true         
  }
}
```
- **Response:**
```json
{
  "id": 1
}
```

### Trigger an Event
- **URL:** `/triggers/{trigger_id}/trigger`
- **Method:** `POST`
- **Request Body:**
```json
{
  "key": "value"
}
```
- **Response:**
```json
{
  "message": "Event triggered"
}
```

### Get Events
- **URL:** `/events`
- **Method:** `GET`
- **Response:**
```json
[
  {
    "id": 1,
    "trigger_id": 1,
    "triggered_at": "2025-03-13T10:00:00Z",
    "payload": {
      "key": "value"
    },
    "is_test": false
  }
]
```

### Swagger UI
You can explore and test the API using Swagger UI:
- **URL:** `http://localhost:5000/api/docs`

## Deployment to Render

### Push Your Code to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Create a New Web Service on Render:
1. Go to Render and create a new Web Service.
2. Connect your GitHub repository.
3. Configure the Web Service:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:create_app()`
4. Add the following environment variables:
   - `FLASK_ENV`: `production`
   - `SQLALCHEMY_DATABASE_URI`: `postgresql://username:password@host:port/database`
5. Click **Create Web Service** to deploy your application.



### Access the Application:
Open your browser and go to `http://localhost:5000`.

## Cost Estimation
Running this application 24x7 for 30 days with 5 queries a day would cost approximately **$0** on Render's free tier.


## Acknowledgments
- Flask for the web framework.
- APScheduler for job scheduling.
- Render for deployment hosting.

## Contact
For questions or feedback, feel free to reach out:
- **Email:** pandu.krishna04@gmail.com
- **GitHub:** [yasasvi2004](https://github.com/yasasvi2004)


