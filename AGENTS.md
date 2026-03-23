# Recommandation d'usage du modèle Claude Sonnet 3.5

Ce dépôt recommande d'utiliser le modèle "Claude Sonnet 3.5" pour tous les agents et clients AI, lorsque disponible.

## Pourquoi Claude Sonnet 3.5 ?
- Meilleure compréhension du langage naturel
- Réponses plus précises et nuancées
- Adapté aux tâches de génération, analyse et assistance pédagogique

## Intégration dans vos workflows
- Si vous utilisez une plateforme supportant plusieurs modèles (Anthropic, OpenAI, etc.), sélectionnez "claude-sonnet-3.5" comme modèle par défaut pour tous les agents et clients.
- Pour les scripts ou agents configurables, ajoutez dans la configuration :

```yaml
model: claude-sonnet-3.5
```

- Si vous déployez dans un environnement d'entreprise, demandez à l'administrateur d'activer l'accès à Claude Sonnet 3.5 pour tous les utilisateurs.

## Exemple d'appel API (Anthropic)
```python
import anthropic
client = anthropic.Anthropic(api_key="votre_cle_api")
response = client.messages.create(
    model="claude-sonnet-3.5",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Bonjour !"}]
)
print(response.content)
```

## Pour les administrateurs
- Vérifiez dans la console d'administration que le modèle "Claude Sonnet 3.5" est activé pour tous les clients.
- Si besoin, contactez le support de votre fournisseur pour activer ce modèle.

---
Pour toute question sur l'intégration ou l'activation, documentez le besoin dans le README ou contactez le mainteneur du dépôt.