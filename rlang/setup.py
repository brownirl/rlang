import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rlang",
    version="1.0.0",
    author="Anonymous",
    author_email="",
    description="For specifying partial information about MDPs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="rlang.ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
