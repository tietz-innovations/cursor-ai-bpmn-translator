from setuptools import setup, find_packages

setup(
    name="bpmn-translator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "bpmn-python>=0.0.23",
        "networkx>=2.6.3",
        "click>=8.0.0",
    ],
    author="Tietz Innovations",
    author_email="contact@tietz-innovations.com",
    description="A BPMN to Natural Language translator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tietz-innovations/cursor-ai-bpmn-translator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "bpmn-translate=bpmn_translator.__main__:cli",
        ],
    },
)