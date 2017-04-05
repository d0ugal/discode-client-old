import setuptools

from discode import VERSION

setuptools.setup(
    name="discode",
    version=VERSION,
    url="https://github.com/d0ugal/discode",
    license="BSD",
    description="Quick code review",
    long_description=(
        "A simple utility to help you use www.discode.co from the command "
        "line. See `discode --help` for more details."),
    author="Dougal Matthews",
    author_email="dougal@dougalmatthews.com",
    keywords='code review codereview discussion',
    py_modules=['discode', ],
    include_package_date=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'discode = discode:main',
        ]
    },
    classifier=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Utilities'
    ],
)
