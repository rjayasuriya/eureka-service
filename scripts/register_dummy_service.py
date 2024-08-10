import requests
from requests.auth import HTTPBasicAuth
import json
import subprocess


def register_dummy_service():
    url = "http://localhost:8761/eureka/apps/dummy-service"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "instance": {
            "hostName": "dummyhost",
            "app": "DUMMY-SERVICE",
            "ipAddr": "127.0.0.1",
            "status": "UP",
            "port": {"$": "8080", "@enabled": "true"},
            "securePort": {"$": "443", "@enabled": "false"},
            "healthCheckUrl": "http://dummyhost:8080/health",
            "statusPageUrl": "http://dummyhost:8080/status",
            "homePageUrl": "http://dummyhost:8080",
            "dataCenterInfo": {
                "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                "name": "MyOwn"
            }
        }
    }
    # Running curl command first
    curl_command = [
        'curl',
        '-X', 'POST',
        'http://localhost:8761/eureka/apps/dummy-service',
        '-u', 'admin:secret',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps(payload),
        '-v'
    ]
    try:
        # Execute the curl command
        process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Output the results
        print("Curl command output:")
        print(stdout.decode())
        if stderr:
            print("Curl command error output:")
            print(stderr.decode())

        # Check for errors
        if process.returncode != 0:
            print("Curl command failed with return code:", process.returncode)

        # Request to get all available Actuator endpoints
        actuator_url = "http://localhost:8761/actuator"
        actuator_response = requests.get(actuator_url, auth=HTTPBasicAuth('admin', 'secret'))
        print("actuator_response",actuator_response)

        # Pre-check: Verify the Eureka server is accessible and responding
        health_check_url = "http://localhost:8761/actuator/health"
        health_response = requests.get(health_check_url, auth=HTTPBasicAuth('admin', 'secret'))
        print("Health check response status code:", health_response.status_code)
        print("Health check response content:", health_response.text)
        assert health_response.status_code == 200, "Eureka server is not accessible or down"

        print("Eureka server is accessible. Proceeding with registration.")

        response = requests.post(url, headers=headers, json=payload, auth=HTTPBasicAuth('admin', 'secret'))
        print("response: ",response)
        print("Registration response status code:", response.status_code)
        print("Registration response headers:", response.headers)
        print("Registration response body:", response.text)
        assert response.status_code == 204, "Failed to register the dummy service"  # 204 is used here assuming successful registration without response body
        print("Dummy service registered successfully.")
    except Exception as e:
        print(f"Registration failed with exception: {e}")
        raise

if __name__ == "__main__":
    register_dummy_service()
