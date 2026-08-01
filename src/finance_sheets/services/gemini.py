# gemini.py - define a classe GeminiService para interagir com o modelo Gemini da Google GenAI

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiService:

    # Inicializa o cliente Gemini com a chave de API do ambiente
    def __init__(self):
        self.gemini_client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    # Interpreta o texto do usuário e retorna um JSON com os campos necessários para registrar a transação
    def interpret_text(self, text, date):
        prompt = f"""
        Você é um assistente especializado em organizar transações financeiras.

        Sua tarefa é analisar a mensagem do usuário e identificar se ela descreve uma transação financeira.

        Se a mensagem NÃO descrever uma transação:
            Não execute nenhuma etapa de extração.
            Retorne apenas o seguinte JSON:
                Campo "type": response,
                Campo "resposta":
                    - Gere uma resposta curta, natural, como se você fosse um pastor evangélico.
                    - Não mencione que a mensagem não é uma transação financeira.
                    - Não peça informações adicionais, a menos que seja necessário para responder.
                    - Exemplos:
                    - Agradecimento → "De nada!"
                    - "Bom dia" → "Bom dia! Como posso ajudar?"
                    - Pergunta comum → responda normalmente.
            Interrompa o processamento imediatamente. Não adicione nenhum outro campo, texto, explicação ou comentário.

        Prossiga aqui caso a mensagem descreva uma transação

        Retorne APENAS um JSON válido, sem texto adicional.
        O JSON deve conter exatamente estes 8 campos:

        - type: "transaction"

        - data: data da transação no formato AAAA-MM-DD.
            - Caso a mensagem não informe uma data, use a data de hoje.
            - Sua referência para hoje é {date}

        - descricao: o objeto ou motivo principal da transação.
            - Exemplo: "Pizza", "Salário", "Sonta de luz", "Presente para João".

        - valor: valor numérico da transação em reais.
            - Retorne apenas o número, sem "R$", sempre positivo.

        - tipo: classifique como:
            - "Entrada" para dinheiro recebido.
            - "Saída" para dinheiro gasto.

        - categoria: classifique a transação em uma categoria adequada.
            Exemplos:
            - "Lazer"
            - "Custo fixo"
            - "Alimentação"
            - "Transporte"
            - "Presente"
            - "Salário"
            - "Saúde"
            - "Outros"

        - conta: conta ou origem do dinheiro utilizada.
            Exemplos:
            - "Itaú"
            - "Bradesco"
            - "Dinheiro"
            - "Nubank"
            - "Não informado" caso não seja possível identificar.

        - pago: informe se a transação já foi paga.
            - Retorne true ou false.
            - Caso a mensagem não informe, considere true.

        - metodo: método de pagamento.
            Exemplos:
                - "Débito"
                - "Crédito"
                - "Dinheiro"
                - "Pix"
                - "Transferência"
            - Caso não informado e não tenha parcelas retorne débito, 
            - Caso não informado e tenha parcelas, retorne crédito
        
        - quantidade_parcelas: número total de parcelas da compra.
            - Se a mensagem informar a quantidade de parcelas, utilize esse valor.
            - Se não for possível identificar a quantidade de parcelas, retorne None.

        - valor_parcela: valor de cada parcela.
            - Se a compra não for parcelada (1 parcela), retorne None.
            - Se a mensagem informar o valor da parcela, utilize-o.
            - Caso a compra seja parcelada e o valor da parcela não seja informado, calcule:
                valor_parcela = valor / quantidade_parcelas.

        Regras:
        - Não invente informações que não estejam na mensagem, exceto pelos valores padrões definidos acima.
        - Valores retornados tem letra inicial maiúscula
        - Dinheiro pode ser tanto método como conta

        Mensagem:
        {text}
        """

        response = self.gemini_client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        return response.text

gemini_service = GeminiService()
