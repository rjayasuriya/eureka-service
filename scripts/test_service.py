import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

def test_eureka_status():
    print("Testing if Eureka server is accessible at http://localhost:8761/eureka/apps")
    try:
        response = requests.get("http://localhost:8761/eureka/apps", auth=HTTPBasicAuth('admin', 'secret'))
        print(f"Received status code: {response.status_code}")
        print("Response Body:")
        print(response.text)  # Print the raw response body
        assert response.status_code == 200, "Eureka server is not accessible"
        print("Eureka server is up and running.")

        # Parse the XML response
        root = ET.fromstring(response.content)
        print("Parsed XML response from Eureka:")
        print(ET.dump(root))  # Dumps the tree structure of the XML

        # Further checks on response content, example check for versions__delta
        versions_delta = root.find('.//versions__delta')
        assert versions_delta is not None, "No versions__delta element found in response"
        print(f"versions__delta: {versions_delta.text}")

    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

if __name__ == "__main__":
    test_eureka_status()
