class TransactionProcessor:
    def __init__(self, transaction_type, payload):
        self.transaction_type = transaction_type
        self.payload = payload

    def process(self):
        if self.transaction_type == "pix":
            # Chamada ao parceiro PIX
            response = self._process_pix(
                self.payload.get("pix_key"),
                self.payload.get("amount"),
                self.payload.get("description")
            )
            return response

        elif self.transaction_type == "ted":
            # Chamada ao parceiro TED
            response = self._process_ted(
                self.payload.get("bank_code"),
                self.payload.get("agency"),
                self.payload.get("account_number"),
                self.payload.get("amount"),
            )
            return response

        elif self.transaction_type == "boleto":
            # Chamada ao gateway de boleto
            response = self._process_boleto(
                self.payload.get("payer_name"),
                self.payload.get("amount"),
            )
            return response

        else:
            raise ValueError("Unsupported transaction type")

    def _process_pix(self, pix_key, amount, description):
        # --- integração simulada com provedor PIX ---
        print(f"[PIX] Enviando pagamento para chave {pix_key}, valor {amount}")
        return {"status": "ok", "provider": "BankPix"}

    def _process_ted(self, bank_code, agency, account_number, amount):
        # --- integração simulada com banco para TED ---
        print(
            f"[TED] Transferindo {amount} para banco "
            f"{bank_code}-{agency}/{account_number}"
        )
        return {"status": "pending", "provider": "LegacyBank"}

    def _process_boleto(self, payer_name, amount):
        # --- integração simulada com gateway de boletos ---
        print(f"[BOLETO] Emitindo boleto no valor {amount} para {payer_name}")
        return {"status": "issued", "provider": "BoletoGateway"}