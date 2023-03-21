import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='consume',
    version='0.0.1',
    author='J. "Dorian Greyson" L.',
    author_email='greysondn@gmail.com',
    description='Text game engine',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/greysondn/Consume',
    project_urls = {
        "Bug Tracker": "https://github.com/greysondn/Consume/issues"
    },
    packages=['iguttae'],
    install_requires=[
    ],
)