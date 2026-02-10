class Pix:        

    def process(self, pix_key, amount, description):
        # --- Simula lib externa de PIX ---
        return {
            "status": "ok", 
            "receiver": {
                "pix_key": pix_key,
                "amount": amount,
                "description": description
            }
        }