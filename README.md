
# Corporate Portal

Welcome to the **Corporate Intranet Portal**! This platform is designed to centralize and streamline internal communications, document management, and team collaboration across the organization.

---

## 🚀 Features
- **Employee Directory:** Quickly search and connect with colleagues across departments.
- **HR Repository:** Store and access important company documents in a secure and organized way.
- **Announcements and Updates:** Stay informed with company-wide news, events, and notices.
- **Task and Project Management:** Collaborate efficiently with built-in task tracking and project dashboards.

---

## 🛠️ Tech Stack
- **Frontend:** Html, CSS, js
- **Backend:** Django 
- **Database:** PostgreSQL/MySQL
- **Authentication:** OAuth2/LDAP for secure login and user management (In development)
- **Hosting:** Dockerized microservices


## 🏗️ Setup Instructions

1. **Clone the Repository:**
   ```bash
    git clone https://github.com/bazuly/intra-corp-app
    docker build -f site_grando/Dockerfile.base -t intra-corp-app-base .
    docker-compose up --build -d
    docler-compose web exec manage.py migrate
