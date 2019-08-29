import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymetno",
    version="0.0.1",
    author="Tormod Haugland",
    author_email="tormod.haugland@gmail.com",
    description="API Wrapper for the met.no API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tOgg1/pymetno",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
