"""
雙語 BMI 計算器 (Bilingual BMI Calculator)
計算公式 / Formula: BMI = 體重 weight (kg) / [身高 height (m)]^2
衛生福利部標準 / MOHW Standards:
  - 體重過輕 / Underweight: BMI < 18.5
  - 正常範圍 / Normal weight: 18.5 <= BMI < 24.0
  - 體重過重 / Overweight: 24.0 <= BMI < 27.0
  - 輕度肥胖 / Mild obesity: 27.0 <= BMI < 30.0
  - 中度肥胖 / Moderate obesity: 30.0 <= BMI < 35.0
  - 重度肥胖 / Severe obesity: BMI >= 35.0
"""

from typing import Tuple


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """透過身高(公分)與體重(公斤)計算 BMI / Calculate BMI using height (cm) and weight (kg)"""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi: float) -> Tuple[str, str]:
    """
    根據台灣衛福部標準判斷 BMI 體位分類 (返回中英雙語標籤)
    Determine BMI category based on Taiwan MOHW standards (returns Chinese and English labels)
    """
    if bmi < 18.5:
        return "體重過輕", "Underweight"
    elif 18.5 <= bmi < 24.0:
        return "正常範圍", "Normal weight"
    elif 24.0 <= bmi < 27.0:
        return "體重過重", "Overweight"
    elif 27.0 <= bmi < 30.0:
        return "輕度肥胖", "Mild obesity"
    elif 30.0 <= bmi < 35.0:
        return "中度肥胖", "Moderate obesity"
    else:
        return "重度肥胖", "Severe obesity"


def main():
    print("=" * 60)
    print("  BMI 身體質量指數計算器 / BMI (Body Mass Index) Calculator")
    print("=" * 60)

    try:
        height_prompt = "請輸入您的身高 (公分 cm) / Please enter your height (cm): "
        height_input = input(height_prompt).strip()
        height_cm = float(height_input)

        weight_prompt = "請輸入您的體重 (公斤 kg) / Please enter your weight (kg): "
        weight_input = input(weight_prompt).strip()
        weight_kg = float(weight_input)

        if height_cm <= 0 or weight_kg <= 0:
            print("\n錯誤：身高和體重必須大於 0！")
            print("Error: Height and weight must be greater than 0!")
            return

        bmi = calculate_bmi(height_cm, weight_kg)
        category_zh, category_en = get_bmi_category(bmi)

        print("-" * 60)
        print(f"您的身高 / Height:        {height_cm} cm")
        print(f"您的體重 / Weight:        {weight_kg} kg")
        print(f"您的 BMI 值 / BMI:        {bmi}")
        print(f"體位判定 / Category:      {category_zh} ({category_en})")
        print("-" * 60)

    except ValueError:
        print("\n輸入錯誤：請輸入有效的數字！")
        print("Input Error: Please enter a valid numerical value!")


if __name__ == "__main__":
    main()
