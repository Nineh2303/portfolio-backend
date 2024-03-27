from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
load_dotenv()
config = cloudinary.config(secure=True)
import cloudinary

cloudinary.config(
    cloud_name="nineh2000",
    api_key="862497236931899",
    api_secret="***************************"
)