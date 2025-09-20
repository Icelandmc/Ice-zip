from setuptools import setup, find_packages

setup(
    name="icezip",
    version="1.0.0",
    description="Advanced lightweight ICEZIP archive tool",
    author="YourName",
    author_email="you@example.com",
    url="https://github.com/username/icezip",
    py_modules=["icezip"],
    entry_points={
        "console_scripts": ["icezip=icezip:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7"
)
