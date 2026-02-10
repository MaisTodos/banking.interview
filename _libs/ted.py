class Ted:        

    def executar(self, bank_code, agency, account_number, amount):
        # --- Simula lib externa de TED ---
        return {
            "status": 200, 
            "tipo": "ted",
            "recebedor": {
                "conta": f"{bank_code}-{agency}/{account_number}",
                "valor": amount
            }
        }