import pytest
from celery.result import EagerResult


from meeting_tool_backend.users.tasks import get_users_count
from meeting_tool_backend.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_count(settings):
    """A basic test to execute the get_users_count Celery task."""
    UserFactory.create_batch(3)
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = get_users_count.delay()
    assert isinstance(task_result, EagerResult)
    assert task_result.result == 3
