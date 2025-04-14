import joblib
import json
import pandas as pd
import shap

data = '''
{
  "ratio_to_median_purchase_price": 1.945940,
  "online_order": 0,
  "distance_from_home": 57.877857,
  "distance_from_last_transaction": 0.311140
}
'''

features = [
    "ratio_to_median_purchase_price",
    "online_order",
    "distance_from_home",
    "distance_from_last_transaction"
]

model = joblib.load('modelos/modelo_random_forest.joblib')
X_novo = pd.DataFrame([json.loads(data)], columns=features)

print("Classe prevista:", model.predict(X_novo)[0])
print("Probabilidade de fraude:", model.predict_proba(X_novo)[0][1])

# Explicador específico para árvores
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_novo)

# Caso o SHAP retorne múltiplas classes, verifique se o resultado tem mais de uma classe
if isinstance(shap_values, list):
    # Para problemas binários, geralmente temos shap_values[0] para a classe 0 e shap_values[1] para a classe 1
    valores_explicacao = shap_values[1][0] if len(shap_values) > 1 else shap_values[0][0]
else:
    # Para modelos que retornam apenas um valor de explicação (ex.: modelo binário simples)
    valores_explicacao = shap_values[0]

# Garantir que estamos lidando com um array unidimensional, caso haja múltiplos valores
valores_explicacao = valores_explicacao.flatten()

# Juntar as features e explicações
explicacao = list(zip(features, valores_explicacao))

# Ordenar por impacto, agora com a verificação de arrays
explicacao_ordenada = sorted(explicacao, key=lambda x: abs(x[1]), reverse=True)

# Mostrar a explicação
print("\nExplicação da decisão:")
for feature, impacto in explicacao_ordenada:
    print(f"{feature}: impacto {impacto:.3f}")
