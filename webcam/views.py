from django.shortcuts import render
import torch
from ultralytics import YOLO
import cv2
# from PIL import ImageGrab
# display = utils.notebook_init()  # YOLOv5 설정

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\myproject\\webcam\\best_10.pt')  # 모델 로드
# model = YOLO('yolov8n.yaml')  # build a new model from scratch
model = YOLO('webcam\\best.pt')  # load a pretrained model (recommended for training)

def index(request):
    return render(request, 'webcam/index.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import pandas
import numpy as np
import io

def english_study(request):
    return render(request, 'english-study.html')

def draw(request):
    return render(request, template_name='draw.html')

def quiz(request):
    return render(request, 'quiz.html')

def game(request):
    return render(request, 'game.html')

@csrf_exempt
def detect(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # YOLOv5 모델로 이미지 분석
        # results = model(image, size=640)
        image_np = np.array(image)
        image_np = np.expand_dims(image_np, axis=0)
        image_np = image_np.transpose(0, 3, 1, 2)

        
        image_tensor = torch.from_numpy(image_np).float()
        if torch.cuda.is_available():
            image_tensor = image_tensor.to('cuda')
        
        results = model(image_tensor)
        
       
        class_idx = results[0].probs.top1
        class_list = ["Apple", "Banana", "Cat", "Lion"]

        return JsonResponse({'class_names': class_list[class_idx], 'class_idx': class_idx})

    return JsonResponse({'error': 'Invalid request'})