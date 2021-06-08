from setuptools import setup, find_namespace_packages

setup(
    name='tacklebox_webhooks',
    version='0.1.3',
    description='An open-source serverless framework that offers webhooks as a service.',
    url='https://github.com/tacklebox-webhooks/python',
    author='Juan Palma, Kayl Thomas, Kevin Counihan, Armando Mota',
    author_email='juanpedropalma@hotmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    py_modules=['tacklebox_webhooks'],
    install_requires=['requests'],
    zip_safe=False
)