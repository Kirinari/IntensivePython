from unittest import TestCase, mock
from assessment import SomeModel, predict_message_mood

def new_predict(message):
    return len(message) / 30

class TestAssessment(TestCase):
    def setUp(self) -> None:
       self.model = SomeModel()
       self.bad = "неуд"
       self.norm = "норм"
       self.good = "отл"

    @mock.patch("assessment.SomeModel.predict")
    def test_bad(self, m_predict):
        message = "они и мы"
        expected = self.bad
        m_predict.return_value = new_predict(message)
        result = predict_message_mood(message, self.model)
        self.assertEqual(result, expected)
        m_predict.assert_called_with(message)

    @mock.patch("assessment.SomeModel.predict")    
    def test_norm(self, m_predict):
        message = "это неплохое сообщение"
        expected = self.norm
        m_predict.return_value = new_predict(message)
        result = predict_message_mood(message, self.model)
        self.assertEqual(result, expected)
        m_predict.assert_called_with(message)

    @mock.patch("assessment.SomeModel.predict")   
    def test_ok(self, m_predict):
        message = "просто идельное сообщение, подходящее идеальному тесту"
        expected = self.good
        m_predict.return_value = new_predict(message)
        result = predict_message_mood(message, self.model)
        self.assertEqual(result, expected)
        m_predict.assert_called_with(message)

    @mock.patch("assessment.SomeModel.predict")        
    def test_empty(self, m_predict):
        message = ""
        m_predict.return_value = new_predict(message)
        result = predict_message_mood(message, self.model)
        self.assertEqual(result, self.bad)
        m_predict.assert_called_with(message)
    
    @mock.patch("assessment.SomeModel.predict")   
    def test_top_edge_norm(self, m_predict):
        message = "aaaaaaaaa тут 24 символа"
        expected = self.norm
        m_predict.return_value = new_predict(message)
        result = predict_message_mood(message, self.model)
        self.assertEqual(result, expected)
        m_predict.assert_called_with(message)
    
    @mock.patch("assessment.SomeModel.predict")   
    def test_bottom_edge_norm(self, m_predict):
        message = "aaa"
        expected = self.bad
        m_predict.return_value = new_predict(message)
        result = predict_message_mood(message, self.model)
        self.assertEqual(result, expected)
        m_predict.assert_called_with(message)
    







