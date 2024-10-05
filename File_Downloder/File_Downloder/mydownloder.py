import requests
import os

def download_file(url, file_name):
    if os.path.exists(file_name):
         print(f"file '{file_name}' already exists. Please provide a different file name.")
         return
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
	url = 'https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/6e61b/MainAfter.png'
	file_name = 'img.png'
	download_file(url, file_name)