from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, headle, base_url, output_csv, process, persistent_file, emb_csv):
        self.headle = headle
        self.base_url = base_url
        self.output_csv = output_csv
        self.process = process
        self.persistent_file = persistent_file
        self.emb_csv = emb_csv
        self.articles = []

    @abstractmethod
    def scrape(self):
        pass
