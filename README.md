# 🤖 Desafio Final - Python: Inteligência Artificial Aplicada

## 📋 Sobre o Projeto

Este projeto é o **desafio final** do curso **"Python: Inteligência Artificial Aplicada"** da **Alura**. O objetivo é criar uma aplicação que processa e analisa resenhas de aplicativos utilizando inteligência artificial local.

## 🎯 Funcionalidades

- 📁 **Carregamento de dados**: Leitura de arquivo com resenhas de aplicativos
- 🧠 **Processamento com IA**: Análise e classificação automática usando modelo local
- 🌐 **Tradução**: Conversão de resenhas para português
- 📊 **Análise de sentimento**: Classificação em Positiva, Neutra ou Negativa
- 📈 **Dashboard**: Visualização de estatísticas das avaliações

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **OpenAI API** (compatível)
- **LM Studio** - Execução local de modelos de IA
- **Modelo**: Google Gemma-3n-e4b
- **JSON** para estruturação de dados

## 🏠 Execução Local com LM Studio

Este projeto utiliza o **LM Studio** para executar modelos de IA localmente, garantindo:

- ✅ **Privacidade total** dos dados
- ⚡ **Processamento rápido** sem dependência de internet
- 💰 **Custo zero** em APIs externas
- 🔒 **Controle completo** sobre o modelo utilizado

### Configuração do LM Studio

1. Instale o [LM Studio](https://lmstudio.ai/)
2. Baixe o modelo `google/gemma-3n-e4b`
3. Execute o servidor local na porta `1234`
4. O projeto se conectará automaticamente via `http://localhost:1234/v1`

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Chamfrado/DesafioFinal-Alura-PythonAI.git
   ```

2. **Instale as dependências**:
   ```bash
   pip install openai
   ```

3. **Configure o LM Studio** com o modelo Gemma-3n-e4b

4. **Execute o projeto**:
   ```bash
   python Desafio.py
   ```

## 📁 Estrutura do Projeto

```
📦 Desafio Final - IA Python
├── 📄 Desafio.py                    # Código principal
├── 📄 Resenhas_App_ChatGPT.txt      # Dataset de resenhas
├── 🖼️ Enunciado.png                # Imagem do enunciado
└── 📄 README.md                     # Este arquivo
```

## 📊 Exemplo de Saída

```
### DASHBOARD DE REVIEWS ###
{'Positiva': 15, 'Neutra': 3, 'Negativa': 7}

### REVIEWS ###
Usuario1 Aplicativo muito bom, recomendo! Positiva####
Usuario2 Funciona bem, mas poderia melhorar Neutra####
...
```

## 🎓 Sobre o Curso

Este projeto faz parte do curso **"Python: Inteligência Artificial Aplicada"** da **Alura**, onde aprendemos:

- Integração com APIs de IA
- Processamento de linguagem natural
- Análise de sentimentos
- Estruturação de dados com JSON
- Boas práticas em Python

## 👨‍💻 Autor

Desenvolvido como parte do desafio final do curso da Alura.

---

⭐ **Gostou do projeto?** Deixe uma estrela no repositório!