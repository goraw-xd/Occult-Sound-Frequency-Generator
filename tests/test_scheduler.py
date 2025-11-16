def test_schedule_event():
    from core.scheduler.event_scheduler import schedule_event
    assert schedule_event({'name':'test'})
