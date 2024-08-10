import requests
from requests.auth import HTTPBasicAuth

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
    try:
        health_check_url = "http://localhost:8761/health"
        health_response = requests.get(health_check_url, auth=HTTPBasicAuth('admin', 'secret'))
        print("health_response: ",health_response)
        assert health_response.status_code == 200, "Eureka server is not accessible or down"
        print("Eureka server is accessible. Proceeding with registration.")

        response = requests.post(url, headers=headers, json=payload, auth=HTTPBasicAuth('admin', 'secret'))
        print("response: ",response)
        assert response.status_code == 204, "Failed to register the dummy service"  # 204 is used here assuming successful registration without response body
        print("Dummy service registered successfully.")
    except Exception as e:
        print(f"Registration failed with exception: {e}")
        raise

if __name__ == "__main__":
    register_dummy_service()
