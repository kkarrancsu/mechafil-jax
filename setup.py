import setuptools

setuptools.setup(
    name="mechafil_jax",
    version="0.1",
    packages=["mechafil_jax"],
    install_requires=[
        "jax", 
        "jaxlib", 
        "numpy", 
        "scipy", 
        "matplotlib",
        "mechaFIL",  # for testing & for data downloads
    ],

    tests_require = [
        'pytest',
    ]
)