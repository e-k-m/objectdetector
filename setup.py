from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

version = {}
with open("objectdetector/version.py") as f:
    exec(f.read(), version)

setup(
    name="objectdetector",
    version=version["__version__"],
    description="Objekt detection in georeferenced arial images.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/e-k-m/objectdetector",
    author="Eric Matti",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="objectdetector",
    packages=find_packages(include=["objectdetector", "objectdetector.*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "mercantile",
        "requests",
        "label-studio"
    ],
    entry_points={"console_scripts": ["objectdetector=objectdetector.cli:main"]},
)
