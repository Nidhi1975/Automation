from setuptools import setup, find_packages

setup(
    name="test-automation-framework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.15.2",
        "pytest>=7.4.3",
        "webdriver-manager>=4.0.1",
        "pytest-pythonpath>=0.7.3",
    ],
)