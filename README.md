# SalesBoost – Realtime E-commerce Recommendation System
# 🚀 SalesBoost — Real-Time Recommendation Engine

SalesBoost est un moteur de recommandation **temps réel** conçu pour analyser les interactions utilisateurs et générer des recommandations personnalisées 🚀  
Il utilise un pipeline Big Data complet basé sur Kafka, Spark Streaming, MongoDB & Redis.

---

## ✅ Technologies utilisées

| Technologie | Rôle |
|------------|------|
| FastAPI | API REST des recommandations |
| Kafka | File d’événements utilisateurs |
| Spark Streaming | Traitement temps réel + scoring |
| MongoDB | Base produits |
| Redis | Stockage des scores & top produits |
| React | Interface utilisateur |
| Docker Compose | Déploiement complet du stack |

---

## 🔥 Fonctionnalités principales

✅ Recommandations mises à jour en temps réel  
✅ Scores calculés en fonction des actions (view/click/buy)  
✅ API REST ultra rapide avec FastAPI  
✅ Simulation d’activité utilisateur  
✅ UI moderne pour visualiser les produits recommandés  

---

## 🧩 Architecture du Projet

```
Frontend (React)
       ⬇️ REST
Backend API (FastAPI) ➡️ Redis ➡️ MongoDB
       ⬆️              ⬆️
Spark Streaming ⬅️ Kafka ⬅️ Simulation des events
```

---

## 🐳 Installation & Lancement (Docker)

```bash
cd salesboost_project/infra/docker
docker-compose up -d
```

Cela démarre automatiquement ⬇️  
✅ MongoDB  
✅ Redis  
✅ Kafka + Zookeeper  
✅ Spark Master + 2 Workers  
✅ FastAPI (port 8000)

---

## ⚙️ Spark Streaming — Lancer le Consumer

```bash
docker exec -it spark-master bash
cd /app/streaming
spark-submit --master spark://spark-master:7077 events_consumer.py
```

---

## 🎯 Simulation des événements Kafka

```bash
python simulation/kafka_producer.py
```

Chaque event met à jour les scores des produits dans Redis ✅

---

## 🌍 Accès API FastAPI

👉 http://localhost:8000/docs

| Méthode | Route | Description |
|--------|-------|-------------|
| GET | `/recommend/{user_id}` | Top produits recommandés |
| GET | `/` | Status API |

Exemple réponse JSON ✅

```json
{
  "user_id": 1,
  "recommendations": [
    { "id": "p3", "name": "iPhone 14", "score": 110 }
  ]
}
```

---

## 🖥️ Frontend UI

```bash
cd salesboost_project/frontend
npm install
npm start
```

Accessible ici 👉 http://localhost:3000  

---

## 📌 Structure du projet

```
salesboost_project/
│
├── backend/
├── data-pipeline/spark/
├── frontend/
├── simulation/
└── infra/docker/
```

---

## 👨‍💼 Auteur

Développé par **Mamou**  
Master Big Data & IA — Projet académique ⭐

---

## 🚀 Roadmap

✅ Pipeline temps réel opérationnel  
⬜ Modèle ML ALS ou Deep Learning  
⬜ Dashboard analytics  
⬜ A/B testing & personnalisation avancée  

---

### ⭐ SalesBoost — Transforme les interactions en ventes ⚡
