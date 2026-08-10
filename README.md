
# MySQL Automation

Automated MySQL installation on Ubuntu using **Bash and Python**.

## 🛠️ Technologies

* Ubuntu / Linux
* MySQL
* Bash
* Python
* Git & GitHub
* `.env`

## 📁 Project Structure

```text
mysql-automation/
├── install_mysql.sh
├── install_mysql.py
├── .env
├── .gitignore
└── README.md
```

## 🚀 Bash Script

```bash
chmod +x install_mysql.sh
sudo ./install_mysql.sh
```

## 🐍 Python Script

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependency:

```bash
pip install python-dotenv
```

Run:

```bash
sudo venv/bin/python install_mysql.py
```

## 🔍 Verify MySQL

```bash
mysql --version
sudo systemctl status mysql
```


