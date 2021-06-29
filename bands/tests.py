from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Band


class BandTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(
      username="testuser1", password="pass"
    )
    testuser1.save()

    test_band = Band.objects.create(
      reviewer=testuser1,
      name="Behemoth",
      description="Scary polish band",
    )
    test_band.save()

  def test_band_content(self):
    band = Band.objects.get(id=1)
    actual_reviewer = str(band.reviewer)
    actual_name = band.name
    actual_description = band.description

    expected_reviewer = "testuser1"
    expected_name = "Behemoth"
    expected_description = "Scary polish band"

    self.assertEqual(actual_reviewer, expected_reviewer)
    self.assertEqual(actual_name, expected_name)
    self.assertEqual(actual_description, expected_description)