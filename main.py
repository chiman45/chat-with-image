import ollama
import base64
import os

# Encode the image in base64
def encode_image(image_path):
    if not os.path.isfile(image_path):
        print("Image not found. Please check the path.")
        return None
    try:
        with open(image_path, 'rb') as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

# Chat using LLaVA model
def chat_with_image(image_path):
    image_data = encode_image(image_path)
    if image_data is None:
        return "Error: Unable to load or encode image."

    print("You can ask multiple questions about the image. Type 'exit' to quit.")
    
    # Loop for multiple questions
    while True:
        question = input("Your question: ")
        if question.lower() == 'exit':
            print("Exiting the chat.")
            break
        
        try:
            response = ollama.chat(
                model='llava:13b',
                messages=[
                    {"role": "user", "content": question, "images": [image_data]}
                ]
            )
            print("Answer:", response['message']['content'])
        except Exception as e:
            print(f"Error during chat: {e}")

# Get inputs from the user
image_path = input('Enter the image path: ')
chat_with_image(image_path)
