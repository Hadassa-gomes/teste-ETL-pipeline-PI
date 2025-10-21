from datetime import datetime
import math


def clean_reading(temp: float, hum: float) -> dict:
    # 1️⃣ Verifica se valores estão ausentes
    if temp is None or hum is None:
        raise ValueError("Temperatura ou umidade ausente")

    # 2️⃣ Converte strings em números, se necessário
    if isinstance(temp, str) or isinstance(hum, str):
        try:
            temp = float(temp)
            hum = float(hum)
        except Exception:
            raise ValueError("Valores de temperatura/umidade inválidos")

    # 3️⃣ Valida se são números reais válidos
    if math.isnan(temp) or math.isnan(hum) or math.isinf(temp) or math.isinf(hum):
        raise ValueError("Leitura inválida (NaN/Inf)")

    # 4️⃣ Checa intervalos físicos plausíveis
    if not (-40.0 <= temp <= 80.0):
        raise ValueError(f"Temperatura fora do intervalo plausível: {temp}")

    if not (0.0 <= hum <= 100.0):
        raise ValueError(f"Umidade fora do intervalo plausível: {hum}")

    # 5️⃣ Arredonda para duas casas decimais
    temp = round(temp, 2)
    hum = round(hum, 2)

    # 6️⃣ Retorna o dicionário formatado
    return {
        "temperature_celsius": temp,
        "humidity_percent": hum,
        "recorded_at": datetime.utcnow(),
    }
