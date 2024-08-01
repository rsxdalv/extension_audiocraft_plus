import setuptools

# todo - fix metadata
setuptools.setup(
    name="extension_audiocraft_plus",
    packages=setuptools.find_namespace_packages(),
    version="2.0.2",
    author="lj1995",
    description="An easy-to-use Voice Conversion framework based on VITS",
    url="https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI",
    project_urls={},
    scripts=[],
    # include_package_data=True,
    # include JSON files
    # package_data={
    #     "": ["*.json"],
    # },
    install_requires=[
        "audiocraft>=1.2",
        "pytaglib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
