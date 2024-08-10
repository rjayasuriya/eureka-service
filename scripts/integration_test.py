import subprocess

def run_curl_command():
    print("Running curl command to check Eureka server status at http://localhost:8761/eureka/apps")
    command = "curl -X GET http://localhost:8761/eureka/apps"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    output, error = process.communicate()

    print("Curl command output:")
    print(output.decode('utf-8'))

    if error:
        print("Curl command error output:")
        print(error.decode('utf-8'))
    print("Test passed")
    assert process.returncode == 0, "Curl command failed"

if __name__ == "__main__":
    run_curl_command()
