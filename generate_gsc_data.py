# generate_gsc_data.py
import pandas as pd
import numpy as np

np.random.seed(42)

QUERIES = [
    # Requêtes locales — forte intention locale
    ("agence digitale Guadeloupe", 850, 12, 3.2),
    ("community manager Guadeloupe", 620, 8, 4.1),
    ("création site web Guadeloupe", 1200, 45, 2.8),
    ("référencement SEO Guadeloupe", 430, 6, 5.3),
    ("agence communication 971", 380, 4, 6.1),
    ("marketing digital Guadeloupe", 560, 9, 4.7),
    ("publicité Facebook Guadeloupe", 290, 3, 7.2),
    ("formation réseaux sociaux Guadeloupe", 210, 2, 8.4),
    ("consultant SEO Guadeloupe", 175, 1, 9.1),
    ("agence web Pointe-à-Pitre", 340, 5, 5.8),
    ("stratégie digitale Antilles", 195, 2, 7.6),
    ("création logo Guadeloupe", 280, 4, 6.3),
    ("rédaction web SEO 971", 145, 1, 10.2),
    ("audit SEO Guadeloupe", 165, 1, 9.8),
    ("gestion réseaux sociaux PME Guadeloupe", 310, 3, 6.9),

    # Requêtes métier — intention informationnelle
    ("comment améliorer son référencement local", 920, 11, 3.9),
    ("stratégie réseaux sociaux entreprise", 780, 22, 2.4),
    ("différence SEO SEA", 650, 18, 2.1),
    ("comment créer une fiche Google My Business", 540, 31, 1.8),
    ("taux engagement Instagram 2024", 480, 14, 3.1),
    ("algorithme Facebook entreprise", 390, 8, 4.5),
    ("contenu evergreen blog entreprise", 275, 3, 7.1),
    ("KPI community manager", 310, 5, 5.9),
    ("brief créatif réseaux sociaux", 195, 2, 8.2),
    ("calendrier éditorial template", 420, 12, 3.6),
    ("comment mesurer ROI réseaux sociaux", 365, 4, 6.4),
    ("outils veille concurrentielle gratuits", 290, 6, 5.1),
    ("newsletter vs réseaux sociaux", 215, 2, 8.7),
    ("landing page conversion optimisation", 445, 13, 3.3),
    ("persona marketing exemple", 510, 19, 2.9),

    # Requêtes longue traîne — très ciblées
    ("agence digitale spécialisée tourisme Guadeloupe", 120, 1, 11.3),
    ("community manager freelance Guadeloupe", 95, 0, 12.1),
    ("formation marketing digital Guadeloupe 2024", 140, 1, 10.8),
    ("création site e-commerce Antilles", 185, 2, 8.9),
    ("pub Instagram Guadeloupe restaurant", 110, 0, 13.2),
    ("agence SEO locale petite entreprise", 230, 2, 7.8),
    ("comment choisir agence digitale", 680, 8, 4.2),
    ("prix community manager freelance", 590, 7, 4.6),
    ("outils planification réseaux sociaux gratuits", 445, 11, 3.7),
    ("erreurs SEO débutants", 380, 9, 4.0),

    # Requêtes bien positionnées (pas des gaps)
    ("digitallis guadeloupe", 1850, 312, 1.1),
    ("digitallis agence", 920, 187, 1.2),
    ("agence digitallis", 740, 145, 1.3),
    ("digitallis avis", 310, 58, 1.8),
    ("site internet guadeloupe pas cher", 890, 67, 2.2),
    ("création site vitrine guadeloupe", 560, 41, 2.6),
    ("agence web basse-terre", 245, 19, 3.4),
    ("devis site web guadeloupe", 420, 32, 2.9),
    ("wordpress guadeloupe", 195, 14, 4.1),
    ("refonte site web guadeloupe", 275, 18, 3.8),
]

def build_gsc_csv(queries):
    rows = []
    for query, base_imp, base_clics, base_pos in queries:
        # Légère variation aléatoire pour simuler données réelles
        impressions = int(base_imp * np.random.uniform(0.85, 1.15))
        clics = int(base_clics * np.random.uniform(0.80, 1.20))
        clics = max(0, clics)
        position = round(base_pos * np.random.uniform(0.90, 1.10), 1)
        ctr = round((clics / impressions * 100), 2) if impressions > 0 else 0.0

        # Page associée simulée
        slug = query.lower().replace(" ", "-").replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("ô", "o")
        page = f"https://www.digitallis.fr/blog/{slug}/"

        rows.append({
            "query": query,
            "page": page,
            "impressions": impressions,
            "clics": clics,
            "ctr": ctr,
            "position": position
        })

    df = pd.DataFrame(rows)
    df = df.sort_values("impressions", ascending=False).reset_index(drop=True)
    return df

if __name__ == "__main__":
    df = build_gsc_csv(QUERIES)
    df.to_csv("data/gsc_digitallis_simule.csv", index=False, encoding="utf-8-sig")

    # Aperçu des gaps détectés
    gaps = df[(df["impressions"] > 100) & (df["clics"] < 10)]
    print(f"Total requêtes : {len(df)}")
    print(f"Gaps SEO détectés : {len(gaps)}")
    print("\nTop 10 opportunités :")
    print(gaps[["query", "impressions", "clics", "position"]].head(10).to_string(index=False))
