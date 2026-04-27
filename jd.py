import joblib

# Asumiendo que tus objetos de modelo se llaman model_knn y model_svm
joblib.dump(model_knn, 'modelo_iris_knn.pkl', compress=3)
joblib.dump(model_svm, 'modelo_iris_svm.pkl', compress=3)
