import setuptools 

with open('README.md') as file:
    readme = file.read()


setuptools.setup(
    name='wargame-rpa',
    version = '2.0.2',
    packages = setuptools.find_packages(),
    url = 'https://test.pypi.org/simple/wargame-rpa',
    license = 'LICENCE.txt',
    description = 'RPA projekt | Moja igra',
    long_description=readme,
    long_description_content_type='text/markdown',    
    author = 'dseverdi',
    author_email = 'dseverdi@mathos.hr'    
)
