import base64


class Base64Util:
    @staticmethod
    def encode_file(file_path):
        try:
            with open(file_path, "rb") as file:
                return base64.b64encode(file.read()).decode()
        except Exception as e:
            raise Exception(f"Erro ao codificar o arquivo: {e}")
