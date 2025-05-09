# -*- coding: utf-8 -*-
"""
Ash - 您的 AI 心理健康支援夥伴

本程式旨在提供初步的心理健康支援、情緒開導和日常陪伴。
它結合了自然語言處理、簡單的情緒分析和您提供的特定開導語句，
目標是成為一個高可近性、初步預警的心理支持工具。

模型的核心功能包括：
- 對話互動：與使用者進行文字對話。
- 情緒初步判斷：分析使用者語句中的情緒傾向。
- 心理問題初步篩選：根據使用者描述的症狀，給予初步的疾病可能性判斷和就醫建議。
- 正向開導與陪伴：提供積極的回應和您提供的開導語句。
- 特殊功能整合：
    - 目標設定 (基於 Talk to Ash AI 的理念)
    - 人聲情緒分析 (概念性整合 Ellipsis Health 的技術)
    - CBT 模組化引導 (概念性整合 Woebot 的 CBT 原則)
    - 文化敏感性回應 (結合文化思維和情緒表達)
    - 可愛貓貓圖片/文字回應 (作為輕鬆元素)

請注意：本程式提供的資訊僅為初步判斷和支持，不能取代專業的心理諮詢和醫療診斷。
如果使用者出現嚴重的心理問題，請務必建議他們尋求專業協助。

"""

import random
# 可以根據需求導入更複雜的 NLP 和情緒分析函式庫，例如 NLTK、spaCy、transformers 等
# 這裡先使用簡單的字詞匹配和規則判斷

class Ash:
    def __init__(self):
        self.positive_responses = [
            "沒錯，你很棒！",
            "這是一個很好的想法！",
            "我相信你可以做到。",
            "你正在進步，真為你感到高興。",
            "保持積極的心態！"
        ]
        self.comforting_responses_breakup = [
            "這不一定是你的錯，有時候離開是因為不適合。",
            "她拋棄你是她的損失，你值得更好的人。",
            "把重心放回自己身上，你會找到更珍惜你的人。",
            "這是一個重新開始的機會，你會變得更強大。",
            "時間會沖淡一切，給自己一些時間療傷。"
        ]
        self.cat_responses = [
            "摸摸可愛的貓貓 (>^.^<)",
            "喵～ (づ｡◕‿‿◕｡)づ",
            "貓咪也來給你一個溫暖的抱抱 (=^･ω･^=)",
            "呼嚕嚕...希望這個聲音能讓你放鬆。",
            "看看這隻可愛的貓貓圖片：[在這裡放圖片連結]" # 可以替換成實際的圖片連結或隨機圖片 API
        ]
        self.cbt_modules = {
            "認知重建": ["找出你的負面想法", "挑戰這些想法的證據", "建立更積極的想法"],
            "情緒調節": ["辨識你的情緒", "了解情緒的起因", "學習健康的應對方式"]
            # 可以根據認知行為療法的原則擴充更多模組
        }
        # 這裡可以加入更複雜的心理疾病關鍵字和初步判斷規則
        self.mental_health_keywords = {
            "憂鬱": ["心情低落", "失去興趣", "疲倦", "失眠", "食慾不振"],
            "焦慮": ["緊張", "不安", "擔心", "恐慌", "心跳加速"],
            # ... 更多心理疾病關鍵字
        }
        self.severity_levels = {
            1: "可能需要關注",
            2: "建議尋求專業評估",
            3: "強烈建議尋求專業協助"
        }

    def greet(self):
        return "你好！我是 Ash，你的 AI 心理健康支援夥伴。今天有什麼我可以幫你嗎？"

    def analyze_sentiment(self, text):
        # 這是一個非常簡化的情緒分析
        positive_words = ["開心", "快樂", "舒服", "放鬆", "喜歡", "好"]
        negative_words = ["難過", "傷心", "生氣", "沮喪", "痛苦", "糟"]
        positive_count = sum(1 for word in text if word in positive_words)
        negative_count = sum(1 for word in text if word in negative_words)

        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"

    def check_mental_health_keywords(self, text):
        potential_issues = {}
        for issue, keywords in self.mental_health_keywords.items():
            count = sum(1 for keyword in keywords if keyword in text)
            if count > 0:
                potential_issues[issue] = count
        return potential_issues

    def determine_severity(self, potential_issues):
        severity = 0
        for issue, count in potential_issues.items():
            severity += count
        if severity >= 3:
            return 3
        elif severity >= 1:
            return 2
        else:
            return 1

    def provide_support(self, text):
        sentiment = self.analyze_sentiment(text)
        mental_health_issues = self.check_mental_health_keywords(text)

        if mental_health_issues:
            severity = self.determine_severity(mental_health_issues)
            response = "我注意到你提到了一些不適的感覺。"
            for issue, count in mental_health_issues.items():
                response += f" 你提到了 {issue} 相關的詞語 {count} 次。"
            response += f" 根據你的描述，我初步判斷你的情況可能屬於 {self.severity_levels[severity]}。"
            if severity >= 2:
                response += " 為了更了解你的情況，強烈建議你諮詢專業的心理健康專家。"
            else:
                response += " 試著和朋友或家人聊聊，或者做一些讓你放鬆的事情。"
            return response

        if "分手" in text or "被拋棄" in text:
            return random.choice(self.comforting_responses_breakup)

        if "貓" in text or "可愛" in text:
            return random.choice(self.cat_responses)

        if "目標" in text or "計畫" in text:
            return "設定目標是很棒的第一步！你願意告訴我你的目標是什麼嗎？我們可以一起想想如何達成。" # 基於 Talk to Ash AI 的理念

        if sentiment == "negative":
            return random.choice(self.positive_responses) + " 記得，你並不孤單。"
        elif sentiment == "positive":
            return random.choice(self.positive_responses)
        else:
            return random.choice(["嗯嗯。", "我明白了。", "可以多告訴我一些嗎？"])

    def start_cbt_module(self, module_name):
        if module_name in self.cbt_modules:
            return f"好的，我們開始進行 {module_name}。\n" + "\n".join([f"{i+1}. {step}" for i, step in enumerate(self.cbt_modules[module_name])])
        else:
            return "抱歉，目前沒有這個 CBT 模組。"

    def cultural_sensitive_response(self, text, culture="預設"):
        # 這部分需要更深入的文化理解和資料
        if culture == "台灣":
            if "加油" in text:
                return "謝謝你的鼓勵！我們會繼續努力。"
            # 可以加入更多針對台灣文化的回應
        return self.provide_support(text) # 預設情況下還是提供一般的心理支持

    def process_input(self, user_input):
        # 在這裡可以加入人聲分析的介面 (需要整合相關函式庫和 API)
        # 這裡先簡化為文字輸入
        print(f"使用者說：{user_input}")
        response = self.cultural_sensitive_response(user_input, culture="台灣") # 假設使用者是台灣文化背景
        return response

if __name__ == "__main__":
    ash = Ash()
    print(ash.greet())
    while True:
        user_input = input("> ")
        if user_input.lower() in ["再見", "掰掰", "結束"]:
            print("很高興今天能和你聊天，再見！")
            break
        response = ash.process_input(user_input)
        print(f"Ash 說：{response}")