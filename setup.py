from distutils.core import setup
setup(
  name = 'babyavi',
  packages = ['babyavi'],
  version = '0.1',
  license='MIT',
  description = 'Simplest codes you ever seen baby!',
  author = 'Aviral Bhardwaj',
  author_email = 'ardb40@gmail.com',
  url = 'https://github.com/aviralb/babyavi',
  download_url = 'https://github.com/aviralb/babyavi/blob/master/dist/babyavi.tar.gz',
  keywords = ['alzebra', 'maths', 'multiplication', 'prime number', 'rivision', 'formuals', 'fun', 'codes'],
  install_requires=[
          'numpy',
          'sklearn',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)