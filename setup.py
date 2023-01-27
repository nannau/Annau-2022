from setuptools import setup

setup(
   name='Annau2023',
   version='0.1.0',
   author='Nic Annau',
   author_email='nicannau@gmail.com ',
   packages=['Annau2023'],
   # scripts=[
   #    'models/generator.py',
   #    'models/critic.py',
   #    'SRModel.py',
   #    'RAPSD.py'
   # ],
   license='LICENSE',
   description='Python module to produce figures and analysis in Annau-2022. Model training is a separate project.',
   long_description=open('README.md').read(),
   install_requires=[
         "mlflow",
         "torch",
         "torchvision",
         "numpy",
         "matplotlib",
         "scipy",
         ],
)