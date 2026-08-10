# MySQL Automation

Automated MySQL Server installation on Ubuntu using **Bash Script** and **Python**.

## 📌 Project Overview

Manually installing MySQL requires several commands such as:

* Updating packages
* Installing MySQL Server
* Starting MySQL service
* Enabling MySQL at system startup
* Checking MySQL version
* Verifying MySQL service status

This project automates these tasks using scripts.

## 🛠️ Technologies Used

* Linux / Ubuntu
* Bash Shell Scripting
* Python 3
* MySQL Server
* Git
* GitHub
* Python-.env
* 
## 📁 Project Structure

```text
mysql-automation/
│
├── install_mysql.sh       # Bash installation script
├── install_mysql.py       # Python installation script
├── .env                   # Local configuration file
├── .gitignore             # Files ignored by Git
└── README.md              # Project documentation
```

## 🚀 Bash Script Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/Divya12004/mysql-automation.git
cd mysql-automation
```

### Step 2: Give Execute Permission

```bash
chmod +x install_mysql.sh
```

### Step 3: Run Script

```bash
sudo ./install_mysql.sh
```

The script will:

```text
Update packages
      ↓
Install MySQL
      ↓
Start MySQL
      ↓
Enable MySQL
      ↓
Check MySQL version
      ↓
Verify service
```

## 🐍 Python Script Installation

### Step 1: Install Python

Check Python:

```bash
python3 --version
```

If Python is not installed:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### Step 3: Install Python Dependency

```bash
pip install python-dotenv
```

### Step 4: Create `.env`

Create:

```bash
nano .env
```

Add:

```env
MYSQL_PACKAGE=mysql-server
MYSQL_SERVICE=mysql
```

### Step 5: Run Python Script

```bash
sudo python3 install_mysql.py
```

## ⚙️ Environment Variables

The `.env` file contains configuration values used by the Python script.

```env
MYSQL_PACKAGE=mysql-server
MYSQL_SERVICE=mysql
```

The `.env` file should **not be pushed to GitHub** if it contains secrets or environment-specific configuration.

The `.gitignore` file contains:

```text
.env
venv/
__pycache__/
*.pyc
```

## 🔍 Verify MySQL

Check MySQL version:

```bash
mysql --version
```

Check MySQL service:

```bash
sudo systemctl status mysql
```

Check whether MySQL is running:

```bash
systemctl is-active mysql
```

Expected:

```text
active
```

Login to MySQL:

```bash
sudo mysql
```

Exit:

```sql
exit;


