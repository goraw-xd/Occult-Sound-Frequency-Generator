def test_map_intention():
    from core.ai_engine.intention_mapper import map_intention
    assert map_intention('I want healing') == '528'
