import random
from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import re


class ActionGiveRandomWord(Action):

    def name(self) -> Text:
        return "action_give_random_word"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        words = tracker.get_slot("word_list")
        if len(words) == 0:
            response = requests.get('https://randomwordgenerator.com/json/words_ws.json')
            if response.status_code == 200:
                words = list(map(lambda word: word["word"]["value"], response.json()["data"]))
            else:
                dispatcher.utter_message("Không thể lấy từ, xin hãy thử lại sau")
                return []
        word = random.choice(words)
        dispatcher.utter_message(word)
        return [SlotSet("word_list", words), SlotSet("last_used_word", word)]


class ActionExplainLastUsedWord(Action):

    def name(self) -> Text:
        return "action_explain_last_used_word"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_slot("last_used_word")
        if len(last) == 0:
            dispatcher.utter_message("Không có từ được lưu trong bộ nhớ")
            return []
        else:
            last = last.lower()
        explained = tracker.get_slot("explained_words")
        usedExplanation = list(filter(lambda explanation: explanation["word"] == last, explained))
        if len(usedExplanation) > 0:
            dispatcher.utter_message(usedExplanation[0]["explanation"])
            return []
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{last}")
        if response.status_code != 200:
            dispatcher.utter_message("Không thể lấy thông tin, xin hãy thử lại sau")
            return []
        url = response.json()[0]['sourceUrls'][0]
        response = response.json()[0]["meanings"]
        info = [f"Thông tin về từ {last}:"]
        for data in response:
            translation = requests.get("https://clients5.google.com/translate_a/t",
                                       {"client": "dict-chrome-ex", "sl": "en", "tl": "vi",
                                        "q": [data["partOfSpeech"], data["definitions"][0]["definition"]]})
            if translation.status_code != 200:
                dispatcher.utter_message("Không thể lấy thông tin, xin hãy thử lại sau")
                return []
            str = f"Từ loại: {translation.json()[0]}\n"
            str += f"Nghĩa: {translation.json()[1]}"
            if "example" in data['definitions'][0]:
                str += f"\nVí dụ: {data['definitions'][0]['example']}"
            info.append(str)
        info.append(f"Tìm hiểu thêm tại {url}")
        msg = "\n\n".join(info)
        dispatcher.utter_message(msg)
        explained.append({
            "word": last,
            "explanation": msg
        })
        return [SlotSet("explained_words", explained)]


class ActionExplainGivenWord(Action):

    def name(self) -> Text:
        return "action_explain_given_word"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = tracker.get_slot("given_word")
        if len(word) == 0:
            dispatcher.utter_message("Không nhận dạng được từ yêu cầu, xin hãy thử lại sau")
            return []
        else:
            word = word.lower()
        explained = tracker.get_slot("explained_words")
        usedExplanation = list(filter(lambda explanation: explanation["word"] == word, explained))
        if len(usedExplanation) > 0:
            dispatcher.utter_message(usedExplanation[0]["explanation"])
            return []
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code != 200:
            dispatcher.utter_message("Không nhận dạng được từ yêu cầu, xin hãy thử lại sau")
            return []
        url = response.json()[0]['sourceUrls'][0]
        response = response.json()[0]["meanings"]
        info = [f"Thông tin về từ {word}:"]
        for data in response:
            translation = requests.get("https://clients5.google.com/translate_a/t",
                                       {"client": "dict-chrome-ex", "sl": "en", "tl": "vi",
                                        "q": [data["partOfSpeech"], data["definitions"][0]["definition"]]})
            if translation.status_code != 200:
                dispatcher.utter_message("Không thể lấy thông tin, xin hãy thử lại sau")
                return []
            str = f"Từ loại: {translation.json()[0]}\n"
            str += f"Nghĩa: {translation.json()[1]}"
            if "example" in data['definitions'][0]:
                str += f"\nVí dụ: {data['definitions'][0]['example']}"
            info.append(str)
        info.append(f"Tìm hiểu thêm tại {url}")
        msg = "\n\n".join(info)
        dispatcher.utter_message(msg)
        explained.append({
            "word": word,
            "explanation": msg
        })
        return [SlotSet("last_used_word", word), SlotSet("explained_words", explained)]


class ActionTranslate(Action):

    def name(self) -> Text:
        return "action_translate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sentence = tracker.latest_message.get("text")
        matches = re.findall(r'"(.*?)"', sentence)
        if len(matches) == 0 or len(matches[0]) == 0:
            dispatcher.utter_message("Không nhận dạng được câu yêu cầu, xin hãy để câu trong dấu ngoặc kép")
            return []
        else:
            sentence = matches[0]
        response = requests.get("https://clients5.google.com/translate_a/t",
                                {"client": "dict-chrome-ex", "sl": "en", "tl": "vi", "q": sentence})
        if response.status_code != 200:
            dispatcher.utter_message("Không dịch đuược câu yêu cầu, xin hãy thử lại")
            return []
        dispatcher.utter_message(f"Tiếng Anh: {sentence}\nTiếng Việt: {response.json()[0]}")
        return []
