from typing import List

class KeywordFilter:
    def __init__(self, keywords: List[str]):
        self.keywords = keywords

    def load_keywords(self, filepath: str):
        with open(filepath, 'r') as file:
            self.keywords = [line.strip() for line in file.readlines()]

    def filter_comments(self, comments: List[str]) -> List[str]:
        filtered_comments = []
        for comment in comments:
            if any(keyword in comment.lower() for keyword in self.keywords):
                filtered_comments.append(comment)
        return filtered_comments

    def block_comments(self, comments: List[str]) -> List[str]:
        blocked_comments = []
        for comment in comments:
            if any(keyword in comment.lower() for keyword in self.keywords):
                blocked_comments.append(comment)
        return blocked_comments