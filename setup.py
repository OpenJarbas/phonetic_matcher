from setuptools import setup

setup(
    name='phonetic_matcher',
    version='0.1.2',
    packages=['phonetic_matcher'],
    url='https://github.com/OpenJarbas/phonetic_matcher',
    license='Apache-2.0',
    author='jarbasAi',
    author_email='jarbasai@mailfence.com',
    install_requires=["phonetics",
                      "phoneme_guesser"],
    description='matching strings by phonetics'
)
