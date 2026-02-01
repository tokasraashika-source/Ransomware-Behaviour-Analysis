# Ransomware Behaviour Analysis with Data Visualization

## Project Overview

This project focuses on understanding ransomware behaviour through a controlled and ethical simulation. The objective is not to create real malware, but to study how ransomware typically encrypts files and how such activity can be logged and analysed from a cybersecurity and data analytics perspective. All experiments were performed in an isolated virtual environment.

The project simulates file encryption, records the activity in structured log files, and analyses the resulting data using Orange ML and Tableau.

## Objectives

The main objectives of this project are to simulate ransomware-like file encryption in a safe environment, generate structured logs of encryption activity, analyse behavioural patterns using data visualisation tools, and build an academic project that combines cybersecurity concepts with data science techniques.

## Tools and Technologies Used

Python was used to simulate ransomware behaviour and handle file encryption. The project was executed on Ubuntu running inside VirtualBox to ensure isolation and safety. Encryption activity was logged in CSV format. Orange ML was used for exploratory data analysis, and Tableau was used to build interactive dashboards. Git and GitHub were used for version control and project hosting.

## Project Structure

The project consists of a Python script that performs the ransomware simulation, a CSV file that stores the encryption activity logs, and a screenshots directory containing visual outputs from Orange ML and Tableau.

## Working of the Simulation

The Python script scans a target directory and encrypts sample files using a symmetric encryption method. Each encryption action is logged with relevant details such as file name, timestamp, and encryption status. These logs are saved in a CSV file, which is later used for data analysis and visualisation.

## Data Analysis and Visualisation

The generated ransomware log file is loaded into Orange ML to perform exploratory data analysis and observe basic behavioural patterns. The same dataset is visualised in Tableau to analyse trends such as the number of encrypted files and time-based activity patterns. Screenshots of these analyses are included in the screenshots directory.

## Ethical Disclaimer

This project is strictly for academic and educational purposes. No real user data was harmed during development. All simulations were executed in a virtual environment to prevent any unintended impact on real systems. The project is intended to support defensive cybersecurity learning and behavioural analysis.

## Author

Raashika Tokas
B.Tech Computer Science and Engineering (Data Science)

## Key Learnings

Through this project, key learnings include understanding ransomware behaviour, logging and analysing security events, applying data visualisation techniques to cybersecurity data, and structuring and presenting a technical project on GitHub.

## Future Scope

The project can be extended by incorporating anomaly detection techniques, applying machine learning models for behaviour classification, and expanding the simulation to cover multiple directories or more complex attack patterns.
