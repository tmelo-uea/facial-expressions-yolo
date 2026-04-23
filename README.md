# Classificação de Expressões Faciais com YOLOv8

Projeto educacional para demonstrar o treino de um classificador de expressões faciais usando YOLOv8.

## 🎯 Objetivo

Mostrar o pipeline completo de Machine Learning:
- Exploração de dados
- Preparação do dataset
- Treinamento de modelo
- Validação e testes
- Deploy

## 📊 Dataset

- **Classes**: 9 expressões faciais
  - Angry (Raiva)
  - Calm (Calmo)
  - Confused (Confuso)
  - Disgust (Desgosto)
  - Fear (Medo)
  - Happy (Feliz)
  - Neutral (Neutro)
  - Sad (Triste)
  - Surprise (Surpresa)

- **Treino**: 180 imagens (20 por classe)
- **Validação**: 45 imagens (5 por classe)
- **Tamanho**: 13MB (otimizado para Colab)

## 🚀 Quick Start no Colab

Clique para abrir no Colab (substituir SEU_USUARIO):

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tmelo-uea/facial-expressions-yolo/blob/main/notebooks/facial_expressions_yolo.ipynb)

**Passos:**
1. Clique no link acima
2. File → Save a copy in Drive
3. Execute célula por célula
4. Treinamento leva ~10 minutos

## 📈 Resultados Esperados

- **Top-1 Accuracy**: ~85-90%
- **Tempo de treino**: ~10 minutos (GPU T4)
- **Tempo de inferência**: ~50ms por imagem

## 💻 Estrutura

```
facial-expressions-yolo/
├── README.md                              # Este arquivo
├── requirements.txt                       # Dependências Python
├── convert_yolo_to_classification.py      # Script de conversão YOLO→Classificação
├── dataset-sample/                        # Dataset (13MB)
│   ├── train/ (180 imagens)
│   └── val/ (45 imagens)
└── notebooks/
    └── facial_expressions_yolo.ipynb      # Notebook do curso
```

## 📚 Conteúdo do Notebook

1. **Setup e Instalações** - Instalar YOLOv8 e dependências
2. **Configuração do Ambiente** - Verificar GPU
3. **Download do Dataset** - Clonar do GitHub
4. **Exploração de Dados** - Entender estrutura
5. **Visualização** - Ver amostras
6. **Preparação** - Arquivo data.yaml
7. **Treinamento** - YOLOv8 Small
8. **Validação** - Avaliar modelo
9. **Testes** - Predições em imagens
10. **Análise** - Gráficos de desempenho
11. **Produção** - Como usar o modelo
12. **Conclusões** - Próximos passos

## 🔧 Requisitos

- Google Colab (gratuito)
- Conexão com internet
- Conta GitHub

## 📋 Uso Local (Opcional)

```bash
# Instalar dependências
pip install -r requirements.txt

# Se precisar converter dataset YOLO para classificação
python convert_yolo_to_classification.py /path/to/yolo/dataset
```

## 🎓 Aprendizados

Neste projeto você aprenderá:
- Fundamentos de Machine Learning
- Como usar YOLOv8
- Trabalhar com datasets
- Validação e métricas
- Deploy de modelos

## 📖 Referências

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Ultralytics GitHub](https://github.com/ultralytics/ultralytics)
- [Kaggle - 9 Facial Expressions](https://www.kaggle.com/datasets)

## 👨‍🏫 Instrutor

Tiago Eugênio - Curso de Detecção de Objetos em Tempo Real com YOLO e Python

---

**Última atualização**: 2026-04-23  
**Versão**: 1.0
