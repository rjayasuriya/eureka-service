import requests

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

# Register the service
register_url = f'{eureka_url}/eureka/apps/{service_id}'
response = requests.post(register_url, json=instance_info)

if response.status_code == 204:
    print(f'Successfully registered {service_id}.')
else:
    print(f'Failed to register {service_id}. Status code: {response.status_code}')

# Verify the registration
apps_url = f'{eureka_url}/eureka/apps'
response = requests.get(apps_url)
if service_id.upper() in response.text:
    print(f'Verification successful: {service_id} is registered.')
else:
    print(f'Verification failed: {service_id} is not registered.')
