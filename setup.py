import setuptools

setuptools.setup(
    name="fastapi-crud-auth-api",
    version="0.1.0",
    author="Chandan Mohan",
    author_email="chandanmohan2002@gmail.com",
    description="A FastAPI backend for a CRUD API with authentication",
    packages=setuptools.find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
)