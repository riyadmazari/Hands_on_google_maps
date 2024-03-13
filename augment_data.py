import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def augment_images_from_folder(folder, img_size=(64, 64), augmentations=10):
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
            img = cv2.resize(img, img_size)  # Resize to your desired input size
            img = np.expand_dims(img, axis=0)  # Add batch dimension
            augmented_images = datagen.flow(img, batch_size=1)

            for i in range(augmentations):
                batch = next(augmented_images)
                augmented_image = batch[0].astype('uint8')
                cv2.imwrite(os.path.join(folder, f'aug_{filename.split(".")[0]}_{i}.jpg'), cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR))

# List of directories to augment
gestures = ['Up', 'Down', 'Right', 'Left', 'In', 'Out']
for gesture in gestures:
    augment_images_from_folder(os.path.join('', gesture))
