export type predictResponseType = {
  prediction: {
    value: number
    fraudProbability: number
  }
} | {
  erro: string
}

export type predictRequestType = {
  ratio_to_median_purchase_price: number
  online_order: number
  distance_from_home: number
  distance_from_last_transaction: number
}
