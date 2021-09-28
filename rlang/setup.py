import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rlang-irl",
    version="0.1.0",
    author="Benjamin Spiegel",
    author_email="bspiegel@cs.brown.edu",
    description="A symbolic interface to grounded agent knowledge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafarodsa/lmdp",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
