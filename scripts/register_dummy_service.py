import requests
from requests.auth import HTTPBasicAuth

# Eureka server URL
eureka_url = 'http://localhost:8761'

# Service details
service_id = 'dummy-service'
instance_info = {
    'instance': {
        'hostName': 'localhost',
        'app': service_id,
        'ipAddr': '127.0.0.1',
        'status': 'UP',
        'port': {'$': 8080, '@enabled': 'true'},
        'vipAddress': service_id,
        'secureVipAddress': service_id,
        'dataCenterInfo': {
            '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
            'name': 'MyOwn'
        }
    }
}

# Headers
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Authentication
auth = HTTPBasicAuth('admin', 'secret')

# Register the service
register_url = f'{eureka_url}/eureka/apps/{service_id}'
response = requests.post(register_url, json=instance_info, headers=headers, auth=auth)

if response.status_code == 200:  # Changed expected status code from 204 to 200
    print(f'Successfully registered {service_id}.')
else:
    print(f'Failed to register {service_id}. Status code: {response.status_code}')

# Verify the registration
apps_url = f'{eureka_url}/eureka/apps'
response = requests.get(apps_url, auth=auth)
if service_id.upper() in response.text:
    print(f'Verification successful: {service_id} is registered.')
else:
    print(f'Verification failed: {service_id} is not registered.')


assert response.status_code == 200, "Failed to register service. Status code: {}".format(response.status_code)
assert service_id.upper() in response.text, "Service is not registered as expected."

