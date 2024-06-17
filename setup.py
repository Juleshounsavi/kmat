from setuptools import setup, find_packages
setup(
    name = "kmat",
    version = "0.0.1",
    author = "HOUNSAVI Jules Koffi",
    author_email = "hounsavijuleskoffi@gmail.com",
    url = "",
    description = "A package for matrix operations.",
    packages = find_packages(),
    readme = "README.md",
    install_requires = "none",
    python_requires = ">=3.11",
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
