__version__ = "0.27"

# 
def get_requirements():
    """Get requirements for product environment, write the requirements of 
    development environment in 'pygubudesigner.sh' file.

    Returns:
        list: The requirements for product environment.
    """

    return [
        # ("require","version","license","project_url")
        (
            "appdirs",
            ">=1.4.3",
            "MIT License",
            "http://github.com/ActiveState/appdirs",
        ),
        (
            "Mako",
            ">=1.1.4",
            "MIT License",
            "https://github.com/sqlalchemy/mako",
        ),
        (
            "screeninfo",
            ">=0.8",
            "MIT License",
            "https://github.com/rr-/screeninfo",
        ),
        (
            "pygubu",
            ">=0.22",
            "MIT License",
            "https://github.com/alejandroautalan/pygubu",
        ),
    ]

def  get_product_requirements():
    return get_requirements()

def get_setup_requirements():
    return [r[0] + r[1] for r in get_requirements()]
