import pytest
from django.urls import reverse

from project_name.django_assertions import assert_contains, assert_equal


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_title(resp):
    assert_contains(resp, '<title>Project Name</title>')


