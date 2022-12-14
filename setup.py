from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='1.0',
      description='Sorts files in a folder',
      url='https://github.com/DanielDDZ/clean_folder',
      author='Daniel Zubov',
      author_email='danielzubov12@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'clean-folder = clean_folder.clean:main']}
      )
