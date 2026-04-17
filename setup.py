from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fuel-agent-kit",
    version="0.1.0",
    author="Jonathan Zhang",
    author_email="jonathan7591@example.com",
    description="Python SDK for building AI agents on Fuel blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathan7591/fuel-agent-kit-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "web3>=6.0.0",
        "pydantic>=2.0.0",
        "openai>=1.0.0",
        "anthropic>=0.8.0",
        "google-generativeai>=0.3.0",
        "langchain>=0.1.0",
        "python-dotenv>=1.0.0",
        "aiohttp>=3.8.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
        ],
    },
)
