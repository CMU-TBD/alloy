import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='alloylib',
      version='0.0.2',
      description='Lab Library for Commonly used Modules/Functions',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Xiang Zhi Tan',
      url='https://github.com/CMU-ARM/alloy',
      author_email='zhi.tan@ri.cmu.edu',
      packages=setuptools.find_packages(),
      install_requires=[
          'numpy',
          'pyquaternion'
      ],
      license='MIT'
)
