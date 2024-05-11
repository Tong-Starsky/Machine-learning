import joblib

class AQY_predict_Model:
    def __init__(self):
        self.predictor = None

    def load_models(self):
        print("load_models")
        self.predictor = joblib.load(f".\\Fusion_model.joblib")

aqy_predict_Model = AQY_predict_Model()
aqy_predict_Model.load_models()