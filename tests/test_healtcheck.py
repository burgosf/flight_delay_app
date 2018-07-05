from tests.base import BaseTest


class HealthcheckTestCase(BaseTest):
    def test_healthcheck(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
