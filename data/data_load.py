from config import batch_size
import torch
import torchvision
import torchvision.transforms as transforms

transform=transforms.Compose([
    transforms.ToTensor(),
#     transforms.Normalize((0.1307,), (0.3081,))
    ])

# 加载训练数据和测试数据到train_data, test_data
train_data = torchvision.datasets.MNIST('../data', train=True, download=True,
                   transform=transform)
test_data = torchvision.datasets.MNIST('../data', train=False,
                   transform=transform)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size,
                                          shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False)