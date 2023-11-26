# title: LogicMonitor API - Get Devices
# description: This script will get all devices in your LogicMonitor account and display them in a table format.

import requests
import json
import hashlib
import base64
import time
import hmac
import os
from dotenv import load_dotenv
from tabulate import tabulate  # Import tabulate for table formatting

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
access_key = os.getenv("ACCESS_KEY")
access_id = os.getenv("ACCESS_ID")
company = os.getenv("COMPANY")

# Request Info
httpVerb = 'GET'
resourcePath = '/device/devices'  # This is the URL for the list of devices
data = ''
queryParams = ''

# Construct URL
url = 'https://' + company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams

# Get current time in milliseconds
epoch = str(int(time.time() * 1000))

# Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

# Construct signature
hmac1 = hmac.new(access_key.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac1.encode())

# Construct headers
auth = 'LMv1 ' + access_id + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type': 'application/json', 'Authorization': auth}

# Make request
response = requests.get(url, data=data, headers=headers)

# Print header banner
print("======================================")
print("LogicMonitor - Get Devices")
print("======================================")
print("Company:", company)
print("URL:", url)
print("======================================")

# Print status and body of response
if response.status_code == 200:
    device_list = response.json()
else:
    print("Error:", response.status_code)
    exit()

# Extract and display device information in table format
if 'data' in device_list:
    devices = device_list['data']['items']

    # Create a list to store device information in tabular format
    table_data = []

    # Loop through devices and append their information to the table_data list
    for device in devices:
        device_id = device['id']
        device_name = device['name']
        device_displayname = device['displayName']
        auto_properties = device.get('autoProperties', [])
        auto_manufacturer = None
        for prop in auto_properties:
            if prop['name'] == 'auto.endpoint.manufacturer':
                auto_manufacturer = prop['value']
                break
        system_properties = device.get('systemProperties', [])
        sysinfo = None
        for prop in system_properties:
            if prop['name'] == 'system.sysinfo':
                sysinfo = prop['value']
                break
        entphysical_descr = None
        for prop in auto_properties:
            if prop['name'] == 'auto.entphysical.descr':
                entphysical_descr = prop['value']
                break
        table_data.append([device_id, device_name, device_displayname, auto_manufacturer, sysinfo, entphysical_descr])

    # Define table headers
    headers = ["Device ID", "Name", "Display Name", "Manufacturer", "Sysinfo", "Description"]

    # Use tabulate to format the table
    table = tabulate(table_data, headers, tablefmt="grid")

    # Print the formatted table
    print(table)
else:
    print("Error: Invalid or missing data in the API response")
    exit()

# Ask the user if they want to proceed with inserting a device ID (y or n)
proceed = input("Do you want to proceed with inserting a device ID? (y/n): ")

if proceed.lower() == 'y':
    # Prompt the user for a device ID
    device_id = input("Enter the device ID: ")

    # Request Info
    httpVerb ='GET'
    resourcePath = f'/device/devices/{device_id}/devicedatasources' # Customize the URL based on the user's input
    data=''
    queryParams =''

    # Construct URL 
    url = 'https://' + company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams

    # Get current time in milliseconds
    epoch = str(int(time.time() * 1000))

    # Concatenate Request details
    requestVars = httpVerb + epoch + data + resourcePath

    # Construct signature
    hmac1 = hmac.new(access_key.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmac1.encode())

    # Construct headers
    auth = 'LMv1 ' + access_id + ':' + signature.decode() + ':' + epoch
    headers = {'Content-Type': 'application/json', 'Authorization': auth}

    # Make request
    response = requests.get(url, data=data, headers=headers)

    # Print status and body of response
    if response.status_code == 200:
        data_dict = response.json()
        items = data_dict.get('data', {}).get('items', [])
    else:
        print("Error:", response.status_code)
        exit()

    # Create an empty list to store the extracted data
    output_data = []

    # Iterate through items and extract the desired information
    for i, item in enumerate(items, start=1):
        data_source_id = item.get('dataSourceId')
        data_source_name = item.get('dataSourceName')
        device_name = item.get('deviceName')
        device_display_name = item.get('deviceDisplayName')
        graphs = item.get('graphs', [])

        # Extract graph IDs
        graph_ids = [graph['id'] for graph in graphs]

        # Append extracted data to the output structure
        output_data.append({
            'Data Source ID': data_source_id,
            'Data Source Name': data_source_name,
            'Device Name': device_name,
            'Device Display Name': device_display_name,
            'Graphs': graph_ids  # Only include graph IDs
        })

        # Calculate and print the progress percentage
        progress_percentage = (i / len(items)) * 100
        print("\rProgress: {:.2f}%".format(progress_percentage), end="")

    print("\n")

    # Save all responses in a JSON file
    output_file = "output/getDeviceDataSources.json"
    with open(output_file, "w") as file:
        json.dump(items, file, indent=4)

    # Display the extracted data in table format
    table_headers = output_data[0].keys()
    table_data = [entry.values() for entry in output_data]

    # Format and print the table
    table = tabulate(table_data, headers=table_headers, tablefmt="pretty")
    print("Extracted Data:")
    print(table)

    # Ask the user if they want to proceed with getting the datasource instances data (y or n)
    proceed = input("Do you want to proceed with getting the datasource instances data? (y/n): ")

    if proceed.lower() == 'y':
        datasource_id = input("Enter the datasource ID: ")

        # Request Info
        httpVerb = 'GET'
        resourcePath = f'/device/devices/{device_id}/devicedatasources/{datasource_id}/instances'  # URL for data sources instances
        data = ''
        queryParams = ''

        # Construct URL
        url = 'https://' + company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams

        # Get current time in milliseconds
        epoch = str(int(time.time() * 1000))

        # Concatenate Request details
        requestVars = httpVerb + epoch + data + resourcePath

        # Construct signature
        hmac1 = hmac.new(access_key.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
        signature = base64.b64encode(hmac1.encode())

        # Construct headers
        auth = 'LMv1 ' + access_id + ':' + signature.decode() + ':' + epoch
        headers = {'Content-Type': 'application/json', 'Authorization': auth}

        # Make request
        response = requests.get(url, data=data, headers=headers)

        # Print status and body of response
        if response.status_code == 200:
            data = response.json()["data"]["items"]
            table_data = []
            for item in data:
                table_data.append([
                    item["deviceDataSourceId"], # Device DataSource ID
                    item["name"], # Name
                    item["deviceDisplayName"], # Device Display Name
                    item["id"],  # DataSource Instances ID
                    item["dataSourceId"],  # DataSource ID
                ])
            
            # Display the table
            headers = ["Device DataSource ID", "Name", "DeviceDisplayName","DataSource Instances ID", "DataSource ID"]
            print(tabulate(table_data, headers, tablefmt="grid"))
        else:
            print("Error:", response.status_code)
            exit()

        # Save the JSON response to a file
        output_file = "output/output_getDatasourceInstances.json"

        print("Done!")

        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
    else:
        print("Exiting without getting the data source instances data.")
        exit()

else:
    print("Exiting without inserting a device ID.")
    exit()