import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

print("Testing if Eureka server is accessible at http://localhost:8761/eureka/apps")
response = requests.get("http://localhost:8761/eureka/apps", headers={'Accept': 'application/xml'}, auth=HTTPBasicAuth('admin', 'secret'))
print(f"Received status code: {response.status_code}")

if response.status_code == 200:
    print("Eureka server is up and running.")
    root = ET.fromstring(response.content)
    print("Parsed XML response from Eureka:")
    versions_delta = root.find('.//versions__delta')
    if versions_delta is not None:
        print(f"versions__delta: {versions_delta.text}")
        print("Test passed")
    else:
        print("No versions__delta element found in response. Test failed.")
else:
    print("Eureka server is not accessible. Test failed.")
