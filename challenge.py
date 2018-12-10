import torch
from torch import nn
import torch.nn.functional as F
from torchvision import models
from collections import OrderedDict


def load_checkpoint(checkpoint_path):
    checkpoint = torch.load(checkpoint_path, map_location='cpu')

    model = models.vgg16(pretrained=False)
    num_features = model.classifier[0].in_features
    for param in model.parameters():
        param.requires_grad = False

    # Put the classifier on the pretrained network
    model.classifier = nn.Sequential(OrderedDict([
        ('fc1', nn.Linear(num_features, 512)),
        ('relu', nn.ReLU()),
        ('drpot', nn.Dropout(p=0.5)),
        ('hidden', nn.Linear(512, 100)),
        ('fc2', nn.Linear(100, 102)),
        ('output', nn.LogSoftmax(dim=1)),
    ]))

    model.load_state_dict(checkpoint['state_dict'])

    return model


# Load your model to this variable
model = load_checkpoint('vgg16_flower.pth')

# If you used something other than 224x224 cropped images, set the correct size here
image_size = 224
# Values you used for normalizing the images. Default here are for
# pretrained models from torchvision.
norm_mean = [0.485, 0.456, 0.406]
norm_std = [0.229, 0.224, 0.225]