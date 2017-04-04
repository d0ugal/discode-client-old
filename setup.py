import setuptools

setuptools.setup(
    name="discode",
    version="0.0.3",
    url="https://github.com/d0ugal/discode-cli",
    license="MIT",
    description="Quick code review",
    long_description="TODO",
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
