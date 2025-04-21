export type predictResponse = {
  prediction: {
    value: number
    fraudProbability: number
  }
} | {
  erro: string
}
