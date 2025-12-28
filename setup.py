from setuptools import setup, find_packages

setup(
    name="j4f-cli-toolkit",
    version="1.0.0",
    author="Sohail",
    description="A professional Python CLI toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "j4f=main:run"
        ]
    },
    python_requires=">=3.8",
)
