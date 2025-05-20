from vnexpress_scraper import VNExpressScraper
from cafef_scraper import CafeFScraper
from tienphong_scraper import TienPhongScraper

def get_scraper(name, headle, base_url, output_csv, process, persistent_file, emb_csv):
    if name == "VNExpress":
        return VNExpressScraper(headle, base_url, output_csv, process, persistent_file, emb_csv)
    elif name == "TienPhong":
        return TienPhongScraper(headle, base_url, output_csv, process, persistent_file, emb_csv)
    else:
        raise ValueError(f"Unknown scraper: {name}")