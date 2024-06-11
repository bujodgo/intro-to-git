class kriptovaluta:
    def __init__(self, ime, vrijednost, trend_24h, trend_24h_postotak, trend_7h, trend_7h_postotak) -> None:
        self.ime = ime
        self.vrijednost = vrijednost
        self.trend_24h = trend_24h
        self.trend_24h_postotak = trend_24h_postotak
        self.trend_7h = trend_7h
        self.trend_7h_postotak = trend_7h_postotak
        

    def __str__(self) -> str:
        return f"{self.ime}, {self.vrijednost}, 24H: {self.trend_24h_postotak}, ({self.trend_24h}), 7D: {self.trend_7h_postotak}, ({self.trend_7h})"