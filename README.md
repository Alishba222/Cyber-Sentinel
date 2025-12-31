🛡️ Cyber Sentinel: Real-time Cyberbullying Identifier
Cyber Sentinel is a full-stack machine learning application designed to monitor and identify cyberbullying in online interactions. By combining a Django web dashboard with a Support Vector Machine (SVM) classifier, the system provides automated text moderation, live metrics tracking, and a robust background processing service.

🚀 Key Features
Automated Classification: Uses a trained SVM model to classify text as "Bullying" or "Safe" with an optimal decision threshold of 0.5.

Live Dashboard: A real-time monitoring interface displaying precision, recall, F1-score, and categorical attack analysis (Toxicity, Insult, etc.).

Hybrid Data Sourcing: Capability to fetch live data from external APIs or upload custom CSV datasets (supports large-scale data up to 32,000+ records).

Windows Background Service: A dedicated background worker (CyberSentinelService) that manages long-running data ingestion and model retraining tasks without interrupting the UI.

Secure Authentication: Integrated user signup and login system to protect sensitive administrative controls.

🛠️ Tech Stack
Backend: Python, Django

Machine Learning: Scikit-learn (SVM Classifier, TF-IDF Vectorization), Joblib

Data Handling: Pandas, NumPy

Frontend: HTML5, CSS3, JavaScript (AJAX for live metric updates)

Database: SQLite (default) / Support for PostgreSQL

System Integration: PyWin32 (Windows Service Integration)

📊 Model Performance
The current model is optimized for high Recall, ensuring that subtle forms of harassment are not missed.

Accuracy: ~88% - 92% (on balanced datasets)

Threshold: 0.5 (Configured for balanced sensitivity)

Feature Extraction: TF-IDF (Term Frequency-Inverse Document Frequency) to capture weighted importance of offensive terminology.

⚙️ Installation & Setup
1. Clone the Repository
Bash

git clone https://github.com/yourusername/cyber-sentinel.git
cd cyber-sentinel/config
2. Install Dependencies
Bash

python -m pip install -r requirements.txt
3. Database Migration
Bash

python manage.py makemigrations
python manage.py migrate
4. Running the Windows Service (Optional)
To enable background automation, run your terminal as Administrator:

PowerShell

python windows_service.py install
python windows_service.py start
5. Start the Web Server
Bash

python manage.py runserver
📂 Project Structure
/config: Main Django project configuration.

/webapp: Core application logic, views, and templates.

/service: Background tasks and machine learning pipeline logic.

master_dataset.csv: Central data storage for training and analysis.

windows_service.py: Script for Windows Service management.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
