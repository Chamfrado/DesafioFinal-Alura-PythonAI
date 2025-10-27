#1 - Carregando Arquivo
perguntas = []
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
  for linha in arquivo:
    perguntas.append(linha.strip())


#2 - Enviando ao modelo
from openai import OpenAI

client_openai = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3n-e4b",
    messages=[
        {"role": "system", "content": "Você é uma IA em que recebe uma lista de dados sobre resenhas e separa os dados conforme a vontade do cliente "},
        {"role": "user", "content": "Tenho uma lista de avaliações e preciso que você separe os dados dela em: usuario, resenha original, resenha_pt(tradução) "
        "e avaliação (Positiva, neutra ou negativa). Me devolva as informações em um JSON , quero apenas o JSON , nenhum texto a mais"
        }
    ],
    temperature=1.0,
)

print(resposta_do_llm.choices[0].message.content)
json_de_resenhas = resposta_do_llm.choices[0].message.content
#3 Transformando em Lista de Dicionarios

import json

json_de_resenhas_limpo = json_de_resenhas.replace("```json", "").replace("```", "") # type: ignore

dict_resenhas = json.loads(json_de_resenhas_limpo)
print(dict_resenhas)

#4 - Funções com o dicionario
dict_contagem = {"Positiva": 0, "Neutra": 0, "Negativa": 0}
join_resenhas = ""
for resenha in dict_resenhas:
  dict_contagem[resenha["avaliacao"]] += 1
  join_resenhas += f"{resenha['usuario']} {resenha['resenha_pt']} {resenha['avaliacao']}####"


print("### DASHBOARD DE REVIEWS ###")
print(dict_contagem)

print("### REVIEWS ###")
print(join_resenhas)
