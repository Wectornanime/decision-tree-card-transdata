export type FormStepsType = {
  label: string;
  name: string;
  description: string;
  type: 'number' | 'boolean';
}

export const FormSteps: FormStepsType[] = [
  {
    label: 'Preço médio da compra',
    name: 'ratio_to_median_purchase_price',
    description: 'Esse valor nos ajuda a entender se a compra está muito acima ou abaixo do valor típico.',
    type: 'number',
  },
  {
    label: 'Pedido online?',
    name: 'online_order',
    description: 'Sabemos que pedidos online podem ter diferentes padrões de fraude.',
    type: 'boolean',
  },
  {
    label: 'Distância de casa',
    name: 'distance_from_home',
    description: 'Compras feitas longe de casa podem levantar suspeitas.',
    type: 'number',
  },
  {
    label: 'Distância da última transação',
    name: 'distance_from_last_transaction',
    description: 'Ajuda a identificar comportamentos suspeitos como saltos grandes entre transações.',
    type: 'number',
  }
];
