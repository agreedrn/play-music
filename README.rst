play-music
=============

play-music is a Python library for manipulating WAV files or Numpy Arrays

Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`__ to
install play-music.

.. code:: bash

    pip install play-music

Usage
-----

play music from wavfile:

.. code:: python

    import play-music

    if __name__ == "__main__":
        process = play-music.playMusic("alarm.wav", loop=False, threaded=False)

play music on loop:

.. code:: python

    import play-music

    if __name__ == "__main__":
        process = play-music.playMusic("alarm.wav", loop=True, threaded=True)

play music asynchronous:

.. code:: python

    import play-music

    if __name__ == "__main__":
        process = play-music.playMusic("alarm.wav", loop=False, threaded=True)

stop all sounds:

.. code:: python

    import play-music, time

    if __name__ == "__main__":
        process = play-music.playMusic("alarm.wav", loop=True, threaded=True)
        time.sleep(1)
        play-music.stopAllSounds()

stop specific sound:

.. code:: python

    import play-music, time

    if __name__ == "__main__":
        process = play-music.playMusic("alarm.wav", loop=True, threaded=True)
        process2 = play-music.playMusic("alarm2.wav", loop=True, threaded=True)
        time.sleep(1)
        play-music.stopSpecificSound(process)

stop specific sounds:

.. code:: python

    import play-music, time

    if __name__ == "__main__":
        sounds_to_stop = []
        process = play-music.playMusic("alarm.wav", loop=True, threaded=True)
        sounds_to_stop.append(process)
        process2 = play-music.playMusic("alarm2.wav", loop=True, threaded=True)
        sounds_to_stop.append(process2)
        process3 = play-music.playMusic("alarm2.wav", loop=True, threaded=True)
        time.sleep(1)
        play-music.stopSpecificSounds(sounds_to_stop)

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`__
