from setuptools import setup


setup(
    name="say-jira",
    version="0.0.1",
    description="Adds a jira ticket to the beginning of a commit message",
    author="Svyatoslav Blokhin",
    keywords="git commit pre-commit hook commit msg message python",
    platforms=["Any"],
    packages=["say_jira"],
    scripts=["say-jira"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "poetry"
    ],
    classifiers=[
        "Development Status :: In Development",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)
