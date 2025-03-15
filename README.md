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
- Ready for deployment to Replit or any other cloud platform..

## Technologies Used
- **Backend:** Flask (Python)
- **Database:** PostgreSQL
- **Scheduler:** APScheduler
- **API Documentation:** Swagger UI
- **Deployment:** Replit,Render

## Qualities
- **Scalable:** Designed to handle multiple triggers efficiently.
- **Reliable:** Ensures event execution even under high loads.
- **Secure:** Implements authentication and access control for API triggers.
- **User-Friendly:** Provides an intuitive interface for managing triggers and viewing logs.

## Getting Started

### Prerequisites
- Python 3.9 or higher
- PostgreSQL database


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
- **Query Parameters:**
  - aggregate (optional): Set to true to get aggregated event logs.
- **Response(Individual Logs):**
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
- **Response(Aggregrated Logs):**
```json
[
  {
    "trigger_id": 7,
    "count": 1
  },
  {
    "trigger_id": 1,
    "count": 2
  }
]
```

### Swagger UI
You can explore and test the API using Swagger UI:
- **URL:** `http://localhost:5000/api/docs`

## Deployment to Replit with Render Database

### Push Your Code to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Create a New Repl:
1. Go to Replit and log in.
2. Click Create > Import from GitHub.
3. Enter the URL of your GitHub repository.
4. Click Import.

## Set Environment Variables  
1. In your Replit project, click on the Secrets (Environment Variables) tab on the left sidebar.  
2. Add the following environment variables:  

   ```plaintext
   SQLALCHEMY_DATABASE_URI: postgresql://username:password@host:port/database
Replace username, password, host, port, and database with the credentials for your Render-hosted PostgreSQL database.


## Install Dependencies
Replit will automatically detect the requirements.txt file and install the dependencies. If it doesn't, you can manually install them by running:
```bash
pip install -r requirements.txt
```

### Run the Application
1. In the Replit shell, run:
```bash
python run.py
```
2. Replit will automatically start the application and provide a public URL for your app.

### Access the Application:
1. Once the application is running, Replit will display a public URL (e.g., https://event-trigger.yasasvi2004.repl.co).
2. You can access the Swagger UI at: https://231138af-3043-43c5-940f-f034089fe172-00-z46sv88g2m19.pike.replit.dev/api/docs

## Cost Estimation
1. Running this application 24x7 for 30 days with 5 queries a day would cost approximately $0 on Replit's free tier. The Render-hosted PostgreSQL database may have its own pricing, depending on the plan you choose.
2. I have kept my repo public as private repo in replit costs 20$/month

## Acknowledgments
- Flask for the web framework.
- APScheduler for job scheduling.
- Replit,Render for deployment hosting.

## Contact
For questions or feedback, feel free to reach out:
- **Email:** pandu.krishna04@gmail.com
- **GitHub:** [yasasvi2004](https://github.com/yasasvi2004)


