def test_play_tone():
    from core.dsp.synth_engine import play_tone
    assert play_tone(440, 0.1) is None
