import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim

def get_image_similarity(img1, img2):
    # Convert images to grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Resize images to a fixed size (20x20 pixels)
    resized_img1 = cv2.resize(gray_img1, (20, 20))
    resized_img2 = cv2.resize(gray_img2, (20, 20))
    
    # Calculate structural similarity index (SSIM)
    similarity = ssim(resized_img1, resized_img2)
    
    
    return similarity

def find_most_similar_images(image_folder):
    image_files = os.listdir(image_folder)
    
    similar_pairs = []
    
    # Iterate through all pairs of images
    for i in range(len(image_files)):
        img1 = cv2.imread(os.path.join(image_folder, image_files[i]))
        
        for j in range(i+1, len(image_files)):
            img2 = cv2.imread(os.path.join(image_folder, image_files[j]))
            
            # Calculate similarity between the two images
            similarity = get_image_similarity(img1, img2)
            
            # Add the pair and similarity value to the list
            similar_pairs.append((image_files[i], image_files[j], similarity))
    
    # Sort the similar pairs based on similarity value (descending order)
    similar_pairs.sort(key=lambda x: x[2], reverse=True)
    
    return similar_pairs

# Klasör yolu
image_folder_path = "C:/AA_ODEV_1200505017/ALGORITMA_ANALIZI_ODEV_SOURCES"

# En çok benzeyen görselleri bul
similar_images = find_most_similar_images(image_folder_path)

# Sonuçları yazdır
for pair in similar_images:
    img1_name, img2_name, similarity = pair
    print(f"{img1_name} ve {img2_name} görselleri {similarity} benzerlik skoruyla en çok benzeyenlerdir.")
