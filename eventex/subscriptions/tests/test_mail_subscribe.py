from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Victor Bezerra', cpf='12345678901',
                    email='victor.tbez@gmail.com', phone='83-988982597')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'victor.tbez@gmail.com'  # troquei o contato@eventex

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['victor.tbez@gmail.com', 'victor.tbez@gmail.com']  # troquei o contato@eventex

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Victor Bezerra',
            '12345678901',
            'victor.tbez@gmail.com',
            '83-988982597'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
