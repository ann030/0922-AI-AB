"""
BMI 計算器 (BMI Calculator)
計算公式: BMI = 體重(公斤) / 身高(公尺)^2
衛生福利部標準:
  - 體重過輕: BMI < 18.5
  - 正常範圍: 18.5 <= BMI < 24.0
  - 體重過重: 24.0 <= BMI < 27.0
  - 輕度肥胖: 27.0 <= BMI < 30.0
  - 中度肥胖: 30.0 <= BMI < 35.0
  - 重度肥胖: BMI >= 35.0
"""

def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """透過身高(公分)與體重(公斤)計算 BMI"""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi: float) -> str:
    """根據台灣衛福部標準判斷 BMI 體位分類"""
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 24.0:
        return "正常範圍"
    elif 24.0 <= bmi < 27.0:
        return "體重過重"
    elif 27.0 <= bmi < 30.0:
        return "輕度肥胖"
    elif 30.0 <= bmi < 35.0:
        return "中度肥胖"
    else:
        return "重度肥胖"

def main():
    print("=" * 30)
    print("      BMI 身體質量指數計算器     ")
    print("=" * 30)

    try:
        height_input = input("請輸入您的身高 (公分 cm): ").strip()
        height_cm = float(height_input)

        weight_input = input("請輸入您的體重 (公斤 kg): ").strip()
        weight_kg = float(weight_input)

        if height_cm <= 0 or weight_kg <= 0:
            print("錯誤：身高和體重必須大於 0！")
            return

        bmi = calculate_bmi(height_cm, weight_kg)
        category = get_bmi_category(bmi)

        print("-" * 30)
        print(f"您的身高：{height_cm} cm")
        print(f"您的體重：{weight_kg} kg")
        print(f"您的 BMI 值為：{bmi}")
        print(f"體位判定：{category}")
        print("-" * 30)

    except ValueError:
        print("輸入錯誤：請輸入有效的數字！")

if __name__ == "__main__":
    main()
