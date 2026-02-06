class IntentModel:
    """
    Simple ML-style intent classifier.
    This simulates a trained ML model.
    """

    def predict(self, texts):
        text = texts[0].lower()

        if "calculate" in text or any(char.isdigit() for char in text):
            return ["math"]

        if len(text.split()) <= 4:
            return ["simple"]

        return ["reasoning"]
