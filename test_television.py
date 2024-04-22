from television import Television
from television import *



def test_power():
    tv = Television()
    tv.power()
    assert str(tv)
    tv.power()
    assert str(tv)

def test_init():
    tv = Television()
    assert str(tv)


def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv)

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv)


def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv)
    tv.mute()
    tv.volume_down()
    assert str(tv)


def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv)
    tv.mute()
    assert str(tv)

    tv.power()
    tv.mute()
    assert str(tv)

    tv.mute()
    assert str(tv)



def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv)
    tv.mute()
    tv.volume_up()
    assert str(tv)
    tv.volume_up()
    tv.volume_up()
    assert str(tv)


def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv)




if __name__ == '__main__':
    main()

