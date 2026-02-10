class Boleto:        

    def pagar(self, payer_name, amount):
        # --- Simula lib externa de Boleto ---
        return {
            "status": "issued",
            "provider": "BoletoGateway",
            "destinatorio": {
                "nome": payer_name, 
                "valor": amount
            }
        }