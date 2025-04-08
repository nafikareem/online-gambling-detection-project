import os

class KeywordFilter:
    def __init__(self):
        self.gambling_keywords = set()
        self.gambling_sites = set()
        self.gambling_emojis = set(['💰', '🎰', '🔥', '💎', '⚡', '🚀'])

    def load_keywords(self, keywords_file):
        """Memuat kata kunci dari file teks."""
        if os.path.exists(keywords_file):
            with open(keywords_file, 'r', encoding='utf-8') as f:
                for line in f:
                    keyword = line.strip().lower()
                    if keyword:  # Pastikan tidak kosong
                        self.gambling_keywords.add(keyword)
        default_keywords = ['jp', 'wd', 'cuan', 'menang', 'modal', 'rezeki', 'jackpot', 'jakpot', 
                            'hoki', 'untung', 'main', 'spin', 'sultan', 'gacor', 'caerr']
        default_sites = ['manjurbet', 'aero88', 'dora77', 'alexis17', 'pulau777', 'koislot', 'miya88']
        self.gambling_keywords.update(default_keywords)
        self.gambling_sites.update(default_sites)

    def is_gambling_related(self, text):
        """Memeriksa apakah teks mengandung unsur perjudian."""
        text_lower = text.lower()
        return (any(keyword in text_lower for keyword in self.gambling_keywords) or
                any(site in text_lower for site in self.gambling_sites) or
                any(emoji in text_lower for emoji in self.gambling_emojis))

    def filter_comments(self, comments_df):
        """Filter komentar berdasarkan kata kunci dan mengembalikan list teks yang terdeteksi."""
        filtered = []
        for text in comments_df['processed_text']:
            if self.is_gambling_related(text):
                filtered.append(text)
        return filtered