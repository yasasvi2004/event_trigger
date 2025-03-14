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
- Ready for deployment to Heroku or any other cloud platform..

## Technologies Used
- **Backend:** Flask (Python)
- **Database:** PostgreSQL
- **Scheduler:** APScheduler
- **API Documentation:** Swagger UI
- **Deployment:** Heroku,Render

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

## Deployment to Heroku with Render Database

### Push Your Code to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Create a New App on Heroku:
1. Go to Heroku and log in.
2. Click New > Create new app.
3. Enter a unique name for your app and select a region.
4. Click Create app.

## Connect Your GitHub Repository  
1. On your app’s dashboard, go to the **Deploy** tab.  
2. Under **Deployment method**, select **GitHub**.  
3. Connect your GitHub account and search for your repository (e.g., `yasasvi2004/event_trigger`).  
4. Click **Connect**.  

## Set Environment Variables  
1. Go to the **Settings** tab.  
2. Click **Reveal Config Vars**.  
3. Add the following environment variables:  

   ```plaintext
   SQLALCHEMY_DATABASE_URI: postgresql://username:password@host:port/database

## Deploy Your App
1. On the Deploy tab, scroll down to the Manual deploy section.
2. Select the branch you want to deploy (e.g., main).
3. Click Deploy Branch.
4. Wait for the deployment to complete.

### Access the Application:
1. Once the deployment is complete, click Open App in the top-right corner of your Heroku dashboard.
2. Your app will be live at: https://your-app-name.herokuapp.com

## Cost Estimation
Running this application 24x7 for 30 days with 5 queries a day would cost approximately $0 on Heroku's free tier. The Render-hosted PostgreSQL database may have its own pricing, depending on the plan you choose.

## Acknowledgments
- Flask for the web framework.
- APScheduler for job scheduling.
- Heroku,Render for deployment hosting.

## Contact
For questions or feedback, feel free to reach out:
- **Email:** pandu.krishna04@gmail.com
- **GitHub:** [yasasvi2004](https://github.com/yasasvi2004)


