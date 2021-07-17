from distutils.core import setup
with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
  name = 'play-music',         # How you named your package folder (MyLib)
  packages = ['play-music'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'PyPi library which allows you to play wav files or numpy arrays',   # Give a short description about your library
  author = 'agreedrn',                   # Type in your name
  author_email = 'rishinachnani@hotmail.com',      # Type in your E-Mail
  long_description=long_description,
  long_description_content_type="reStructuredText",
  url = 'https://github.com/agreedrn/play-music',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/agreedrn/play-music/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  keywords = ['SOUND_EFFECTS', 'MUSIC', 'WAV', 'MANIPULATE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'simpleaudio',
	        'numpy'
      ],
  classifiers=[
    'Development Status :: 4 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)