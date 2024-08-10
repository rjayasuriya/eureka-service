import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

# Eureka server URL and service details
eureka_url = 'http://localhost:8761'
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

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
auth = HTTPBasicAuth('admin', 'secret')

# Register the service
register_url = f'{eureka_url}/eureka/apps/{service_id}'
response = requests.post(register_url, json=instance_info, headers=headers, auth=auth)
if response.status_code != 200:
    print(f"Failed to register service. Status code: {response.status_code}")
else:
    print("Service registered successfully.")

# Verify the registration
apps_url = f'{eureka_url}/eureka/apps'
response = requests.get(apps_url, headers={'Accept': 'application/xml'}, auth=auth)
root = ET.fromstring(response.content)
service_registered = False
for application in root.findall('./application'):
    name = application.find('name')
    if name is not None and service_id.upper() == name.text.upper():
        service_registered = True
        break

if service_registered:
    print(f'Verification successful: {service_id} is registered.')
else:
    print(f'Verification failed: {service_id} is not registered.')

assert response.status_code == 200, "Failed to register service. Status code: {}".format(response.status_code)
assert service_id.upper() in response.text, "Service is not registered as expected."

