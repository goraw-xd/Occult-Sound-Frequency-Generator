def test_fetch_ephemeris():
    from core.planetary.api_gateway import fetch_ephemeris
    try:
        fetch_ephemeris({})
    except NotImplementedError:
        pass
    else:
        assert False, 'Expected NotImplementedError'
