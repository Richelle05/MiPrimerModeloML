import joblib
# Suponiendo que 'model' es tu objeto de modelo entrenado
joblib.dump(model, 'modelo_iris_knn.pkl', compress=3)
