import setuptools

with opn('README.md', 'r') as rm:
    long_description = rm.read()

setuptools.setup(name='nlppre',
      version='0.0.1',
      author='Tim Crammond',
      author_email='25987791+tcramm0nd@users.noreply.github.com',
      url='https://github.com/tcramm0nd/nlppre',
      description= 'A NLP Text Processing tool',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=setuptools.find_packages()
      )
