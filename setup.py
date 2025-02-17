import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygellan",
    version="0.0.3",
    author="Henry Pinkard",
    author_email="henry.pinkard@gmail.com",
    description="Open source microscope control using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henrypinkard/Pygellan",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'dask>=2.1.0', 'zmq'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)