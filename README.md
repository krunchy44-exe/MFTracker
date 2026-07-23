# 📊 Mutual Fund Tracker

![Python](https://img.shields.io/badge/Python-3.12-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-success)
![License](https://img.shields.io/badge/License-MIT-green)



An automated Python-based Mutual Fund Tracker that fetches the latest NAV from AMFI, calculates portfolio performance, generates a beautiful HTML report, and emails it daily using GitHub Actions.

---

## 🚀 Features

- 📈 Fetches latest NAV from AMFI
- 💼 Tracks your mutual fund portfolio
- 💰 Calculates:
  - Current Portfolio Value
  - Total Investment
  - Profit/Loss
  - Returns (%)
- 📧 Sends an HTML email report automatically
- ⏰ Runs daily using GitHub Actions
- 🔐 Keeps email credentials secure using GitHub Secrets

---

## 📸 Sample Report

The email contains:

- Fund Name
- Scheme Code
- Latest NAV
- NAV Date
- Units Held
- Total Invested Amount
- Current Portfolio Value
- Profit/Loss
- Overall Returns

---

## 🛠 Tech Stack

- Python 3
- Requests
- python-dotenv
- SMTP (Gmail)
- GitHub Actions
- JSON

---

## 📂 Project Structure

```
MFTracker/
│
├── tracker.py
├── nav_fetcher.py
├── report_generator.py
├── email_sender.py
├── portfolio.json
├── requirements.txt
├── .env (Local Only)
│
└── .github/
    └── workflows/
        └── daily_report.yml
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/krunchy44-exe/MFTracker.git
cd MFTracker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
```

Update `portfolio.json`

```json
{
  "scheme_code": "YOUR_SCHEME_CODE",
  "fund_name": "YOUR_FUND_NAME",
  "units": 100,
  "invested": 10000
}
```

Run the project

```bash
python tracker.py
```

---

## 🔄 Automation

The project automatically runs every day using **GitHub Actions**.

Workflow tasks:

- Download latest NAV data
- Calculate portfolio performance
- Generate HTML report
- Send report via email

---

## 📌 Future Improvements

- Support multiple mutual funds
- Portfolio growth charts
- Daily NAV history
- Telegram notifications
- WhatsApp notifications
- Web dashboard using Flask or Streamlit
- SIP detection from confirmation emails

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kannishk Chauhan**

AI & Machine Learning Student

Interested in:
- Artificial Intelligence
- Machine Learning
- Backend Development
- Python Programming
- Cyber Security

GitHub: https://github.com/krunchy44-exe
