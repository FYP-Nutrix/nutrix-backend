import requests


def requestImageName(food_image):
    endpoint = "https://nutrifitai-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/f796fbfd-a4dd-473f-918a-2716ed03620c/detect/iterations/Iteration6/image"

    headers = {
        "Prediction-Key": "9af3ccfe487d4987aaf96fb84f2da07e",
        "Content-Type": "application/octet-stream"
    }

    food_image.seek(0)
    binary_content = food_image.read()

    response = requests.request(
        "POST", endpoint, headers=headers, data=binary_content)

    data = response.json()
    food_name = data['predictions'][0]['tagName']
    
    return food_name
