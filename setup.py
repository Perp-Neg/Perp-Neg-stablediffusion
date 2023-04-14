from setuptools import setup

setup(
    name="perpneg-diffusion",
    packages=[
        "perpneg_diffusion",
        "perpneg_diffusion.perpneg_stable_diffusion",
    ],
    install_requires=[
        "Pillow",
        "attrs",
        "torch",
        "filelock",
        "requests",
        "tqdm",
        "ftfy",
        "regex",
        "numpy",
        "blobfile",
        "torchvision",
        "diffuser",
        "transformers"
    ],
    author="huangjie and reza",
    version='2.0',
)
