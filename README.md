## Face Recognition based Attendance Management System (FRAMS)
Face Recognition based Attendance Management System with a Flask web application and Power BI attendance dashboard.

### Table of Contents
- [Features](#features)
- [Installation and Usage](#installation-and-usage)
- [Technologies Used](#technologies-used)
- [Methodology](#methodology)
- [User Interface Demo](#user-interface-demo)

### Features
- Face detection and recognition
- Attendance management
- Generates attendance reports in a csv file
- Secure admin login
- Interactive user interface
- Can detect multiple faces and mark attendance at a time 
- Works in bright and low light conditions
- Attendance dashboards using Power BI


### Installation and Usage
1. Clone the repository:
    ```
    git clone https://github.com/Manohar59/Face-Recognition-Attendance-Management-System/tree/main
    ```
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Replace the training images with your own set of images in the folder `Training images`.
4. Open the `app.py` file and change the file paths as per your system.
5. Run the `app.py` file.

### Technologies Used
- **Programming Languages:** Python
- **Libraries:** OpenCV, dlib, face-recognition
- **Database:** SQLite
- **Web Application:** Flask, HTML, CSS, JavaScript
- **Data Visualization:** Power BI

### Methodology
- **Environment Setup:** Created a conda environment and installed necessary dependencies including OpenCV, dlib, face-recognition, and Flask.
- **Face Detection:** Converted images to black and white, then used HOG to detect faces by comparing image gradients.
- **Face Embedding:** Used 128-dimensional vectors and the triplet loss function for distinguishing between faces.
- **Face Recognition:** Utilized Euclidean distance with a threshold of 0.5 to compare the generated face encodings with the actual encodings of the training images to recognize the faces.
- **Database Connection:** Stored attendance data in a SQLite database and exported it to CSV for Power BI integration.
- **Web Application:** Developed a Flask-based web app for real-time attendance capturing and management.
- **Power BI Dashboard:** Connected the attendance data to Power BI to create dashboards. Embedded Power BI reports into the web app for real-time insights.


### User Interface Demo
- Fig.1: Home page
  <img width="1906" height="863" alt="Interface 1" src="https://github.com/user-attachments/assets/cc0515be-b1bc-4f27-9b9a-d4293138667d" />


- Fig.2: Register Page
  <img width="1917" height="918" alt="Interface 2" src="https://github.com/user-attachments/assets/6b1b30cd-c0d6-4d10-b6d1-b619826a885d" />

 
- Fig.3: User Register
<img width="1911" height="948" alt="Interface 3" src="https://github.com/user-attachments/assets/d093d4e6-c3e1-4872-a89b-bb3707a19dd9" />

 
- Fig.4: Face Registor Page
<img width="1901" height="885" alt="Interface 4" src="https://github.com/user-attachments/assets/114f625c-13a6-4520-affc-a6b07205f5f4" />

  
- Fig.5: Database
<img width="1429" height="363" alt="dataBase" src="https://github.com/user-attachments/assets/21eb75cc-fab7-4cef-9390-c85601107cc8" />

  

### License

MIT License

Copyright (c) 2026 Kathi Manohar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
