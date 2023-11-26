# LogicMonitor API - Get Devices Script

## Overview
This Python script is designed to interact with the LogicMonitor API to retrieve information about devices and their associated data sources. It can be used to fetch a list of all devices in your LogicMonitor account and display them in a tabular format. Additionally, you can choose to insert a specific device ID and retrieve detailed information about the data sources associated with that device, including their instances. The LogicMonitor REST API will allow you to programmatically query and manage your LogicMonitor resources: dashboards, devices, reports, services, alerts, collectors, datasources, SDTs and more. Refer to their official Product Documentation for REST API at https://www.logicmonitor.com/support/rest-api-developers-guide/overview/using-logicmonitors-rest-api

## Prerequisites
Before using this script, make sure you have the following prerequisites in place:

1. LogicMonitor Account: You must have a LogicMonitor account with appropriate permissions to access the API.
2. Access Key and ID: You will need an Access Key and Access ID for authentication. These should be stored in a .env file in the same directory as the script. Guide to generate API tokens can be seen at https://www.logicmonitor.com/support/settings/users-and-roles/api-tokens/
3. Python Dependencies: Install the required Python packages using pip:
    ```
    pip install requests json hashlib base64 time hmac os dotenv tabulate
    ```

## How to Use the Script
1. Set Up Environment Variables
    Ensure that you have created a .env file in the script's directory with the following environment variables:
    - ACCESS_KEY: Your LogicMonitor Access Key.
    - ACCESS_ID: Your LogicMonitor Access ID.
    - COMPANY: Your LogicMonitor account company name.

2. Run the Script
    Run the script by executing the Python file using the command line:
    ```
    python getDevices.py
    ```

3. Retrieve Device Information
    The script will fetch a list of all devices in your LogicMonitor account and display them in a table format. The table will include device ID, name, display name, manufacturer, sysinfo, and description.

4. Insert a Device ID (Optional)
    You can choose to insert a specific device ID when prompted. The script will then retrieve detailed information about the data sources associated with that device, including their instances.

5. Retrieve Data Source Instances (Optional)
    If you decide to proceed with retrieving data source instances, the script will prompt you to enter a data source ID. It will then fetch and display information about the instances associated with that data source.

## Output
- The script will display retrieved information in a formatted table in the console.
- JSON responses will be saved in the output/ directory, including device information and data source instances.

## Caution
Be cautious with your LogicMonitor Access Key and Access ID, as they provide access to your LogicMonitor account. Keep them secure and do not share them publicly.

## Disclaimer
This script is provided as-is and may require modifications to fit your specific LogicMonitor environment and needs. Use it responsibly and in compliance with LogicMonitor's terms of service and API usage guidelines.

## What is LogicMonitor?
LogicMonitor is a comprehensive cloud-based IT infrastructure monitoring and observability platform designed to help organizations monitor and manage their entire technology stack. It provides real-time visibility into the performance, health, and availability of a wide range of IT resources, including servers, networks, applications, cloud services, and more. Visit their official website at https://www.logicmonitor.com/

## Motivation
The motivation behind creating this script was to streamline the process of accessing and retrieving device information from a LogicMonitor account. LogicMonitor provides a powerful monitoring platform, but sometimes you need a more customized way to access and analyze device data. This script aims to simplify the retrieval of device details and associated data sources.

## Why I Built This Script
- **Automation**: I wanted to automate the process of fetching device information, making it easier and more efficient for LogicMonitor users to access crucial data.
- **Customization**: LogicMonitor offers a wealth of information, but I wanted to provide a way for users to extract specific data or focus on individual devices when needed.
- **Learning Opportunity**: Developing this script allowed me to deepen my understanding of APIs, authentication, and data manipulation in Python. It also provided hands-on experience with LogicMonitor's API.

## What I Learned
While working on this project, I gained valuable insights and skills, including:

- **API Integration**: I learned how to interact with RESTful APIs, including authentication using access keys and IDs, making HTTP requests, and handling responses.
- **Data Manipulation**: I honed my skills in processing JSON data, extracting relevant information, and presenting it in a readable format.
- **Environment Variables**: I explored the use of environment variables for storing sensitive information securely.
- **Python Libraries**: I utilized various Python libraries, such as `requests` for HTTP requests, `dotenv` for managing environment variables, and `tabulate` for table formatting.
- **Error Handling**: I improved my error handling and debugging skills to ensure the script runs smoothly even in less-than-ideal conditions.

By sharing this script and its documentation, I hope to contribute to the LogicMonitor community and help fellow users leverage the power of LogicMonitor's API for their specific needs.

## Contributing
If you would like to contribute to this project, please open an issue or submit a pull request.

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Author
Mohd NeoTech
Email: mohdneotech@gmail.com