import os
from setuptools import find_packages, setup
from pathlib import Path


PACKAGE_NAME = "entmax"

here = Path(__file__).parent

about = {}

exec(
    (here / PACKAGE_NAME.replace('.', os.path.sep) / "__version__.py").read_text(
        encoding="utf-8"
    ),
    about,
)

setup(name='entmax',
      version=about['__version__'],
      url="https://github.com/deep-spin/entmax",
      author="Ben Peters, Goncalo M Correia, Vlad Niculae",
      author_email="vlad@vene.ro",
      description=("The entmax mapping and its loss, a family of sparse "
                   "alternatives to softmax."),
      license="MIT",
      packages=find_packages(),
      install_requires=['torch>=1.0'],
      python_requires=">=3.5")
