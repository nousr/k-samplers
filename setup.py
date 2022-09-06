from setuptools import setup, find_packages

setup(
    name="k-samplers",
    version="0.0.1",
    description="Samplers from crowsonkb/k-diffusion",
    packages=find_packages(),
    install_requires=[
        "scipy",
        "torch",
        "torchdiffeq",
        "torchvision",
        "tqdm",
    ],
)
