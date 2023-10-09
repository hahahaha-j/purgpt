import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="purgpt",
    version="0.1.0",
    author="TheCatsMoo",
    author_email="tcm@tcm.gay",
    packages=["purgpt"],
    description="A wrapper for PurGPT... but in python!",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/hahahaha-j/purgpt",
    license='MIT',
    python_requires='>=3.8',
    install_requires=["requests"]
)
