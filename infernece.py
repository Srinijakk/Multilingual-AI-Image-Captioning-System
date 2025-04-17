# inference.py

from PIL import Image
from transformers import CLIPProcessor, MBartForConditionalGeneration, MBart50TokenizerFast
import torch

# Load models and tokenizer
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
mbart_tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
mbart_model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

def generate_caption(image_path, target_lang='fr'):
    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt")
    
    # Generate caption in English
    # Assume 'model' is your trained captioning model
    # caption = model.generate_caption(inputs)
    caption = "A placeholder caption."  # Replace with actual model inference
    
    # Translate caption
    mbart_tokenizer.src_lang = "en_XX"
    encoded_caption = mbart_tokenizer(caption, return_tensors="pt")
    generated_tokens = mbart_model.generate(**encoded_caption, forced_bos_token_id=mbart_tokenizer.lang_code_to_id[target_lang])
    translated_caption = mbart_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    
    return translated_caption

if __name__ == "__main__":
    image_path = "path_to_image.jpg"
    caption = generate_caption(image_path, target_lang='fr')
    print(f"Translated Caption: {caption}")
