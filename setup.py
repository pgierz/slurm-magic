from setuptools import setup

README = open("README.md").read()

setup(
    author="Paul Gierz",
    author_email="pgierz@awi.de",
    description="IPython magic for SLURM.",
    long_description=README,
    name="slurm-magic",
    py_modules=["slurm_magic"],
    install_requires=["ipython", "pandas"],
    url="https://github.com/pgierz/slurm-magic",
    version="0.1.0",
)
