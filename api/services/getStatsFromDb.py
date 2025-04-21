class GetStatsFromDb():
    def __init__(self, repository):
        self.repository = repository

    def getStats(self):
        total = self.repository.getCountAllRegisters()
        resultados = self.repository.getCountOfClass()
        medias = self.repository.getFeaturesMedia()

        return {
            "total": total,
            "classes": {str(k): v for k, v in resultados},
            "medias": {
                "ratio_to_median_purchase_price": medias[0],
                "distance_from_home": medias[1],
                "distance_from_last_transaction": medias[2]
            }
        }
