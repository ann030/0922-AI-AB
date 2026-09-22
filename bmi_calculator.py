"""
多語言 BMI 計算器 (Multilingual BMI Calculator)
支援語言 / Supported Languages:
  1. 繁體中文 (Traditional Chinese)
  2. English (英文)
  3. 日本語 (Japanese)
  4. Español (西班牙文)
"""

from typing import Dict, Any


MESSAGES: Dict[str, Dict[str, Any]] = {
    "zh_TW": {
        "name": "繁體中文",
        "title": "BMI 身體質量指數計算器",
        "prompt_height": "請輸入您的身高 (公分 cm): ",
        "prompt_weight": "請輸入您的體重 (公斤 kg): ",
        "err_positive": "錯誤：身高和體重必須大於 0！",
        "err_invalid": "輸入錯誤：請輸入有效的數字！",
        "label_height": "您的身高",
        "label_weight": "您的體重",
        "label_bmi": "您的 BMI 值",
        "label_category": "體位判定",
        "categories": {
            "underweight": "體重過輕",
            "normal": "正常範圍",
            "overweight": "體重過重",
            "mild_obese": "輕度肥胖",
            "moderate_obese": "中度肥胖",
            "severe_obese": "重度肥胖",
        },
    },
    "en": {
        "name": "English",
        "title": "BMI (Body Mass Index) Calculator",
        "prompt_height": "Please enter your height (cm): ",
        "prompt_weight": "Please enter your weight (kg): ",
        "err_positive": "Error: Height and weight must be greater than 0!",
        "err_invalid": "Input Error: Please enter a valid number!",
        "label_height": "Height",
        "label_weight": "Weight",
        "label_bmi": "BMI Value",
        "label_category": "Category",
        "categories": {
            "underweight": "Underweight",
            "normal": "Normal weight",
            "overweight": "Overweight",
            "mild_obese": "Mild obesity",
            "moderate_obese": "Moderate obesity",
            "severe_obese": "Severe obesity",
        },
    },
    "ja": {
        "name": "日本語",
        "title": "BMI (体格指数) 計算ツール",
        "prompt_height": "身長を入力してください (cm): ",
        "prompt_weight": "体重を入力してください (kg): ",
        "err_positive": "エラー：身長と体重は0より大きくなければなりません！",
        "err_invalid": "入力エラー：有効な数値を入力してください！",
        "label_height": "身長",
        "label_weight": "体重",
        "label_bmi": "BMI値",
        "label_category": "判定",
        "categories": {
            "underweight": "低体重 (痩せ型)",
            "normal": "普通体重",
            "overweight": "肥満 (1度) / 過体重",
            "mild_obese": "肥満 (2度)",
            "moderate_obese": "肥満 (3度)",
            "severe_obese": "肥満 (4度)",
        },
    },
    "es": {
        "name": "Español",
        "title": "Calculadora de IMC (Índice de Masa Corporal)",
        "prompt_height": "Por favor ingrese su altura (cm): ",
        "prompt_weight": "Por favor ingrese su peso (kg): ",
        "err_positive": "¡Error: La altura y el peso deben ser mayores que 0!",
        "err_invalid": "¡Error de entrada: Por favor ingrese un número válido!",
        "label_height": "Altura",
        "label_weight": "Peso",
        "label_bmi": "Valor de IMC",
        "label_category": "Clasificación",
        "categories": {
            "underweight": "Bajo peso",
            "normal": "Peso normal",
            "overweight": "Sobrepeso",
            "mild_obese": "Obesidad leve",
            "moderate_obese": "Obesidad moderada",
            "severe_obese": "Obesidad severa",
        },
    },
}

LANG_KEYS = ["zh_TW", "en", "ja", "es"]


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """透過身高(公分)與體重(公斤)計算 BMI"""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_category_key(bmi: float) -> str:
    """依據 BMI 數值取得分類代碼"""
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.0:
        return "normal"
    elif 24.0 <= bmi < 27.0:
        return "overweight"
    elif 27.0 <= bmi < 30.0:
        return "mild_obese"
    elif 30.0 <= bmi < 35.0:
        return "moderate_obese"
    else:
        return "severe_obese"


def choose_language() -> str:
    """讓使用者選擇語言介面"""
    print("=" * 60)
    print("  語言選擇 / Select Language / 言語選択 / Seleccione idioma")
    print("=" * 60)
    print("  1. 繁體中文 (Traditional Chinese)")
    print("  2. English (英語)")
    print("  3. 日本語 (Japanese)")
    print("  4. Español (Spanish)")
    print("  5. 多語言全部顯示 (Display All)")
    print("=" * 60)

    choice = input("請選擇 / Select [1-5] (預設/Default: 1): ").strip()
    mapping = {"1": "zh_TW", "2": "en", "3": "ja", "4": "es", "5": "all"}
    return mapping.get(choice, "zh_TW")


def display_results(lang_code: str, height_cm: float, weight_kg: float, bmi: float, cat_key: str):
    """根據選擇的語言輸出結果"""
    print("-" * 60)
    if lang_code == "all":
        for k in LANG_KEYS:
            msg = MESSAGES[k]
            cat_text = msg["categories"][cat_key]
            print(f"[{msg['name']}]")
            print(f"  {msg['label_height']}: {height_cm} cm | {msg['label_weight']}: {weight_kg} kg")
            print(f"  {msg['label_bmi']}: {bmi} | {msg['label_category']}: {cat_text}")
    else:
        msg = MESSAGES[lang_code]
        cat_text = msg["categories"][cat_key]
        print(f"{msg['label_height']}:   {height_cm} cm")
        print(f"{msg['label_weight']}:   {weight_kg} kg")
        print(f"{msg['label_bmi']}:   {bmi}")
        print(f"{msg['label_category']}:   {cat_text}")
    print("-" * 60)


def main():
    selected_lang = choose_language()
    prompt_lang = "zh_TW" if selected_lang in ("zh_TW", "all") else selected_lang
    msg = MESSAGES[prompt_lang]

    print("\n" + "=" * 60)
    print(f"  {msg['title']}")
    print("=" * 60)

    try:
        height_input = input(msg["prompt_height"]).strip()
        height_cm = float(height_input)

        weight_input = input(msg["prompt_weight"]).strip()
        weight_kg = float(weight_input)

        if height_cm <= 0 or weight_kg <= 0:
            print(f"\n{msg['err_positive']}")
            return

        bmi = calculate_bmi(height_cm, weight_kg)
        cat_key = get_category_key(bmi)
        display_results(selected_lang, height_cm, weight_kg, bmi, cat_key)

    except ValueError:
        print(f"\n{msg['err_invalid']}")


if __name__ == "__main__":
    main()
