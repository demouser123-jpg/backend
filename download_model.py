import gdown
import os

def download_model():
    # Your Google Drive file ID
    file_id = "15u2GY0686FkJ0Dmzu6d8BMxMAB7haBGN"
    
    # Path where the model will be saved
    output_path = os.path.join(os.path.dirname(__file__), "model.h5")
    
    # If the model already exists, don't download it again
    if os.path.exists(output_path):
        print("Model already exists at:", output_path)
        return output_path
    
    # Create the Google Drive download URL
    url = f"https://drive.google.com/uc?id={file_id}"
    
    print("Downloading model from Google Drive...")
    gdown.download(url, output_path, quiet=False)
    print("Model downloaded successfully to:", output_path)
    
    return output_path

if __name__ == "__main__":
    download_model()
