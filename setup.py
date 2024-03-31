from setuptools import setup

f = open('README.md')

long = f.read()

f.close()


setup(
    name="apyoripandas",
    version="0.1.0",
    description="Make easy user Apyori for Pandas",
    author="Matheus de Sá",
    author_email="matheusdesa55@gmail.com",
    url="https://github.com/matheus0sa/apyoripandas",
    packages=["apyoripandas"],
    python_requires=">=3.6",
    long_description=long
)
