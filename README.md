# Smart Study Focus Tracker

## 📌 Project Overview

Smart Study Focus Tracker is a real-time computer vision application that monitors a student's concentration during study sessions using webcam input.  
It detects face and eye presence to determine whether the user is focused or distracted and generates a simple study session report.

This project demonstrates practical usage of classical Computer Vision techniques without requiring GPU or heavy deep learning models.

---

## 🎯 Features

- Real-time webcam monitoring  
- Face and eye detection using Haarcascade classifiers  
- Identifies focused vs distracted state  
- Displays live status on video feed  
- Generates study session report:
  - Total session time  
  - Focus time  
  - Distraction time  
  - Focus percentage  

---

## 🧠 Technologies Used

- Python  
- OpenCV  
- Haarcascade Classifiers  
- Real-time Video Processing  

---

## 💻 System Requirements

- Python 3.x  
- Webcam  
- No GPU required  

---

## ⚙️ Installation Steps

1. Clone the repository:
git clone https://github.com/hemaamurthy/Smart_Focus_Tracker.git

2. Install required library:
pip install opencv-python

3. Ensure the following files are in the project folder:

- focus_tracker.py  
- haarcascade_frontalface_default.xml  
- haarcascade_eye.xml  

---

## ▶️ How to Run

python focus_tracker.py

- Webcam window opens  
- Look at screen → Status shows "Focused"  
- Look away → Status shows "Distracted"  
- Press **Q** to end session  

After closing, the terminal displays the study report.

---

## 📊 Sample Output

Study Session Report
Total Time (seconds): 120
Focus Time (frames): 90
Distraction Time (frames): 30
Focus Percentage: 75.0 %

---

## 🚀 Future Enhancements

- Add timer-based accurate tracking  
- Store daily focus reports  
- Build dashboard for analytics  
- Sound alert for long distraction  

---

## 👩‍💻 Author

**Hemalatha P. (Hema)**  
AI & ML Student | Computer Vision Enthusiast  
GitHub: https://github.com/hemaamurthy  
LinkedIn: https://www.linkedin.com/in/hemapitla  
