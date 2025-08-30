import torch

print(torch.__version__)

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available. Using GPU.")
    device = torch.device("cuda")
else:
    print("CUDA is not available. Using CPU.")
    device = torch.device("cpu")



# Empty Tensor creation

et = torch.empty(3,4) # It will create tensor of size 3x4 with uninitialized values
print(et)

print(type(et)) # It will print the type of the tensor

et = torch.zeros(3,4)

print(et)
et = torch.ones(3,4)
print(et)


et = torch.rand(3,4) # It will create a tensor of size 3x4 with random values between 0 and 1
print(et)

