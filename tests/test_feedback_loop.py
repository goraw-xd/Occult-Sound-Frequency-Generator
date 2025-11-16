def test_feedback_analyze():
    from core.feedback.feedback_analyzer import analyze
    assert isinstance(analyze(None), dict)
