class SomeModel:
    def predict(self, message: str) -> float:
        word_count = len(message.split())
        short_words = 0
        for i in message.split():
            if len(i) <= 3:
                short_words += 1
        return 1 - short_words / word_count

def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    res = model.predict(message)
    if res < bad_thresholds:
        return "неуд"
    elif res > good_thresholds:
        return "отл"
    else:
        return "норм"
    
model = SomeModel()