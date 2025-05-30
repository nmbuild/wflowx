from setuptools import setup, find_packages

setup(
  name="ci_converter",
  version="0.1",
  packages=find_packages(),
  install_requires=["pyyaml"],
  entry_points={
    "console_scripts": [
      "ci-convert=ci_converter.cli:main"
    ]
  }
)
