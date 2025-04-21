export type getStatsResponse = {
  total: number
  classes: {
    [key: string]: number
  },
  medias: {
      ratio_to_median_purchase_price: number,
      distance_from_home: number,
      distance_from_last_transaction: number
  }
}
