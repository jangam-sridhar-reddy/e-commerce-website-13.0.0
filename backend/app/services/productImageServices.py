import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os
import uuid
from fastapi import UploadFile

load_dotenv()



# Configuration       
cloudinary.config( 
    cloud_name = f"{os.getenv('CLOUD_NAME')}", 
    api_key = f"{os.getenv('API_KEY')}", 
    api_secret = f"{os.getenv('API_SECRET')}", 
    secure=True
)

# upload an image
async def upload_image_to_cloudinary(image: UploadFile, product_name: str) -> str:
     # Read file content from UploadFile
    contents = await image.read()

    # Generate a unique public_id for the image (safe from duplicates)
    unique_id = f"{product_name.replace(' ', '_')}_{uuid.uuid4().hex[:6]}"
    folder = "ecommerce/products"
    full_public_id = f"{folder}/{unique_id}"
    
    # Upload image to Cloudinary
    upload_result = upload(
        contents,
        public_id=unique_id,
        resource_type="image",
        folder=folder
    )

     # Get basic image URL
    image_url = upload_result.get("secure_url")

    # Optimized image URL
    optimized_url, _ = cloudinary_url(
        full_public_id,
        fetch_format="auto",
        quality="auto" 
    )

    # Cropped version (square aspect ratio, auto-gravity focus)
    cropped_url, _ = cloudinary_url(
        full_public_id,
        width=500,
        height=500,
        crop="auto",
        gravity="auto" 
    )

    return {
        "original_url": image_url,
        "optimized_url": optimized_url,
        "cropped_url": cropped_url,
        "public_id": unique_id
    }
