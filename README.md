<div align = 'center'>
  
![Header](./Assets/banner.gif)
  
</div>
<h1 align="left">Little Things About Me</h1>

➡ Artificial Intelligence Engineering Student at Institut Teknologi Sepuluh Nopember (Indonesia)  
➡ Focused on building practical and intelligent systems  
➡ Currently focusing on Natural Language Processing and Retrieval-Augmented Generation  

**Personal Web:** [fahmialfayadh.site](https://fahmialfayadh.site)

---

### Connect With Me

<p align="center">
  <a href="https://instagram.com/fahmialfayadh"><img src="https://skillicons.dev/icons?i=instagram" alt="Instagram" /></a>
  <a href="https://linkedin.com/in/fahmialfayadh"><img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn" /></a>
  <a href="https://www.kaggle.com/fahmialfayadh"><img src="https://cdn.simpleicons.org/kaggle/20BEFF" width="48" height="48" alt="Kaggle" /></a>
</p>

---

```python
import torch.nn as nn

class FahmiAlfayadh(nn.Module):
    def __init__(self):
        super().__init__()
        self.search = Search()
        self.critic = Critic()
        self.builder = Builder()
        self.knowledge = Knowledge(
            domains=["Artifical Intelegence", "Applied Math", "Astronomy", "Anthropology", "History"],
        )

    def forward(self, curiosity, brain_energy: int = 1000):
           query = curiosity

           while brain_energy > 0:
               evidence = self.search(query)
               insight = self.critic(evidence)
               self.knowledge.add(insight)

               if not insight.follow_up:
                   break

               query = insight.follow_up
               brain_energy -= 1

           if insight.buildable:
               return self.builder(insight)

           return insight

```

### Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,rust,js,flask,sqlite,git,linux,pytorch,sklearn,pandas,numpy" alt="Tech Stack" />
</p>

| Domain | Focus |
|---|---|
| **Machine Learning** | Classical supervised & unsupervised learning, statistical & probabilistic modeling, ensembles & gradient boosting, tabular deep learning, anomaly detection, dimensionality reduction. Mainly **scikit-learn**, **XGBoost / LightGBM / CatBoost**, **PyTorch** |
| **Deep Learning** |Multilayer Perceptron (MLP), Convolutional Neural Network (CNN), Recurrent Neural Network (RNN), Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), Graph Neural Network (GNN) and Vision Transformers (ViT) built with **PyTorch** |
| **ML Engineering** | Feature engineering, AutoML, hyperparameter optimization, model interpretability, imbalanced learning. **Optuna**, **SHAP**, **AutoGluon** |
| **NLP & RAG** | Transformer models, embeddings, semantic search, retrieval pipelines. **Hugging Face**, **LangChain**, **Qdrant**, **FAISS** |
| **Data & Visualization** | Data processing, scientific computing, exploratory analysis. **Polars**, **Pandas**, **NumPy**, **SciPy**, **Plotly** |
| **Security** | Applied cryptography and data security|

---

<table align="center">
  <tr>
    <td valign="top">
      <img
        src="https://github-stats-extended.vercel.app/api?username=Fahmialfayadh&custom_title=My%20Github%20Stats&include_all_commits=true&show_icons=true&hide_rank=True&rank_icon=default&theme=swift&hide_border=true&card_width=400"
        alt="My GitHub Stats"
        width="400"
      />
    </td>
    <td valign="top">
      <img
        src="https://wakatime.com/share/@d5dc60ca-1de7-4689-9193-5d2c7c5c586a/8fa73f02-e86a-45fb-88c9-dc49cec8a0c8.svg"
        alt="Top Languages"
        width="400"
      />
    </td>
  </tr>
</table>

---

### AI-Assisted Coding Stats

<p align="center">
  <img
    src="./Assets/ai-coding.svg?v=1795489863491755683"
    alt="AI Coding Percentage"
    width="400"
  />
</p>
