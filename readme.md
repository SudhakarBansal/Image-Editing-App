# ImageMorph - Flask Image Processing Web App

## Overview

This project is a Flask-based web application that allows users to upload images and perform various processing tasks such as converting the image to grayscale or changing the image format (e.g., JPG, PNG, WebP). The app is built using Flask, OpenCV, and HTML templates to offer a simple and efficient interface for basic image manipulation.

---

## Features

- **Image Upload**: Upload images in common formats like JPG, PNG, GIF, and PDF.
- **Image Processing Options**: 
  - Convert image to grayscale.
  - Convert the image format to PNG, JPG, or WebP.
- **User-Friendly Interface**: A simple and intuitive UI where users can upload images, select an operation, and download the processed image.
- **Real-time Processing**: Images are processed and available for download immediately after uploading.

---

## Screenshots

### 1. Home Page

The home page allows users to upload images and choose the operation they want to perform.

![1](https://github.com/user-attachments/assets/ea45ffc6-c6da-4d62-a754-29cb2a5e5211)


---

### 2. Image Processing Options

Once an image is uploaded, users can choose between converting the image to grayscale or changing its format.

![2](https://github.com/user-attachments/assets/964309f2-a763-428b-90b2-4e05d6cfc906)

---

### 3. Processed Image Download

After selecting the operation, users can download the processed image using the generated link.

![3](https://github.com/user-attachments/assets/4e197b1a-123a-4c78-adee-b2cee66fad72)

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```


### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
Make sure you have OpenCV installed:
```bash
pip install opencv-python
```

### 3. Run the Application
```bash
python main.py

```

Open your web browser and go to http://127.0.0.1:5000 to access the application.

---

## File Structure

```

|── main.py                  # Main Flask application
|── templates
|   └── index.html           # HTML template for UI
|── static
|   └── processed images     # Directory where processed files are saved
|── uploads                  # Folder to store uploaded files


```

